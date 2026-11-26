# Hari 8: figur dan literatur

## Tujuan

Dua PNG di `figures/` dibuat oleh `scripts/plot_figures.py`, dan 5 sampai 8 paper terkumpul dengan judul, penulis, tahun, dan DOI yang kamu cek sendiri.

## Prasyarat

- `results/amr_presence_absence.csv` dari Hari 7
- seaborn dan matplotlib terpasang, versinya ditambahkan ke `requirements.txt`

## Bagian A: figur (sekitar 1 jam)

- [x] **Figur 1**, `figures/fig1_amr_count_per_isolate.png`: diagram batang jumlah gen AMR *acquired* per isolat. Mutasi titik ditampilkan terpisah atau ditumpuk dengan warna lain, dan legendanya menjelaskan perbedaan itu
- [x] **Figur 2**, `figures/fig2_amr_heatmap.png`: *heatmap* matriks dengan seaborn, baris dikelompokkan per golongan antibiotik. Sel `NA` punya warna sendiri dan dijelaskan di legenda
- [x] Label sumbu memakai `Sample_ID`
- [x] Pertimbangkan anotasi sumber isolat (hewan, pakan, lingkungan) dari metadata, misalnya bilah warna di atas *heatmap*
- [x] Simpan dengan `dpi=300`, lalu buka PNG-nya dan periksa apakah label terbaca
- [ ] Commit (`Add figures 1 and 2`)

## Bagian B: literatur (sekitar 1 jam)

Kata kunci untuk PubMed (https://pubmed.ncbi.nlm.nih.gov) dan Google Scholar:

- `Escherichia coli Sukabumi farm whole genome` (paper sumber dataset, kalau ada)
- `antimicrobial resistance Escherichia coli poultry Indonesia`
- `ESBL Escherichia coli livestock Southeast Asia genome`
- `AMRFinderPlus` (paper tool, untuk *Methods*)
- `QUAST quality assessment genome assemblies` (paper tool, untuk *Methods*)

- [x] Kumpulkan 5 sampai 8 paper
- [x] Untuk tiap paper, catat judul, penulis pertama, tahun, jurnal, dan DOI langsung dari halaman paper, bukan dari ingatan atau jawaban chatbot
- [x] Tulis satu kalimat per paper: bagian laporan mana yang memakainya dan untuk klaim apa
- [x] Simpan daftarnya di `report/references.md`

| # | Penulis pertama, tahun | Judul | DOI | Dipakai di bagian | Untuk klaim |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

## Hasil yang bisa dicek

- Dua PNG terbaca tanpa perlu memperbesar
- Seseorang yang hanya melihat figur 2 bisa membedakan "tidak terdeteksi" dari "terdeteksi sebagian"
- Setiap DOI di daftar bisa dibuka di https://doi.org/

## Cek dirimu

1. Kenapa gen *acquired* dan mutasi titik dipisah di figur?
2. Kalau figur 1 menunjukkan isolat lingkungan punya gen lebih sedikit, kalimat seperti apa yang boleh kamu tulis dengan n = 2?
3. Paper mana yang paling mirip datasetmu, dan apa perbedaan metodenya?

## Templat log

```
### YYYY-MM-DD (Hari 8)
- **Langkah:** membuat figur 1 dan 2; mencari literatur
- **Input:** results/amr_presence_absence.csv; metadata/genome_metadata.csv
- **Parameter:** seaborn <versi>, matplotlib <versi>, dpi 300
- **Hasil / file keluaran:** figures/fig1_amr_count_per_isolate.png; figures/fig2_amr_heatmap.png; report/references.md (<n> paper)
- **Kendala dan solusinya:**
- **Pertanyaan yang muncul:**
```

Sebelumnya: [Hari 7](hari-07-matriks.md) · Berikutnya: [Hari 9](hari-09-laporan.md)
