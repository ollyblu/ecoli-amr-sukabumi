# Hari 7: matriks gen × isolat

## Tujuan

`results/amr_presence_absence.csv` dibuat oleh `scripts/build_matrix.py` dari tabel terkurasi Hari 6.

## Prasyarat

- `results/amr_hits_curated.csv` sudah lolos uji hitungan manual

## Langkah

- [x] Tulis `scripts/build_matrix.py` dengan spesifikasi berikut:
  - Baris = gen atau mutasi, kolom = isolat yang lolos QC, urut sesuai `Sample_ID`
  - Isi 1 kalau ada setidaknya satu hit `counted`, 0 kalau tidak ada hit sama sekali
  - Hit `note` tidak dijadikan 1 atau 0. Tampung di kolom `Notes`, misalnya `SID09: PARTIAL_CONTIG_ENDX`
  - Tambahkan kolom `Feature_type` berisi `acquired` atau `point_mutation`, diambil dari subtipe
  - Tambahkan kolom golongan antibiotik untuk mengelompokkan baris di figur
- [x] Tentukan cara menulis sel untuk gen yang hanya punya hit `note` pada satu isolat. Pilihan yang jujur: biarkan kosong (`NA`), bukan 0. Tulis keputusanmu di log
- [x] Simpan ke `results/amr_presence_absence.csv`
- [x] Uji silang: jumlah angka 1 per isolat di matriks harus sama dengan jumlah fitur unik `counted` per isolat di tabel terkurasi
- [x] Periksa dengan mata: pilih dua gen dan pastikan polanya cocok dengan TSV mentah
- [x] Isi log (commit ditunda ke Hari 10: folder belum jadi repo git)

## Hasil yang bisa dicek

- Matriks terbaca dengan pandas, tanpa baris ganda
- Mutasi titik dan gen *acquired* bisa dipisah lewat `Feature_type`
- Uji silang jumlah lolos

## Cek dirimu

1. Apa arti 0 di matriksmu, dan apa yang **tidak** boleh disimpulkan dari angka itu?
2. Kenapa sel dengan hit `note` lebih jujur ditulis `NA` daripada 0?
3. Gen yang terdeteksi di dua *contig* pada satu isolat tetap ditulis 1. Informasi apa yang hilang, dan di mana kamu menyimpannya?

## Templat log

```
### YYYY-MM-DD (Hari 7)
- **Langkah:** membangun matriks presence/absence
- **Input:** results/amr_hits_curated.csv
- **Parameter:** sel note = <NA/...>; isolat yang dimasukkan: <...>
- **Hasil / file keluaran:** results/amr_presence_absence.csv (<n> fitur × <n> isolat)
- **Kendala dan solusinya:**
- **Pertanyaan yang muncul:**
```

Sebelumnya: [Hari 6](hari-06-kurasi-hit.md) · Berikutnya: [Hari 8](hari-08-figur-dan-literatur.md)
