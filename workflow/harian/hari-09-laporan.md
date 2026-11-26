# Hari 9: draf laporan

## Tujuan

Draf laporan berbahasa Inggris ada di `report/`, misalnya `report/report.md`, dengan bagian *Methods*, *Results*, *Discussion*, dan *Abstract*.

## Prasyarat

- Tabel QC, tabel terkurasi, matriks, dua figur, dan `report/references.md` sudah ada
- Tabel versi tool dan database di `../analysis_notes.md` lengkap

## Langkah

Tulis sesuai urutan ini, bukan urutan bagian di laporan.

- [x] ***Methods.*** Dataset dan kriteria inklusi, aturan QC beserta sumbernya, tool dan versinya (QUAST, AMRFinderPlus, versi database, server Galaxy), aturan deteksi, dan skrip Python. Hampir semuanya tinggal dipindahkan dari `analysis_notes.md`
- [x] ***Results.*** Tabel QC, jumlah hit per kategori, figur 1, figur 2. Hanya yang teramati, tanpa tafsiran
- [x] ***Discussion.*** Bandingkan dengan literatur, jelaskan pola yang terlihat, dan tulis keterbatasan:
  - genotipe bukan fenotipe; tidak ada data AST
  - n = 9, dan tiap kelompok sumber hanya 2 sampai 3 isolat
  - assembly berlevel *Chromosome*, sehingga plasmid bisa terpotong
  - satu tool dan satu versi database
  - Kelompok B tidak dianalisis
- [x] ***Abstract.*** Paling akhir, satu paragraf
- [ ] Baca ulang tiap kalimat klaim dengan tabel di bawah (draf sudah ditulis; kamu yang memeriksa)
- [ ] Commit (`Add report draft`)

## Merumuskan klaim

| Terlalu jauh | Sesuai data |
|---|---|
| "Isolate SID09 is resistant to tetracycline." | "*tet*(A) was detected in SID09." |
| "Environmental isolates carry fewer resistance genes." | "Under the chosen thresholds, fewer acquired AMR genes were detected in the two environmental isolates (n = 2)." |
| "The isolate lacks beta-lactam resistance." | "No acquired beta-lactamase gene was detected with AMRFinderPlus (database version ...)." |

Dengan 9 isolat, hindari uji statistik. Deskripsi yang jujur lebih kuat daripada nilai p dari n = 2.

## Hasil yang bisa dicek

- Setiap angka di *Results* bisa dilacak ke satu file di `results/`
- Setiap tool punya versi dan sitasi
- Tidak ada kalimat yang menyebut isolat "resisten" atau "rentan"

## Cek dirimu

1. Kalau punya akses lab, eksperimen apa yang akan kamu lakukan untuk menguji hasil *in-silico* ini?
2. Bagaimana hasilmu berkaitan dengan *One Health*, mengingat sumbernya hewan, pakan, dan lingkungan?
3. Keterbatasan mana yang paling memengaruhi kesimpulanmu?

## Templat log

```
### YYYY-MM-DD (Hari 9)
- **Langkah:** menulis draf laporan
- **Input:** results/*, figures/*, report/references.md
- **Parameter:** -
- **Hasil / file keluaran:** report/report.md (draf 1)
- **Kendala dan solusinya:**
- **Pertanyaan yang muncul:**
```

Sebelumnya: [Hari 8](hari-08-figur-dan-literatur.md) · Berikutnya: [Hari 10](hari-10-readme-github.md)
