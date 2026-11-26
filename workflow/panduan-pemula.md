# Panduan: proyek gen AMR *E. coli* Sukabumi

Panduan ini memuat istilah, spesifikasi skrip, dan cara merumuskan klaim. Langkah per hari ada di `harian/`, jadwalnya di `plan.md`, dan aturan analisis di `analysis_notes.md`. Kalau ketiganya bertentangan, `analysis_notes.md` yang berlaku, karena aturan di sana ditulis sebelum hasil terlihat.

Semua angka contoh di panduan ini fiktif. Jangan menyalinnya ke berkas hasil.

## 1. Gambaran besar

Pertanyaan proyek: gen resistansi antibiotik (*antimicrobial resistance*, AMR) apa yang terdeteksi pada 9 genom *E. coli* dari peternakan di Sukabumi (BioProject PRJNA1075840), dan bagaimana profilnya berbeda antarisolat. Datanya sudah ada di NCBI, jadi tidak perlu laboratorium. Alurnya:

```
NCBI (aksesi GCA) -> FASTA -> Galaxy: QUAST (mutu assembly), AMRFinderPlus (gen AMR)
  -> TSV mentah -> curate_hits.py -> build_matrix.py -> plot_figures.py -> laporan -> GitHub
```

Dari TSV mentah sampai figur, satu perintah menjalankan semuanya: `python run_all.py`.

## 2. Kamus mini

| Istilah | Arti di proyek ini |
|---|---|
| *Reads* | Potongan pendek hasil mesin sekuensing. Proyek ini tidak memakainya |
| *Assembly* | Hasil menyusun *reads* menjadi urutan panjang. Proyek ini mulai dari *assembly* yang sudah jadi |
| *Contig* | Satu potongan sambung dalam *assembly*. *Scaffold* menyambung beberapa *contig* dengan celah N |
| N50 | Panjang *contig* yang, bersama *contig* yang lebih panjang, mencakup separuh total genom. Makin besar, makin utuh |
| Kadar GC | Persentase basa G dan C. *E. coli* sekitar 50%; nilai yang meleset jauh bisa menandakan DNA spesies lain |
| FASTA | Format teks untuk urutan; baris berawalan `>` adalah nama urutan |
| BioProject, BioSample | Wadah satu studi di NCBI, dan keterangan satu sampel (inang, lokasi, tanggal) |
| GCA dan GCF | Aksesi genom yang sama: GCA dari GenBank (kiriman peneliti), GCF salinan kurasi RefSeq. Proyek ini memakai GCA |
| Gen AMR *acquired* | Gen yang didapat dari luar, biasanya lewat plasmid atau transposon (*bla*TEM, *tet*(A)) |
| Mutasi titik *chromosomal* | Perubahan pada gen yang dimiliki semua *E. coli*, misalnya *gyrA* S83L. Yang dicari mutasinya, bukan gennya |
| *Identity*, *coverage* | Kemiripan urutan isolat dengan rujukan, dan persentase panjang gen rujukan yang tertutup |

Terdeteksinya gen AMR tidak membuktikan resistansi, dan tidak terdeteksi tidak berarti peka. Resistansi diukur lewat uji kepekaan antibiotik (*antimicrobial susceptibility testing*, AST). Proyek ini memeriksa genotipe, bukan fenotipe, dan kalimat di laporan harus mencerminkan batas itu.

## 3. Persiapan

- Akun https://usegalaxy.eu. Pakai satu server dari awal sampai akhir supaya versi tool konsisten.
- Python 3.11 dengan paket di `requirements.txt`; Git dan akun GitHub.
- Opsional: WSL dan Miniconda untuk jalur lokal (`harian/hari-11-opsional-jalur-lokal.md`).
- Tampilan NCBI dan Galaxy bisa berubah. Kalau tombol yang disebut tidak ada, cari fungsi yang setara dan catat bedanya di log.

Setiap sesi kerja diakhiri dengan mengisi log di `analysis_notes.md` (langkah, input, parameter, hasil, kendala) dan satu *commit*. Log ini yang membuat analisis bisa diulang orang lain.

## 4. Spesifikasi skrip

Tiga skrip di `scripts/`, dijalankan berurutan oleh `run_all.py`. Masing-masing menulis ke folder `results/` atau `figures/` dan berhenti dengan pesan galat kalau masukannya tidak cocok.

**`curate_hits.py`**
- Masukan: semua TSV di `results/raw_tool_outputs/`. `Sample_ID` diambil dari nama berkas dan dicocokkan dengan `metadata/genome_metadata.csv`; skrip berhenti kalau ada yang tidak cocok.
- Hanya baris bertipe AMR. *Method* dipetakan ke `Detection_category`: kategori yang dihitung 1 menurut aturan (`EXACTX`, `ALLELEX`, `BLASTX`, `POINTX`) jadi `counted`, sisanya `note`. Kategori yang tidak dikenal jatuh ke `note` dengan peringatan.
- Keluaran: `results/amr_hits_curated.csv` dengan header `Sample_ID, Feature, Drug_class_or_mechanism, Detection_category, Pct_identity, Pct_coverage, Tool, Tool_version, DB_version, Notes`.

**`build_matrix.py`**
- Dari tabel terkurasi, matriks gen × isolat berisi 1 (`counted`), 0 (tidak ada hit), atau NA (hanya ada hit `note`, alasannya di kolom catatan). Isolat di kolom, urut `Sample_ID`.
- Kolom penanda memisahkan gen *acquired* dari mutasi titik, dan `POINT` dari `POINT_DISRUPT` (frameshift atau stop prematur).
- Keluaran: `results/amr_presence_absence.csv`.

**`plot_figures.py`**
- Figur 1: batang jumlah fitur AMR per isolat, dipisah menurut jenisnya. Figur 2: *heatmap* matriks, baris dikelompokkan per golongan antibiotik, kolom diberi sumber isolat (hewan, pakan, lingkungan) dari pemetaan eksplisit di skrip.
- Keluaran: `figures/fig1_amr_count_per_isolate.png`, `figures/fig2_amr_heatmap.png`.

**Jebakan**
- Gen yang sama di dua *contig* pada satu isolat menghasilkan dua baris. Di matriks tetap 1, kejadiannya dicatat, karena bisa berarti dua salinan atau satu gen yang terbelah.
- Nama mutasi seperti `gyrA_S83L` tidak boleh dipotong jadi `gyrA`.
- Galaxy kadang menempelkan nama dataset ke nama berkas unduhan (`Galaxy12-[AMRFinderPlus on SID09].tabular`). Pola pengambilan `Sample_ID` harus diuji pada kesembilan nama.

**Uji kecil:** hitung satu isolat dengan tangan (berapa baris AMR, berapa yang dihitung 1, berapa yang jadi catatan), lalu bandingkan dengan keluaran skrip. Kalau beda, cari sebabnya sebelum lanjut.

## 5. Merumuskan klaim

| Terlalu jauh | Sesuai data |
|---|---|
| "Isolate SID09 is resistant to tetracycline." | "*tet*(A) was detected in SID09." |
| "Environmental isolates carry fewer resistance genes." | "Under the chosen thresholds, fewer acquired AMR genes were detected in the two environmental isolates (n = 2)." |
| "The isolate lacks beta-lactam resistance." | "No acquired beta-lactamase gene was detected with AMRFinderPlus (database version ...)." |

Dengan 9 isolat, uji statistik tidak informatif. Deskripsi yang jujur lebih kuat daripada nilai p dari n = 2.

## 6. Bekal wawancara iGEM

Proyek ini memperbesar peluang kalau kamu bisa menjelaskannya dengan bahasamu sendiri; tidak ada proyek yang menjamin lolos seleksi. Latih jawaban satu sampai dua menit untuk pertanyaan berikut:

1. Ceritakan proyekmu dalam tiga kalimat untuk orang yang bukan biolog.
2. Kenapa memilih dataset ini, dan kenapa Kelompok B tidak dipakai?
3. Apa beda *reads* dan *assembly*, dan kenapa mulai dari *assembly*?
4. Apa yang diukur QUAST, dan apa batas QC-mu?
5. Kenapa aturan deteksi ditulis sebelum melihat hasil?
6. Apa arti angka 0 di matriks?
7. Kenapa gen *acquired* dan mutasi titik dipisah di figur?
8. Kalau punya akses lab, eksperimen apa yang menguji hasil *in-silico* ini?
9. Bagaimana hasil ini berkaitan dengan *One Health*?
10. Kalau diulang, apa yang akan kamu ubah?
