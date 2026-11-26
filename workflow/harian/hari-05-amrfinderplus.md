# Hari 5: AMRFinderPlus

## Tujuan

Sembilan TSV mentah tersimpan di `results/raw_tool_outputs/`, dan versi tool serta versi database tercatat.

## Prasyarat

- Keputusan QC Hari 4 sudah final. Isolat yang dikeluarkan boleh tetap dijalankan, tapi tandai di log bahwa hasilnya tidak masuk analisis utama.
- Ringkasan kategori *Method* dari Hari 1 sudah ada

## Langkah

- [x] Cari tool `AMRFinderPlus` di Galaxy dan catat versinya (per 18 November 2026 tercatat 4.2.7+galaxy0)
- [x] Input: FASTA nukleotida (genom)
- [x] Organisme: *Escherichia*
- [x] Opsi `--plus` **tidak** dinyalakan, karena gen virulensi dan *stress* di luar cakupan
- [x] Pilih kesembilan dataset; Galaxy membuat satu *job* per isolat dengan setelan yang sama
- [x] Sambil menunggu antrean, catat semua setelan formulir ke log
- [x] Unduh tiap tabel keluaran dan beri nama `SIDxx_amrfinder.tsv` (atau pola lain, asal konsisten)
- [x] Buka ikon "i" pada salah satu *job* untuk mencari versi database. Kalau tidak ada di sana, periksa keluaran log tool
- [x] Isi baris AMR di tabel *Versi tool dan database* di `analysis_notes.md`
- [x] Isi log
- [ ] Commit (`Add raw AMRFinderPlus outputs`): ditunda, folder belum jadi repositori git (Hari 10)

Centang per isolat (isi kolom pertama dengan `Sample_ID`-mu):

| Sample_ID | Job selesai | TSV diunduh |
|---|---|---|
| SID09 | [x] | [x] |
| SID10 | [x] | [x] |
| SID11 | [x] | [x] |
| SID12 | [x] | [x] |
| SID14 | [x] | [x] |
| SID16 | [x] | [x] |
| SID17 | [x] | [x] |
| SID19 | [x] | [x] |
| SID20 | [x] | [x] |

## Kalau macet

- Antrean usegalaxy.eu bisa berjam-jam. Tab boleh ditutup; *job* tetap berjalan.
- Kalau satu *job* gagal, jalankan ulang isolat itu saja dengan setelan yang sama, lalu catat di log.
- Jangan pindah server di tengah jalan, karena versi tool dan database bisa berbeda.

## Hasil yang bisa dicek

- 9 file TSV di `results/raw_tool_outputs/`, namanya mengikuti satu pola
- Versi tool dan versi database tertulis lengkap
- File TSV belum kamu ubah sama sekali. Ini data mentah

## Cek dirimu

1. Kenapa setelan harus sama untuk semua isolat?
2. Apa yang hilang kalau kamu tidak mencatat versi database?
3. Kenapa opsi organisme *Escherichia* perlu dipilih? Petunjuk: kaitkan dengan mutasi titik.

## Templat log

```
### YYYY-MM-DD (Hari 5)
- **Langkah:** deteksi gen AMR dengan AMRFinderPlus
- **Input:** 9 FASTA (lolos QC: <...>)
- **Parameter:** AMRFinderPlus <versi>, DB <versi>, input nukleotida, organisme Escherichia, tanpa --plus
- **Hasil / file keluaran:** results/raw_tool_outputs/SIDxx_amrfinder.tsv (9 file)
- **Kendala dan solusinya:**
- **Pertanyaan yang muncul:**
```

Sebelumnya: [Hari 4](hari-04-quast.md) · Berikutnya: [Hari 6](hari-06-kurasi-hit.md)
