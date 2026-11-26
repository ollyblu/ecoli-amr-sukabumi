"""Jalankan ulang bagian lokal analisis: TSV mentah -> tabel terkurasi -> matriks -> figur.

Pemakaian (dari folder proyek):  python run_all.py
Langkah Galaxy (QUAST dan AMRFinderPlus) tidak ikut; keluaran mentahnya sudah ada di results/.
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STEPS = ["curate_hits.py", "build_matrix.py", "plot_figures.py"]

for name in STEPS:
    print(f"\n== {name} ==", flush=True)
    result = subprocess.run([sys.executable, str(ROOT / "scripts" / name)])
    if result.returncode != 0:
        sys.exit(f"{name} gagal (kode {result.returncode}); langkah berikutnya tidak dijalankan.")

print("\nSelesai: results/amr_hits_curated.csv, results/amr_presence_absence.csv, figures/*.png")
