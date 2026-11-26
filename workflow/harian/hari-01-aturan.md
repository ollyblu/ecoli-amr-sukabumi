# Hari 1: menetapkan aturan sebelum melihat data

**Status per 18 November 2026:** kriteria inklusi, aturan QC, dan aturan deteksi sudah tertulis di `../analysis_notes.md`. Tinggal dua TODO dan tiga pertanyaan.

## Tujuan

Semua aturan analisis tertulis lengkap sebelum kamu menjalankan QUAST atau AMRFinderPlus. Aturan yang ditulis setelah melihat hasil cenderung ikut menyesuaikan diri dengan hasil yang "menarik".

## Prasyarat

- PDF panduan bagian 1 sampai 3 sudah dibaca
- `../dataset_candidates.md` sudah dibaca, dan halaman https://www.ncbi.nlm.nih.gov/bioproject/PRJNA1075840 sudah kamu buka sendiri

## Langkah

- [x] Tulis kriteria inklusi dataset
- [x] Tulis aturan QC (awalnya 4,5 sampai 5,9 Mb dan GC 49,5 sampai 51,5%; pada 25 November diganti ke batas FAIL QC.watch, 4,1 sampai 6,3 Mb dan GC 50,09 sampai 51,13%)
- [x] Tulis aturan deteksi AMR
- [x] **TODO sumber rentang QC.** Buka statistik spesies *E. coli* di NCBI Datasets (https://www.ncbi.nlm.nih.gov/datasets/genome/?taxon=562) atau satu paper yang melaporkan ukuran dan GC genom *E. coli*. Tulis sumbernya dan tanggal kamu membukanya di bagian aturan QC. Kalau angkanya berbeda, ubah rentangnya hari ini, bukan setelah QUAST.
- [x] **TODO kategori *Method*.** Buka https://github.com/ncbi/amr/wiki, cari halaman tentang *output* atau *interpreting results*. Tulis dengan kata-katamu sendiri arti EXACTX, ALLELEX, BLASTX, PARTIALX, PARTIAL_CONTIG_ENDX, INTERNAL_STOPX, HMM, dan POINTX di bawah judul *Ringkasan arti kategori Method*.
- [x] Jawab tiga pertanyaan di bagian aturan, 2 sampai 3 kalimat per pertanyaan
- [ ] Isi log harian (sudah, 25 November), lalu commit (`Finalize analysis rules before running tools`)

Petunjuk untuk TODO kedua: akhiran X berarti pencarian dilakukan pada terjemahan protein, akhiran N pada nukleotida. Perhatikan beda antara "cocok 100% dengan rujukan", "mirip tapi utuh", dan "terpotong di ujung *contig*".

## Hasil yang bisa dicek

- Bagian aturan QC punya rujukan dengan nama sumber dan tanggal akses
- Delapan kategori *Method* punya penjelasan masing-masing satu sampai dua kalimat
- Tiga pertanyaan terjawab

## Cek dirimu

1. Kenapa PARTIAL_CONTIG_ENDX tidak dihitung 1 padahal gennya mungkin benar-benar ada?
2. Apa bedanya mutasi *gyrA* dengan gen *bla*CTX-M kalau dilihat dari cara penularannya antarbakteri?
3. Kalau sumber yang kamu temukan menyebut rentang GC 50,0 sampai 51,0%, apa yang kamu lakukan dengan aturanmu, dan kenapa harus sekarang?

## Templat log

```
### YYYY-MM-DD (Hari 1, lanjutan)
- **Langkah:** melengkapi sumber rentang QC dan ringkasan kategori Method
- **Input:** <URL sumber QC, tanggal akses>; https://github.com/ncbi/amr/wiki
- **Parameter:** -
- **Hasil / file keluaran:** analysis_notes.md bagian aturan lengkap
- **Kendala dan solusinya:**
- **Pertanyaan yang muncul:**
```

Berikutnya: [Hari 2](hari-02-metadata.md)
