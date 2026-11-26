# Rencana kerja

Diadaptasi dari jadwal 10 hari di PDF panduan (hlm. 11). Satu "hari" kira-kira 1 sampai 2 jam dan boleh dipecah per minggu sesuai `05-jadwal-mingguan.md`. Antrean Galaxy bisa membuat jadwal molor.

`panduan-pemula.md` memuat istilah, spesifikasi skrip, dan cara merumuskan klaim. Langkah rinci tiap hari ada di `harian/` (tujuan, prasyarat, daftar centang, hasil yang bisa dicek, pertanyaan *cek dirimu*, templat log untuk `analysis_notes.md`).

Setelah keluaran mentah Galaxy ada di `results/`, bagian lokalnya (kurasi, matriks, figur) dijalankan dengan `python run_all.py` dari folder proyek.

**Keputusan awal:** dataset utama memakai 9 isolat Kelompok A dari PRJNA1075840 (lihat `dataset_candidates.md`), tool AMR utama AMRFinderPlus di usegalaxy.eu, dan QC dengan QUAST di server yang sama. Laporan dan README ditulis dalam bahasa Inggris. Catatan kerja di `analysis_notes.md` ditulis dalam bahasa Indonesia.

| Hari | Kerjakan | Hasil yang bisa dicek |
|---|---|---|
| 1 | Baca bagian 1 sampai 3 PDF. Baca ulang `dataset_candidates.md` dan buka halaman BioProject-nya sendiri. Isi bagian "Aturan yang ditetapkan sebelum melihat hasil" di `analysis_notes.md` | Kriteria inklusi, aturan QC, dan aturan deteksi sudah tertulis |
| 2 | Buka tiap aksesi di NCBI, isi `metadata/genome_metadata.csv` dengan nilai persis dari BioSample, dan pakai `not reported` untuk kolom yang kosong | 9 baris metadata |
| 3 | Unduh FASTA genom (NCBI Datasets, tombol *Download*) ke `data/raw_genomes/`, lalu buat akun usegalaxy.eu dan unggah file-filenya | 9 dataset di *history* Galaxy |
| 4 | Jalankan QUAST pada kesembilan assembly sekaligus. Salin angkanya ke `results/assembly_quality.csv` dan terapkan aturan QC | Tabel QC dan keputusan inklusi |
| 5 | Jalankan AMRFinderPlus (input nukleotida, organisme *Escherichia*) dengan setelan yang sama untuk semua isolat. Unduh tabel mentahnya ke `results/raw_tool_outputs/` | 9 file TSV mentah dan versi database tercatat |
| 6 | Pelajari arti kolom *Method* di AMRFinderPlus (EXACTX, BLASTX, PARTIALX, POINTX, dan seterusnya). Pindahkan hit yang lolos aturan ke `results/amr_hits_curated.csv` | Tabel hit terkurasi |
| 7 | Buat matriks gen × isolat (1/0 plus kolom catatan) dengan skrip Python di `scripts/` (spesifikasinya di `panduan-pemula.md`), lalu simpan sebagai `results/amr_presence_absence.csv` | Matriks |
| 8 | Buat figur 1 (diagram batang jumlah gen per isolat) dan figur 2 (*heatmap*). Mulai cari 5 sampai 8 paper | 2 PNG di `figures/` dan daftar paper |
| 9 | Tulis draf laporan (*Methods* dan *Results* dulu, *Abstract* paling akhir) | Draf di `report/` |
| 10 | Rapikan README, buat repositori GitHub publik, dan unggah semua kecuali genom mentah | Tautan repositori |

## Opsional setelah inti selesai

| Hari | Kerjakan | Kaitannya dengan silabus |
|---|---|---|
| 11 | Pasang WSL dan Miniconda, buat *environment* `amr`, pasang AMRFinderPlus dari bioconda, lalu ulangi analisis satu isolat dan bandingkan hasilnya dengan keluaran Galaxy | `02`: baris perintah, conda, dan WSL |
| 12 | Buat ulang figur 2 dengan Python (pandas dan seaborn) di Jupyter, lalu simpan notebook-nya di repositori | `02`: Python dasar |
| 13+ | Pilih satu: Extension B (ABRicate dengan database CARD sebagai pembanding), Extension C (MLST), atau Extension A (plasmid) | Bahan diskusi saat wawancara iGEM |
