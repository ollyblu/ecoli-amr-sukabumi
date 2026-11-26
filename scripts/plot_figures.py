"""Buat dua figur dari results/amr_presence_absence.csv.

  figures/fig1_amr_count_per_isolate.png : batang bertumpuk per isolat (acquired / substitusi / frameshift-stop)
  figures/fig2_amr_heatmap.png           : heatmap fitur x isolat, baris dikelompokkan per golongan antibiotik

Kategori sumber isolat (hewan / pakan / lingkungan) BUKAN nilai NCBI. Pemetaannya ditulis eksplisit di
SOURCE_BY_HOST di bawah, dari kolom Host di metadata/genome_metadata.csv. Host yang belum ada di
pemetaan membuat skrip berhenti dengan galat.

Jalankan dari folder mana pun:  python scripts/plot_figures.py
"""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "results" / "amr_presence_absence.csv"
METADATA = ROOT / "metadata" / "genome_metadata.csv"
FIG1 = ROOT / "figures" / "fig1_amr_count_per_isolate.png"
FIG2 = ROOT / "figures" / "fig2_amr_heatmap.png"
DPI = 300

SOURCE_BY_HOST = {
    "Capra aegagrus hircus": "Hewan",
    "Bos taurus": "Hewan",
    "Anas platyrhynchos javanica": "Hewan",
    "Cygnus cygnus": "Hewan",
    "Ducks feed": "Pakan",
    "Laying hen feed": "Pakan",
    "Environment": "Lingkungan",
}
SOURCE_ORDER = ["Hewan", "Pakan", "Lingkungan"]
SOURCE_COLOR = {"Hewan": "#4C78A8", "Pakan": "#E6A23C", "Lingkungan": "#6BA368"}

# Warna kategori fitur (Fig 1 dan sel hitam di Fig 2 memakai skema terpisah)
C_ACQ, C_SUB, C_DIS = "#C0392B", "#2E6F9E", "#8E6BBF"
C_NA = "#BBBBBB"


def load():
    mat = pd.read_csv(MATRIX, dtype=str, keep_default_na=False)
    meta = pd.read_csv(METADATA, dtype=str)
    isolates = [c for c in mat.columns if c.startswith("SID")]

    unknown = sorted(set(meta["Host"]) - set(SOURCE_BY_HOST))
    if unknown:
        sys.exit(f"GALAT: Host belum ada di SOURCE_BY_HOST: {unknown}")
    meta["Source"] = meta["Host"].map(SOURCE_BY_HOST)
    if set(isolates) - set(meta["Sample_ID"]):
        sys.exit(f"GALAT: isolat di matriks tidak ada di metadata: {sorted(set(isolates) - set(meta['Sample_ID']))}")

    # Urutan isolat: per sumber, lalu Sample_ID
    meta = meta[meta["Sample_ID"].isin(isolates)].copy()
    meta["_s"] = meta["Source"].map(SOURCE_ORDER.index)
    order = meta.sort_values(["_s", "Sample_ID"])["Sample_ID"].tolist()
    source = meta.set_index("Sample_ID")["Source"]
    return mat, order, source


def fig1(mat, order, source):
    acq = mat[mat["Feature_type"] == "acquired"]
    sub = mat[(mat["Feature_type"] == "point_mutation") & (mat["Feature_subtype"] == "POINT")]
    dis = mat[(mat["Feature_type"] == "point_mutation") & (mat["Feature_subtype"] == "POINT_DISRUPT")]
    other = mat[~mat.index.isin(acq.index.union(sub.index).union(dis.index))]
    if len(other):
        sys.exit(f"GALAT: fitur dengan tipe/subtipe tak terduga: {other['Feature'].tolist()}")

    def count(df):  # NA tidak dihitung sebagai 1
        return pd.Series({s: int((df[s] == "1").sum()) for s in order})

    n_acq, n_sub, n_dis = count(acq), count(sub), count(dis)

    fig, ax = plt.subplots(figsize=(9, 5.2))
    x = range(len(order))
    ax.bar(x, n_acq, color=C_ACQ, label="Gen acquired")
    ax.bar(x, n_sub, bottom=n_acq, color=C_SUB, label="Mutasi titik: substitusi asam amino")
    ax.bar(x, n_dis, bottom=n_acq + n_sub, color=C_DIS, label="Mutasi titik: frameshift atau stop prematur")
    total = n_acq + n_sub + n_dis
    for i, s in enumerate(order):
        ax.text(i, total[s] + 0.12, str(total[s]), ha="center", va="bottom", fontsize=10)

    ax.set_xticks(list(x))
    ax.set_xticklabels(order)
    ax.set_ylabel("Jumlah fitur AMR terdeteksi")
    ax.set_ylim(0, max(total.max() + 1.5, 8))
    ax.set_xlim(-0.6, len(order) - 0.4)
    ax.yaxis.get_major_locator().set_params(integer=True)

    # Pita sumber di bawah sumbu x
    for src in SOURCE_ORDER:
        idx = [i for i, s in enumerate(order) if source[s] == src]
        if idx:
            ax.annotate("", xy=(min(idx) - 0.4, -0.115), xytext=(max(idx) + 0.4, -0.115),
                        xycoords=("data", "axes fraction"), textcoords=("data", "axes fraction"),
                        arrowprops=dict(arrowstyle="-", color=SOURCE_COLOR[src], lw=4))
            ax.text((min(idx) + max(idx)) / 2, -0.17, f"{src} (n = {len(idx)})", ha="center", va="top",
                    transform=ax.get_xaxis_transform(), color=SOURCE_COLOR[src], fontsize=10, fontweight="bold")

    ax.text(0.01, 0.80, "Tidak ada gen acquired terdeteksi.\nAssembly hanya memuat kromosom (tanpa plasmid),\n"
            "jadi nol di sini bukan bukti isolat bebas gen acquired.",
            transform=ax.transAxes, ha="left", va="top", fontsize=8.5, style="italic",
            bbox=dict(boxstyle="round", fc="white", ec="#999999"))
    ax.legend(loc="upper left", fontsize=8.5, frameon=False)
    ax.set_title("Fitur AMR per isolat E. coli (AMRFinderPlus 4.2.7, DB 2026-05-15.1)\n"
                 "9 isolat peternakan Sukabumi, PRJNA1075840", fontsize=11)
    sns.despine(ax=ax)
    fig.subplots_adjust(bottom=0.22)
    FIG1.parent.mkdir(exist_ok=True)
    fig.savefig(FIG1, dpi=DPI)
    plt.close(fig)
    return n_acq, n_sub, n_dis


def fig2(mat, order, source):
    m = mat.copy()
    # Urutan baris: acquired dulu, lalu golongan, lalu nama. Matriks dari build_matrix.py sudah terurut; diurutkan ulang agar mandiri.
    m["_t"] = m["Feature_type"].map({"acquired": 0, "point_mutation": 1})
    m = m.sort_values(["_t", "Drug_class", "Feature"], kind="stable").reset_index(drop=True)

    vals = m[order].replace({"NA": float("nan"), "0": 0, "1": 1}).astype(float)
    classes = m["Drug_class"].tolist()
    short = {"MULTIDRUG/AMPICILLIN/CHLORAMPHENICOL/QUINOLONE/RIFAMPIN/TETRACYCLINE": "MULTIDRUG (+5 kelas)"}
    class_lab = [short.get(c, c) for c in classes]

    n = len(m)
    fig = plt.figure(figsize=(10.5, 0.42 * n + 3.6))
    gs = fig.add_gridspec(2, 3, width_ratios=[0.15, 3.2, 2.0], height_ratios=[0.28, n],
                          hspace=0.04, wspace=0.03)
    ax_src = fig.add_subplot(gs[0, 1])
    ax_sub = fig.add_subplot(gs[1, 0])
    ax = fig.add_subplot(gs[1, 1])
    ax_cls = fig.add_subplot(gs[1, 2])

    # Heatmap: NA abu-abu, 0 putih, 1 biru tua
    cmap = ListedColormap(["#FFFFFF", "#1F3F66"])
    ax.set_facecolor(C_NA)  # sel NaN tidak digambar -> tampak abu-abu
    sns.heatmap(vals, ax=ax, cmap=cmap, vmin=0, vmax=1, cbar=False, linewidths=0.6, linecolor="#CCCCCC",
                xticklabels=order, yticklabels=m["Feature"].tolist())
    ax.set_xlabel("Isolat (Sample_ID)")
    ax.tick_params(axis="y", labelsize=9, left=False)
    ax.tick_params(axis="x", labelrotation=0, labelsize=9)
    for lbl in ax.get_yticklabels():
        lbl.set_style("italic")

    # Pita sumber di atas
    ax_src.set_xlim(0, len(order))
    ax_src.set_ylim(0, 1)
    for i, s in enumerate(order):
        ax_src.add_patch(plt.Rectangle((i, 0), 1, 1, color=SOURCE_COLOR[source[s]]))
    ax_src.axis("off")
    ax_src.set_title("Matriks presence/absence fitur AMR (1 = terdeteksi, 0 = tidak ada hit)", fontsize=11, pad=8, loc="left")

    # Pita subtipe di kiri: substitusi vs frameshift/stop
    ax_sub.set_xlim(0, 1)
    ax_sub.set_ylim(n, 0)
    for i, st in enumerate(m["Feature_subtype"]):
        col = {"POINT": C_SUB, "POINT_DISRUPT": C_DIS}.get(st, C_ACQ)
        ax_sub.add_patch(plt.Rectangle((0, i), 1, 1, color=col))
    ax_sub.axis("off")

    # Label golongan di kanan + garis pemisah antar golongan
    ax_cls.set_xlim(0, 1)
    ax_cls.set_ylim(n, 0)
    ax_cls.axis("off")
    start = 0
    for i in range(1, n + 1):
        if i == n or classes[i] != classes[start]:
            ax_cls.text(0.04, (start + i) / 2, class_lab[start], va="center", ha="left", fontsize=9)
            if i < n:
                ax.axhline(i, color="black", lw=1.4)
            start = i

    handles = [
        Patch(fc="#1F3F66", ec="#999999", label="1: hit terdeteksi"),
        Patch(fc="#FFFFFF", ec="#999999", label="0: tidak ada hit (bukan bukti gen tidak ada)"),
        Patch(fc=C_NA, ec="#999999", label="NA: hanya hit sebagian (PARTIALX dsb.); tidak ada di data ini"),
        Patch(fc=C_SUB, label="Pita kiri: mutasi titik, substitusi"),
        Patch(fc=C_DIS, label="Pita kiri: mutasi titik, frameshift/stop"),
    ] + [Patch(fc=SOURCE_COLOR[s], label=f"Pita atas: {s}") for s in SOURCE_ORDER]
    fig.legend(handles=handles, loc="lower center", ncol=2, fontsize=8.5, frameon=False,
               bbox_to_anchor=(0.5, 0.0))
    fig.text(0.5, 0.155, "Panel gen acquired kosong: assembly hanya memuat kromosom (tanpa plasmid).",
             ha="center", fontsize=8.5, style="italic")
    fig.subplots_adjust(left=0.2, right=0.97, top=0.93, bottom=0.23)
    fig.savefig(FIG2, dpi=DPI)
    plt.close(fig)


def main() -> int:
    mat, order, source = load()
    n_acq, n_sub, n_dis = fig1(mat, order, source)
    fig2(mat, order, source)
    print("Urutan isolat:", order)
    print("acquired:", n_acq.to_dict())
    print("substitusi:", n_sub.to_dict())
    print("frameshift/stop:", n_dis.to_dict())
    print(f"Ditulis: {FIG1}\nDitulis: {FIG2}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
