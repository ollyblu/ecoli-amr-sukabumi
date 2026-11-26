# Lembar kerja harian

Satu berkas untuk satu hari di `../plan.md`. Satu "hari" kira-kira 1 sampai 2 jam dan boleh dipecah jadi beberapa sesi. Buka berkas hari yang sedang kamu kerjakan saja; penjelasan panjang tiap istilah tetap ada di `../panduan-pemula.md`.

Kalau isi berkas di sini bertentangan dengan `../analysis_notes.md`, aturan di `analysis_notes.md` yang berlaku.

| Hari | Berkas | Hasil |
|---|---|---|
| 1 | [hari-01-aturan.md](hari-01-aturan.md) | Aturan inklusi, QC, dan deteksi tertulis lengkap |
| 2 | [hari-02-metadata.md](hari-02-metadata.md) | 9 baris di `genome_metadata.csv` |
| 3 | [hari-03-unduh-dan-galaxy.md](hari-03-unduh-dan-galaxy.md) | 9 FASTA di *history* Galaxy |
| 4 | [hari-04-quast.md](hari-04-quast.md) | `assembly_quality.csv` dan keputusan QC |
| 5 | [hari-05-amrfinderplus.md](hari-05-amrfinderplus.md) | 9 TSV mentah, versi tool dan database tercatat |
| 6 | [hari-06-kurasi-hit.md](hari-06-kurasi-hit.md) | `amr_hits_curated.csv` dari `curate_hits.py` |
| 7 | [hari-07-matriks.md](hari-07-matriks.md) | `amr_presence_absence.csv` dari `build_matrix.py` |
| 8 | [hari-08-figur-dan-literatur.md](hari-08-figur-dan-literatur.md) | 2 PNG di `figures/` dan 5 sampai 8 paper |
| 9 | [hari-09-laporan.md](hari-09-laporan.md) | Draf laporan di `report/` |
| 10 | [hari-10-readme-github.md](hari-10-readme-github.md) | Repositori GitHub publik |
| 11 | [hari-11-opsional-jalur-lokal.md](hari-11-opsional-jalur-lokal.md) | AMRFinderPlus lokal untuk satu isolat |
| 12 | [hari-12-opsional-notebook.md](hari-12-opsional-notebook.md) | Notebook Jupyter untuk figur 2 |
| 13+ | [hari-13-opsional-ekstensi.md](hari-13-opsional-ekstensi.md) | Satu ekstensi (B, C, atau A) |

Setiap berkas punya pola yang sama: tujuan, prasyarat, langkah berupa daftar centang, hasil yang bisa dicek, pertanyaan *cek dirimu*, dan templat log yang tinggal disalin ke `../analysis_notes.md`. Centang di berkas ini hanya alat bantu; centang resmi tetap di `05-jadwal-mingguan.md`.

Bagian lokal alur kerja (Hari 6 sampai 8) bisa dijalankan sekaligus dengan `python run_all.py` dari folder proyek.
