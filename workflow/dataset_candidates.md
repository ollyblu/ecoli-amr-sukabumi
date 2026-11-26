# Kandidat dataset

Ditelusuri 18 November 2026 lewat NCBI E-utilities (`db=bioproject`, `db=sra`) dan NCBI Datasets API. Isi NCBI bisa berubah, jadi buka sendiri setiap tautan dan cek ulang sebelum memutuskan.

Kata kunci yang dipakai: `Escherichia coli[Organism] AND Indonesia`, dan `Escherichia coli[Organism] AND (chicken OR poultry OR broiler OR pig OR livestock) AND (Vietnam OR Thailand OR Malaysia OR Philippines OR Cambodia)`.

## Perbandingan

| BioProject | Isi | Assembly publik | Cocok untuk jalur Galaxy? |
|---|---|---|---|
| PRJNA1075840 (dipilih) | *E. coli* dari peternakan di Kota Sukabumi, Jawa Barat, plus beberapa isolat dari Sekolah Vokasi IPB | 13 assembly unik. NCBI menampilkan 18 baris karena sebagian muncul ganda sebagai GCA dan GCF | Ya. Assembly sudah jadi, tinggal diunduh |
| PRJNA1272294 | *E. coli* dari usap kloaka bebek, Thailand | 8 assembly berlevel *Contig* | Ya, sebagai cadangan. Kekurangannya: di luar Indonesia dan inangnya cuma satu jenis |
| PRJDB18129 | *E. coli* penghasil ESBL/AmpC dari ayam dan relawan sehat | Tidak ada assembly. Ada 204 SRA run (*reads* mentah) | Tidak untuk tahap awal. *Reads*-nya harus dirakit dulu (*de novo assembly*); ini cocok jadi proyek kedua |
| PRJDB18396 | ESBL *E. coli*, proyek Tricycle Indonesia | Tidak ada assembly. Ada 266 SRA run | Sama seperti PRJDB18129 |
| PRJNA1482025 | *E. coli* resisten dari peternakan babi di Banten | Belum ada assembly maupun SRA run per 18 November 2026 | Pantau, mungkin datanya dirilis nanti |

Tautan: https://www.ncbi.nlm.nih.gov/bioproject/PRJNA1075840

## Rincian PRJNA1075840

Pakai aksesi GCA (GenBank). GCF adalah salinan RefSeq dari genom yang sama, jadi jangan dihitung dua kali.

**Kelompok A: peternakan di Sukabumi** (9 isolat, level *Chromosome*, 37 sampai 52 *contig*, dikoleksi Agustus sampai September 2023)

| Aksesi | Isolat | Host atau sumber (sesuai BioSample) |
|---|---|---|
| GCA_037201825.1 | 16 | *Capra aegagrus hircus* (kambing) |
| GCA_037201885.1 | 17 | *Bos taurus* (sapi) |
| GCA_037201895.1 | 11 | *Anas platyrhynchos javanica* (itik) |
| GCA_037201835.1 | 9 | *Anas platyrhynchos javanica* (itik) |
| GCA_037201905.1 | 10 | *Cygnus cygnus* |
| GCA_037201845.1 | 19 | Pakan itik |
| GCA_037201855.1 | 14 | Pakan ayam petelur |
| GCA_037201875.1 | 12 | Lingkungan |
| GCA_037201865.1 | 20 | Lingkungan |

**Kelompok B: Sekolah Vokasi IPB** (4 isolat, level *Complete Genome*, 1 *contig* per isolat, dikoleksi Februari sampai April 2024)

| Aksesi | Isolat | Sumber |
|---|---|---|
| GCA_044648255.1 | BS-04 | Feses broiler, minggu ke-4 |
| GCA_044647575.1 | BS-01 | Feses broiler, hari menetas atau minggu ke-1 |
| GCA_044647535.1 | HS-01 | Feses pekerja |
| GCA_044647545.1 | HS-02 | Feses pekerja |

Label sumber di atas disalin dari BioSample. Catat persis seperti di NCBI saat mengisi `metadata/genome_metadata.csv`, dan jangan menambah informasi yang tidak tercantum.

## Saran pilihan

- **Dataset utama: 9 isolat Kelompok A.** Lokasi, periode, dan level assembly-nya seragam, dan jumlahnya pas dengan target 8 sampai 10 di panduan. Variasi sumbernya (hewan, pakan, lingkungan) memberi sudut *One Health* untuk bagian diskusi.
- **Kelompok B dipisah.** Lokasi, tahun, dan level assembly-nya berbeda. Kalau tetap mau dipakai, perlakukan sebagai analisis tambahan dan sebutkan perbedaannya di bagian keterbatasan. Isolat pekerja adalah data manusia, jadi pakai hanya label yang tercantum di NCBI.
- **Paper sumber belum ketemu** lewat PubMed per 18 November 2026. Cari sendiri dengan kata kunci `Escherichia coli Sukabumi farm whole genome` di PubMed dan Google Scholar, lalu cek halaman BioProject untuk tautan publikasi. Tanpa paper biasanya tidak ada data fenotipe (AST), sehingga Extension D di panduan kemungkinan tidak bisa dikerjakan.
- **Angka 37 sampai 52 *contig* di level *Chromosome*:** setelah diunduh, tiap assembly ternyata satu *scaffold* kromosom dengan celah N dan tanpa sekuens plasmid (`analysis_notes.md`, Hari 3). Ekstensi plasmid (Extension A) tidak bisa dikerjakan dari assembly ini.
