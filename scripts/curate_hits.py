"""Kurasi keluaran mentah AMRFinderPlus menjadi results/amr_hits_curated.csv.

Aturan deteksi mengikuti workflow/analysis_notes.md (ditetapkan sebelum melihat hasil).
Jalankan dari folder mana pun:  python scripts/curate_hits.py
"""
import re
import sys
import warnings
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "results" / "raw_tool_outputs"
METADATA = ROOT / "metadata" / "genome_metadata.csv"
OUT_CSV = ROOT / "results" / "amr_hits_curated.csv"

# Aturan deteksi: Method yang dihitung 1. Selain ini jadi 'note'.
COUNTED_METHODS = {"EXACTX", "ALLELEX", "BLASTX", "POINTX"}
KNOWN_NOTE_METHODS = {"PARTIALX", "PARTIAL_CONTIG_ENDX", "INTERNAL_STOPX", "HMM"}

TOOL = "AMRFinderPlus"
TOOL_VERSION = "4.2.7+galaxy0"
DB_VERSION = "V4.2-2026-05-15.1"

# Nama kolom AMRFinderPlus versi 4. Versi 3 memakai nama lain (Gene symbol, Element type, ...).
COL = {
    "feature": "Element symbol",
    "type": "Type",
    "subtype": "Subtype",
    "class": "Class",
    "subclass": "Subclass",
    "method": "Method",
    "coverage": "% Coverage of reference",
    "identity": "% Identity to reference",
    "contig": "Contig id",
    "start": "Start",
    "stop": "Stop",
}

OUT_COLUMNS = [
    "Sample_ID", "Feature", "Drug_class_or_mechanism", "Detection_category",
    "Pct_identity", "Pct_coverage", "Tool", "Tool_version", "DB_version", "Notes",
]

# Cocok untuk 'SID09_amrfinder.tsv' dan 'Galaxy12-[AMRFinderPlus on SID09].tabular'.
FILENAME_PATTERNS = [
    re.compile(r"^(?P<id>[A-Za-z0-9]+)_amrfinder\.tsv$"),
    re.compile(r"\[AMRFinderPlus on (?P<id>[A-Za-z0-9]+)\]"),
]
COVERAGE_WARN = 90.0  # di bawah ini dicatat di Notes (aturan tidak memakai cakupan)


def sample_id_from_name(name: str):
    for pat in FILENAME_PATTERNS:
        m = pat.search(name)
        if m:
            return m.group("id")
    return None


def drug_label(row) -> str:
    cls, sub = str(row[COL["class"]]), str(row[COL["subclass"]])
    return cls if cls == sub else f"{cls}/{sub}"


def main() -> int:
    meta_ids = set(pd.read_csv(METADATA, dtype=str)["Sample_ID"])

    files = sorted(p for p in RAW_DIR.iterdir()
                   if p.suffix in {".tsv", ".tabular"} and not p.name.lower().startswith("quast"))
    if not files:
        sys.exit(f"GALAT: tidak ada TSV AMRFinderPlus di {RAW_DIR}")

    records, seen = [], {}
    for path in files:
        sid = sample_id_from_name(path.name)
        if sid is None or sid not in meta_ids:
            sys.exit(f"GALAT: Sample_ID dari nama file '{path.name}' ({sid!r}) tidak cocok dengan {METADATA.name}")
        if sid in seen:
            sys.exit(f"GALAT: Sample_ID {sid} muncul di dua file: {seen[sid]} dan {path.name}")
        seen[sid] = path.name

        df = pd.read_csv(path, sep="\t", dtype=str)
        missing = [c for c in COL.values() if c not in df.columns]
        if missing:
            sys.exit(f"GALAT: {path.name} tidak punya kolom {missing}. Versi AMRFinderPlus berbeda?")

        df = df[df[COL["type"]] == "AMR"]  # hanya AMR; virulensi dan stress dibuang
        for _, r in df.iterrows():
            method = r[COL["method"]]
            if method in COUNTED_METHODS:
                category = "counted"
            else:
                category = "note"
                if method not in KNOWN_NOTE_METHODS:
                    warnings.warn(f"{sid}: Method tidak dikenal '{method}' pada {r[COL['feature']]}; dimasukkan ke 'note'")
            notes = [f"Subtype={r[COL['subtype']]}", f"Method={method}"]
            if float(r[COL["coverage"]]) < COVERAGE_WARN:
                notes.append(f"coverage {r[COL['coverage']]}% < {COVERAGE_WARN:g}%")
            records.append({
                "Sample_ID": sid,
                "Feature": r[COL["feature"]],  # jangan dipotong: gyrA_S83L tetap utuh
                "Drug_class_or_mechanism": drug_label(r),
                "Detection_category": category,
                "Pct_identity": r[COL["identity"]],
                "Pct_coverage": r[COL["coverage"]],
                "Tool": TOOL, "Tool_version": TOOL_VERSION, "DB_version": DB_VERSION,
                "_contig": r[COL["contig"]], "_locus": (r[COL["contig"]], r[COL["start"]], r[COL["stop"]]),
                "_notes": notes,
            })

    out = pd.DataFrame(records)
    if out.empty:
        out = pd.DataFrame(columns=OUT_COLUMNS)
    else:
        # Fitur yang sama di >1 contig pada satu isolat: dua baris, kejadiannya dicatat.
        # Fitur berbeda di lokus yang sama (mis. gyrA_D87N dan gyrA_S83L): tetap dua baris, dicatat.
        for (sid, feat), g in out.groupby(["Sample_ID", "Feature"]):
            if g["_contig"].nunique() > 1:
                for i in g.index:
                    out.at[i, "_notes"].append(f"gen sama di {g['_contig'].nunique()} contig")
        for (sid, locus), g in out.groupby(["Sample_ID", "_locus"]):
            if len(g) > 1:
                for i in g.index:
                    others = ",".join(x for x in g["Feature"] if x != out.at[i, "Feature"])
                    out.at[i, "_notes"].append(f"lokus sama dengan {others}")
        out["Notes"] = out["_notes"].apply("; ".join)
        out = out[OUT_COLUMNS].sort_values(["Sample_ID", "Feature"], kind="stable").reset_index(drop=True)

    out.to_csv(OUT_CSV, index=False)

    n_amr = len(out)
    print(f"Isolat diproses: {len(seen)} | baris AMR: {n_amr} | "
          f"counted: {(out['Detection_category'] == 'counted').sum()} | "
          f"note: {(out['Detection_category'] == 'note').sum()}")
    print(out.groupby("Sample_ID").size().reindex(sorted(meta_ids), fill_value=0).to_string())
    print(f"Ditulis: {OUT_CSV}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
