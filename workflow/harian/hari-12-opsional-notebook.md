# Hari 12 (opsional): notebook Jupyter untuk figur 2

## Tujuan

Notebook `notebooks/fig2_heatmap.ipynb` membuat ulang figur 2 langkah demi langkah dengan pandas dan seaborn, lengkap dengan penjelasan di sel Markdown.

## Kaitan dengan silabus

`02-silabus-dry-lab.md`: Python dasar, pandas, visualisasi.

## Langkah

- [ ] Buat folder `notebooks/` dan notebook baru
- [ ] Sel 1: baca `results/amr_presence_absence.csv` dan `metadata/genome_metadata.csv`
- [ ] Sel 2: tampilkan ringkasan matriks (jumlah fitur, jumlah isolat, jumlah sel 1, 0, dan `NA`)
- [ ] Sel 3: urutkan baris per golongan antibiotik dan pisahkan `acquired` dari `point_mutation`
- [ ] Sel 4: gambar *heatmap*, lalu bandingkan dengan `figures/fig2_amr_heatmap.png`
- [ ] Tulis sel Markdown di antara sel kode yang menjelaskan **arti biologis** tiap langkah, bukan cara kerja kodenya
- [ ] *Restart and run all* sebelum menyimpan, supaya urutan sel benar
- [ ] Commit notebook beserta keluarannya, lalu tautkan dari README

## Hasil yang bisa dicek

- Notebook jalan dari atas ke bawah tanpa galat setelah *restart*
- *Heatmap* di notebook sama dengan figur 2

## Cek dirimu

1. Kalau pewawancara membuka notebook ini, bagian mana yang paling mungkin ditanyakan?
2. Pengelompokan baris apa yang paling membantu pembaca melihat pola?

## Templat log

```
### YYYY-MM-DD (Hari 12)
- **Langkah:** notebook figur 2
- **Input:** results/amr_presence_absence.csv; metadata/genome_metadata.csv
- **Parameter:** -
- **Hasil / file keluaran:** notebooks/fig2_heatmap.ipynb
- **Kendala dan solusinya:**
- **Pertanyaan yang muncul:**
```

Sebelumnya: [Hari 11](hari-11-opsional-jalur-lokal.md) · Berikutnya: [Hari 13+](hari-13-opsional-ekstensi.md)
