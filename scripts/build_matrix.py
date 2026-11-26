"""Bangun matriks gen x isolat (results/amr_presence_absence.csv) dari tabel terkurasi.

Aturan sel (lihat workflow/analysis_notes.md, log Hari 7):
  1   : ada >= 1 hit 'counted' untuk fitur itu pada isolat itu
  NA  : tidak ada hit 'counted', tetapi ada hit 'note' (belum bisa dinyatakan ada atau tidak)
  0   : tidak ada hit sama sekali

Jalankan dari folder mana pun:  python scripts/build_matrix.py
Argumen opsional (untuk uji dengan data tiruan):
  python scripts/build_matrix.py <hits.csv> <quality.csv> <metadata.csv> <keluaran.csv>
"""
import re
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
HITS = ROOT / "results" / "amr_hits_curated.csv"
QUALITY = ROOT / "results" / "assembly_quality.csv"
METADATA = ROOT / "metadata" / "genome_metadata.csv"
OUT_CSV = ROOT / "results" / "amr_presence_absence.csv"

# Batas FAIL QC (analysis_notes.md, QC.watch qualibact-v1.0). Isolat di luar rentang tidak masuk matriks.
LEN_MIN, LEN_MAX = 4_100_000, 6_300_000
GC_MIN, GC_MAX = 50.09, 51.13

ID_COLS = ["Feature", "Feature_type", "Feature_subtype", "Drug_class"]


def parse_note(notes: str, key: str):
    """Ambil nilai 'key=...' dari kolom Notes tabel terkurasi ('Subtype=POINT; Method=POINTX; ...')."""
    m = re.search(rf"(?:^|; ){key}=([^;]+)", notes)
    return m.group(1).strip() if m else None


def feature_type(subtype: str) -> str:
    # POINT (substitusi) dan POINT_DISRUPT (frameshift/stop) sama-sama mutasi titik pada gen kromosom.
    return "point_mutation" if subtype.upper().startswith("POINT") else "acquired"


def qc_pass_ids(quality: pd.DataFrame) -> list:
    ok = quality["Total_length_bp"].astype(float).between(LEN_MIN, LEN_MAX) & \
         quality["GC_pct"].astype(float).between(GC_MIN, GC_MAX)
    return sorted(quality.loc[ok, "Sample_ID"])


def build(hits: pd.DataFrame, isolates: list) -> pd.DataFrame:
    unknown = set(hits["Sample_ID"]) - set(isolates)
    if unknown:
        sys.exit(f"GALAT: hit milik isolat di luar daftar (gagal QC atau tidak ada di metadata): {sorted(unknown)}")
    if not set(hits["Detection_category"]) <= {"counted", "note"}:
        sys.exit(f"GALAT: Detection_category tak dikenal: {set(hits['Detection_category'])}")

    hits = hits.copy()
    hits["Subtype"] = hits["Notes"].fillna("").map(lambda n: parse_note(n, "Subtype"))
    hits["Method"] = hits["Notes"].fillna("").map(lambda n: parse_note(n, "Method"))
    if hits["Subtype"].isna().any():
        sys.exit("GALAT: ada baris tanpa 'Subtype=' di Notes; jalankan ulang curate_hits.py")

    # Atribut per fitur. Satu fitur harus punya satu golongan dan satu subtipe di semua isolat.
    attrs = hits.groupby("Feature").agg(
        Feature_subtype=("Subtype", "unique"), Drug_class=("Drug_class_or_mechanism", "unique"))
    for feat, row in attrs.iterrows():
        if len(row["Feature_subtype"]) > 1 or len(row["Drug_class"]) > 1:
            sys.exit(f"GALAT: {feat} punya subtipe atau golongan yang tidak konsisten: {dict(row)}")
    attrs = attrs.map(lambda v: v[0])
    attrs["Feature_type"] = attrs["Feature_subtype"].map(feature_type)

    rows = []
    for feat, a in attrs.iterrows():
        h = hits[hits["Feature"] == feat]
        row = {"Feature": feat, "Feature_type": a["Feature_type"],
               "Feature_subtype": a["Feature_subtype"], "Drug_class": a["Drug_class"]}
        notes = []
        for sid in isolates:
            hs = h[h["Sample_ID"] == sid]
            counted = hs[hs["Detection_category"] == "counted"]
            noted = hs[hs["Detection_category"] == "note"]
            row[sid] = 1 if len(counted) else (pd.NA if len(noted) else 0)
            for _, r in noted.iterrows():
                notes.append(f"{sid}: {r['Method']} (identitas {r['Pct_identity']}%, cakupan {r['Pct_coverage']}%)")
            for _, r in hs.iterrows():   # jejak yang hilang saat banyak baris diringkas jadi satu sel
                m = re.search(r"gen sama di \d+ contig", r["Notes"])
                if m:
                    notes.append(f"{sid}: {m.group(0)}")
        row["Notes"] = "; ".join(dict.fromkeys(notes))
        rows.append(row)

    mat = pd.DataFrame(rows, columns=ID_COLS + isolates + ["Notes"])
    mat["_t"] = mat["Feature_type"].map({"acquired": 0, "point_mutation": 1})
    mat = mat.sort_values(["_t", "Drug_class", "Feature"], kind="stable").drop(columns="_t").reset_index(drop=True)
    return mat


def cross_check(hits: pd.DataFrame, mat: pd.DataFrame, isolates: list) -> None:
    """Jumlah angka 1 per isolat harus sama dengan jumlah fitur unik 'counted' per isolat di tabel terkurasi."""
    expected = hits[hits["Detection_category"] == "counted"].groupby("Sample_ID")["Feature"].nunique()
    bad = []
    for sid in isolates:
        got = int((mat[sid] == 1).sum())
        want = int(expected.get(sid, 0))
        if got != want:
            bad.append((sid, got, want))
    if bad:
        sys.exit(f"GALAT uji silang: (isolat, 1 di matriks, fitur counted di tabel) = {bad}")
    if mat["Feature"].duplicated().any():
        sys.exit("GALAT: ada baris ganda di matriks")


def main(argv) -> int:
    if len(argv) == 4:
        hits_p, quality_p, meta_p, out_p = map(Path, argv)
    elif not argv:
        hits_p, quality_p, meta_p, out_p = HITS, QUALITY, METADATA, OUT_CSV
    else:
        sys.exit(__doc__)

    meta_ids = set(pd.read_csv(meta_p, dtype=str)["Sample_ID"])
    quality = pd.read_csv(quality_p, dtype=str)
    if set(quality["Sample_ID"]) != meta_ids:
        sys.exit(f"GALAT: Sample_ID assembly_quality.csv dan metadata tidak sama: "
                 f"{sorted(set(quality['Sample_ID']) ^ meta_ids)}")
    isolates = qc_pass_ids(quality)
    excluded = sorted(meta_ids - set(isolates))

    hits = pd.read_csv(hits_p, dtype=str)
    mat = build(hits, isolates)
    cross_check(hits, mat, isolates)
    mat.to_csv(out_p, index=False, na_rep="NA")

    n_acq = int((mat["Feature_type"] == "acquired").sum())
    print(f"Isolat dalam matriks: {len(isolates)} | dikeluarkan karena QC: {excluded or 'tidak ada'}")
    print(f"Fitur: {len(mat)} (acquired {n_acq}, point_mutation {len(mat) - n_acq}) | "
          f"sel NA: {int(mat[isolates].isna().sum().sum())}")
    print("Angka 1 per isolat:", {s: int((mat[s] == 1).sum()) for s in isolates})
    print("Uji silang dengan tabel terkurasi: LOLOS")
    print(f"Ditulis: {out_p}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
