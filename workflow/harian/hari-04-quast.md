# Hari 4: QUAST

## Tujuan

`results/assembly_quality.csv` terisi, dan keputusan inklusi tiap isolat tercatat sesuai aturan QC dari Hari 1.

## Prasyarat

- Aturan QC di `../analysis_notes.md` sudah punya sumber. Jangan mulai hari ini kalau TODO itu belum selesai.
- 9 dataset FASTA di Galaxy

## Langkah

- [x] Cari tool `QUAST` di panel Galaxy. Catat versinya (per 18 November 2026 tercatat 5.3.0+galaxy3)
- [x] Pilih kesembilan dataset sekaligus sebagai input. Tanpa genom rujukan; setelan lain bawaan
- [x] Temuan Hari 3: tiap file berupa satu *scaffold* dengan celah N. Dengan setelan bawaan, QUAST akan melaporkan 1 *contig* per isolat. Cari opsi pemecah *scaffold* di formulir (di QUAST baris perintah namanya `--split-scaffolds`; label di Galaxy perlu kamu periksa sendiri). Kalau ada, aktifkan supaya QUAST juga melaporkan statistik per *contig* hasil pecahan (*broken*). Catat pilihanmu di log
- [x] Sebelum melihat angka, putuskan dan tulis di log: apakah aturan *Total length* memakai panjang dengan N (baris *Total length* bawaan QUAST) atau tanpa N. Aturan QC di `analysis_notes.md` belum menyebutnya
- [x] Catat setelan yang terlihat di formulir tool ke log
- [x] Jalankan, lalu buka laporan tabularnya (TSV)
- [x] Putuskan versi jumlah *contig* yang dipakai (semua *contig* atau hanya yang ≥ 500 bp). Tulis pilihanmu di log dan pakai untuk semua isolat
- [x] Salin ke CSV: `Sample_ID, Total_length_bp, Contigs, N50_bp, GC_pct, Notes`
- [x] Terapkan aturan QC. Isolat di luar rentang ditulis di `Notes` beserta nilainya
- [x] Isi baris QC di tabel *Versi tool dan database* di `analysis_notes.md`
- [x] Simpan laporan tabular QUAST sebagai `results/raw_tool_outputs/quast_report.tsv`
- [x] Isi log
- [ ] Commit (`Add QUAST results and QC decisions`): ditunda, folder ini belum jadi repositori git (repo dibuat Hari 10)

## Cara membaca angka QUAST

| Baris | Yang kamu periksa |
|---|---|
| *Total length* | Dikeluarkan bila < 4,1 atau > 6,3 Mb; catat WARN bila 4,1 sampai 4,4 atau 5,7 sampai 6,3 Mb (QC.watch) |
| *GC (%)* | Dikeluarkan bila < 50,09 atau > 51,13%; catat WARN bila 50,09 sampai 50,25 atau 50,88 sampai 51,13% (QC.watch) |
| *# contigs* | Dilaporkan saja, bukan batas QC |
| *N50* | Dilaporkan saja; makin besar, makin utuh |
| *# N's per 100 kbp* | Celah di dalam assembly. Catat kalau ada yang menonjol |

## Hasil yang bisa dicek

- 9 baris di `assembly_quality.csv`
- Tiap isolat punya keputusan jelas: masuk analisis utama atau dikeluarkan, dengan alasan
- Versi QUAST tercatat

## Cek dirimu

1. Satu isolat punya 52 *contig* dan isolat lain 37. Apakah yang pertama "lebih buruk"? Apa yang bisa dan tidak bisa kamu simpulkan?
2. Kenapa panjang total yang jauh di atas 6,3 Mb (batas FAIL QC.watch) mencurigakan?
3. Kalau satu isolat meleset tipis dari rentang GC, apa yang kamu lakukan? Jawabannya ada di aturanmu, bukan di perasaanmu saat melihat angka.

## Templat log

```
### YYYY-MM-DD (Hari 4)
- **Langkah:** QC assembly dengan QUAST
- **Input:** 9 FASTA di history ecoli-sukabumi-amr
- **Parameter:** QUAST <versi>, tanpa rujukan, setelan: <...>; jumlah contig yang dipakai: <...>
- **Hasil / file keluaran:** results/assembly_quality.csv; results/raw_tool_outputs/quast_report.tsv; isolat dikeluarkan: <tidak ada / ...>
- **Kendala dan solusinya:**
- **Pertanyaan yang muncul:**
```

Sebelumnya: [Hari 3](hari-03-unduh-dan-galaxy.md) · Berikutnya: [Hari 5](hari-05-amrfinderplus.md)
