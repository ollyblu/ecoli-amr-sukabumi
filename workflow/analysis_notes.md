# Catatan analisis

Catatan kerja harian proyek AMR *E. coli*. Tujuannya supaya orang lain (dan kamu sendiri tiga bulan lagi) bisa mengulang setiap langkah. Tulis apa adanya, termasuk yang gagal.

## Aturan yang ditetapkan sebelum melihat hasil

Isi bagian ini **sebelum** menjalankan QUAST dan tool AMR. Kalau aturannya baru kamu tulis setelah melihat hasil, pilihanmu bisa tanpa sadar mengikuti hasil yang "menarik".

Ditetapkan 18 November 2026, sebelum data diunduh.

**Kriteria inklusi dataset**
- [x] Organisme tercatat *Escherichia coli* di NCBI
- [x] Semua genom berasal dari satu BioProject: PRJNA1075840
- [x] Hanya isolat yang `geo_loc_name`-nya "Indonesia: Livestock farm in Sukabumi city" (Kelompok A di `dataset_candidates.md`), dengan sumber hewan, pakan, dan lingkungan
- [x] Level assembly yang diterima: *Chromosome*, sesuai level semua isolat Kelompok A
- [x] Jumlah genom: 9, semua isolat Kelompok A tanpa subsampel
- [x] Aksesi yang dipakai GCA (GenBank). Salinan GCF tidak dihitung lagi
- [x] Kelompok B (4 isolat Sekolah Vokasi IPB) dikeluarkan dari analisis utama karena lokasi, tahun, dan level assembly-nya berbeda. Kelompok ini disebut di bagian keterbatasan dan bisa jadi analisis tambahan

**Aturan QC** (diperbarui 25 November 2026, sebelum QUAST dijalankan). Assembly dikeluarkan dari analisis utama bila salah satu syarat berikut terpenuhi (batas *FAIL* QC.watch):
- total panjang < 4.100.000 bp atau > 6.300.000 bp, atau
- GC < 50,09% atau > 51,13%.

Assembly yang lolos tetapi masuk pita *WARN* (panjang 4,1 sampai 4,4 Mb atau 5,7 sampai 6,3 Mb; GC 50,09 sampai 50,25% atau 50,88 sampai 51,13%) tetap dianalisis, dan statusnya dicatat di kolom `Notes` pada `results/assembly_quality.csv`.

Alasannya, nilai di luar rentang itu bisa menandakan kontaminasi atau assembly yang tidak lengkap. Jumlah *contig* dan N50 hanya dilaporkan, tidak dijadikan batas, karena kesembilan isolat punya level assembly yang sama (37 sampai 52 *contig*).

- [x] **Sumber rentang QC:** QC.watch, skema `qualibact-v1.0` untuk *Escherichia coli*, https://www.qc.watch/Escherichia/Escherichia_coli/ (diakses 25 November 2026). Ambang diturunkan dari 376.660 genom (5.033 di antaranya rujukan RefSeq). Statistik dari 371.627 genom non-RefSeq: median panjang 5.108.717 bp (Q1 sampai Q3: 4.824.002 sampai 5.334.353), median GC 50,59% (Q1 sampai Q3: 50,47 sampai 50,72). Situs dikembangkan Centre for Genomic Pathogen Surveillance dan Big Data Institute. Sitasi yang diminta situs: Alikhan, NF. *Species specific quality control of bacterial de novo genome assemblies using QC.watch*. https://gitlab.com/cgps/tools/qualibact. Halaman spesies menandai *engine quality flag: warn* untuk dataset rujukan *E. coli*; ini disebut di bagian keterbatasan.
- Perubahan dari rentang awal (18 November: 4,5 sampai 5,9 Mb; GC 49,5 sampai 51,5%): rentang awal hanya perkiraan tanpa sumber. Batas GC awal ternyata jauh lebih longgar daripada distribusi nyata (SD 0,17%), jadi diganti dengan angka bersumber. Diubah sebelum QUAST dijalankan.

Kalau ada assembly yang dikeluarkan, catat aksesinya, nilainya, dan alasannya di log harian.

**Aturan deteksi AMR (AMRFinderPlus, input nukleotida, organisme *Escherichia*, tanpa `--plus`)**
- Dihitung **1**: *Method* `EXACTX`, `ALLELEX`, `BLASTX`, dan `POINTX` (mutasi titik pada gen *chromosomal*).
- Masuk **kolom catatan** dan tidak dipaksa jadi 1 atau 0: `PARTIALX`, `PARTIAL_CONTIG_ENDX`, `INTERNAL_STOPX`, `HMM`, dan kategori lain yang tidak ada di daftar ini.
- Hanya baris dengan *Element type* = AMR yang dianalisis. Gen virulensi dan gen *stress* (logam, biosida) tidak termasuk.
- Mutasi titik dan gen didapat (*acquired*) disajikan terpisah di figur. Keduanya mekanisme yang berbeda, dan gen *chromosomal* seperti *gyrA* ada di semua *E. coli*.
- [x] **Arti kategori *Method*** dicocokkan dengan dokumentasi resmi: https://github.com/ncbi/amr/wiki/Interpreting-results, bagian *The Method column* (diakses 25 November 2026).

*Ringkasan arti kategori Method:*

Akhiran X berarti hit ditemukan dengan menerjemahkan sekuens nukleotida (*contig*) ke protein lalu membandingkannya dengan protein rujukan. Akhiran P berarti input-nya sudah berupa protein, dan N berarti perbandingan langsung pada nukleotida (dipakai untuk mutasi non-koding seperti 16S atau promoter).

- **EXACTX:** protein hasil terjemahan identik 100% dengan protein rujukan di database, sepanjang penuh. Keluarga gennya tidak punya sistem penomoran alel.
- **ALLELEX:** sama-sama identik 100% sepanjang penuh, tetapi keluarga gennya punya penomoran alel (misalnya *bla*CTX-M-15), jadi alel spesifiknya bisa disebut.
- **BLASTX:** mirip tapi tidak identik (identitas di bawah 100%, ambang bawaan 90% kecuali dikurasi lain) dengan cakupan lebih dari 90% panjang protein rujukan. Gennya utuh, tetapi bisa varian yang belum tercatat.
- **PARTIALX:** cakupan hanya 50 sampai 90% panjang protein rujukan, dan potongan itu berada di tengah *contig*. Gennya benar-benar terpotong di assembly ini, bukan karena terputus di ujung *contig*.
- **PARTIAL_CONTIG_ENDX:** cakupan di bawah 90%, tetapi keselarasannya berhenti dalam jarak dua nukleotida dari ujung *contig* dengan arah yang membuat sisa gen "keluar" dari *contig*. Gen ini sering sebenarnya utuh di genom, hanya terbelah oleh *assembler* ke dua *contig*.
- **INTERNAL_STOPX:** saat diterjemahkan, ada kodon stop sebelum ujung protein rujukan. Proteinnya kemungkinan tidak berfungsi; bisa juga akibat *frameshift* atau galat *sequencing*.
- **HMM:** tidak memenuhi syarat BLAST, tetapi cocok dengan profil HMM keluarga gen di atas ambang yang dikurasi. Biasanya kerabat jauh dari keluarga gen yang dikenal, jadi kandidat, bukan temuan pasti.
- **POINTX:** mutasi titik yang sudah dilaporkan di literatur menyebabkan resistansi, ditemukan pada gen *chromosomal* lewat pencarian protein terjemahan. Hanya aktif bila opsi `--organism` diisi, dan hanya mutasi yang sudah dikurasi yang dilaporkan. Tidak adanya hit POINTX tidak berarti tidak ada mutasi fungsional.

## Ketersediaan tool di Galaxy

Dicek lewat API Galaxy pada 18 November 2026. Versi bisa berganti, jadi cek ulang di panel tool saat menjalankan, lalu tulis versi yang benar-benar kamu pakai di tabel berikutnya.

| Tool | usegalaxy.eu | usegalaxy.org | Kegunaan |
|---|---|---|---|
| QUAST | 5.3.0+galaxy3 | 5.3.0+galaxy3 | Statistik assembly |
| AMRFinderPlus | 4.2.7+galaxy0 | 4.2.7+galaxy0 | Tool AMR utama yang disarankan; punya opsi organisme *Escherichia* |
| ABRicate | 1.4.0+galaxy1 | 1.4.0+galaxy1 | Pembanding (Extension B); bisa memakai database CARD, ResFinder, atau NCBI |
| staramr | 0.12.3+galaxy0 | 0.12.3+galaxy0 | Alternatif pembanding berbasis ResFinder dan PointFinder |
| MLST | 2.35.0+galaxy0 | 2.35.0+galaxy0 | *Sequence typing* (Extension C) |

Saran: pakai satu server saja dari awal sampai akhir (misalnya usegalaxy.eu) supaya versinya konsisten.

## Versi tool dan database

| Langkah | Tool | Versi | Database | Platform | Tanggal jalan |
|---|---|---|---|---|---|
| QC | QUAST | 5.3.0+galaxy3 | – | usegalaxy.eu | 2026-11-25 |
| AMR | AMRFinderPlus | 4.2.7+galaxy0 (binari 4.2.7) | V4.2-2026-05-15.1 (`amrfinderplus_V4.2_2026-05-15.1`) | usegalaxy.eu | 2026-11-25 |

## Log harian

### 2026-11-18 (Hari 1)
- **Langkah:** menetapkan kriteria inklusi, aturan QC, dan aturan deteksi AMR
- **Input:** `dataset_candidates.md` dan PDF panduan bagian 1 sampai 3
- **Hasil:** 9 isolat Kelompok A dari PRJNA1075840; aturan tertulis di bagian atas
- **Belum selesai:** sumber untuk rentang QC; ringkasan kategori *Method* AMRFinderPlus; jawaban 3 pertanyaan di atas
- **Pertanyaan yang muncul:**

### 2026-11-25 (Hari 1, lanjutan)
- **Langkah:** melengkapi sumber rentang QC dan ringkasan kategori *Method*; menjawab tiga pertanyaan aturan
- **Input:** https://www.qc.watch/Escherichia/Escherichia_coli/ (skema qualibact-v1.0, diakses 25 November 2026); https://github.com/ncbi/amr/wiki/Interpreting-results (diakses 25 November 2026)
- **Parameter:** -
- **Hasil / file keluaran:** bagian aturan di `analysis_notes.md` lengkap. Rentang QC diganti dari perkiraan awal (4,5 sampai 5,9 Mb; GC 49,5 sampai 51,5%) ke batas FAIL QC.watch (4,1 sampai 6,3 Mb; GC 50,09 sampai 51,13%), dengan pita WARN dicatat di kolom `Notes`. Diubah sebelum QUAST dijalankan. `harian/hari-04-quast.md` ikut disesuaikan.
- **Kendala dan solusinya:** rujukan yang disarankan lembar kerja (NCBI Datasets) tidak dipakai. QC.watch dipilih karena memberi ambang eksplisit yang diturunkan dari ratusan ribu genom, bukan sekadar statistik deskriptif. Halaman spesies menandai *engine quality flag: warn*, jadi ini dicatat sebagai keterbatasan.
- **Pertanyaan yang muncul:** apakah pita WARN perlu memengaruhi interpretasi hasil AMR? Misalnya, apakah GC di pita WARN bisa jadi tanda kontaminasi plasmid atau spesies lain. Dijawab setelah melihat QUAST di Hari 4, tanpa mengubah aturan eksklusi.

### 2026-11-25 (Hari 2)
- **Langkah:** mengisi metadata dari halaman genom dan BioSample NCBI
- **Input:** 9 aksesi GCA Kelompok A (PRJNA1075840); BioSample SAMN39925913 sampai SAMN39925924
- **Parameter:** skema `Sample_ID` = `SID` + nomor isolat dua digit (`SID09`, `SID10`, ..., `SID20`). Diisi di `metadata/genome_metadata.xlsx` (semua sel berformat teks), lalu diekspor ke CSV dengan `pandas.read_excel(..., dtype=str).to_csv(..., index=False)`. Tidak memakai Save As CSV dari Excel karena *locale* `id-ID` memakai pemisah `;`.
- **Hasil / file keluaran:** `metadata/genome_metadata.csv` (9 baris data, 12 kolom, tanpa sel kosong; isi identik dengan XLSX). Kesembilan baris dicocokkan dengan catatan BioSample (E-utilities) dan laporan *assembly* (NCBI Datasets).
- **Kendala dan solusinya:**
  - Isian pertama salah mengambil kolom: `/collected by` (nama pengumpul) masuk ke `Collection_source`, tanggal rilis *assembly* (2024-03-17) masuk ke `Collection_date` untuk dua isolat, dan nama strain rujukan ANI (SE11, SMS-3-5) masuk ke `Organism`. Diperbaiki dengan mengambil semua kolom, kecuali `Assembly_level`, dari atribut BioSample.
  - *Tab* tersembunyi terbawa saat menyalin dari web (di dua aksesi dan satu nama organisme). Sel diketik ulang.
  - *Autofill* Excel menaikkan `Download_date` per baris. Diisi ulang dengan nilai tetap.
- **Catatan data:** `/geographic location` = `Indonesia: Sekolah Vokasi IPB`, tetapi `/isolation source` = `A farm in Sukabumi city` dan koordinat (sekitar 6,94° LS, 106,95° BT) juga menunjuk Sukabumi. Kemungkinan pengirim mengisi lokasi lab. Nilai disalin apa adanya. Masuk ke bagian keterbatasan laporan.
- **Jawaban *Cek dirimu*:**
  1. BioProject adalah payung proyek penelitian (di sini PRJNA1075840) yang mengelompokkan semua sampel dan data. BioSample menyimpan keterangan satu sampel biologis: inang, sumber isolasi, tanggal, lokasi, dan pengumpul. Aksesi *assembly* (GCA) adalah rakitan sekuens genom yang dibuat dari *read* sampel itu. Keterangan inang ada di BioSample (atribut `/host`).
  2. GCA adalah rakitan asli yang dikirim peneliti ke GenBank. GCF adalah salinan RefSeq dari genom yang sama, yang dikurasi dan dianotasi ulang oleh NCBI. Kalau keduanya dihitung, satu isolat masuk dua kali, sehingga frekuensi gen AMR menjadi bias. GCA dipilih karena merupakan rekaman primer dan dimiliki tiap isolat.
  3. `Host`. Kolom ini satu-satunya yang bervariasi secara bermakna (hewan, pakan, lingkungan). `Collection_source` dan `Location` sama untuk semua isolat, sedangkan `Collection_date` hanya terbagi tiga tanggal.
- **Pertanyaan yang muncul:**
  - Apakah perlu kolom kategori turunan (hewan / pakan / lingkungan) untuk figur? Kolom itu tidak boleh masuk `genome_metadata.csv` karena bukan nilai NCBI; lebih tepat dibuat di skrip figur, dengan pemetaannya ditulis eksplisit.
  - Apakah `genome_metadata.xlsx` ikut di-*commit* atau dimasukkan ke `.gitignore`? Belum diputuskan; diputuskan paling lambat Hari 10.

### 2026-11-25 (Hari 3)
- **Langkah:** unduh 9 genom dan unggah ke Galaxy
- **Input:** 9 aksesi GCA Kelompok A (GCA_037201825.1 sampai GCA_037201905.1)
- **Parameter:** cara unduh = CLI (NCBI `datasets download genome accession ... --include genome`); server = usegalaxy.eu; history = `ecoli-sukabumi-amr`, dipublikasikan di https://usegalaxy.eu/u/ollyblu/h/ecoli-sukabumi-amr
- **Hasil / file keluaran:**
  - `data/raw_genomes/*.fna` (9 file, tidak di-commit). Header tiap file cocok dengan nomor strain di metadata.
  - Jumlah urutan per file: 1. Jumlah celah (blok ≥10 N) per file, dengan jumlah *contig* = celah + 1: SID09 40, SID10 41, SID11 42, SID12 44, SID14 43, SID16 36, SID17 41, SID19 40, SID20 51. Hasilnya cocok persis dengan `number_of_contigs` di laporan assembly NCBI untuk kesembilan aksesi (37 sampai 52). Hitungan pertama memakai semua blok N dan kelebihan 1 sampai 2 di enam isolat, karena blok pendek (1 sampai 9 N) adalah basa ambigu di dalam *contig*, bukan celah. Perintah di lembar kerja sudah diganti ke `N{10,}`.
  - Galaxy: 9 dataset berstatus `ok` (hijau), format `fasta`, bernama `SID09` sampai `SID20`. Ukuran tiap dataset sama persis dengan file lokal aksesinya, jadi tidak ada nama yang tertukar (dicek lewat API Galaxy, 25 November 2026).
- **Kendala dan solusinya:**
  - Lembar kerja Hari 3 menganggap `grep -c '>'` sama dengan jumlah *contig*. Ternyata tiap assembly berupa satu *scaffold* kromosom yang berisi celah N, dengan panjang celah bervariasi (sekitar 0,08 sampai 9 kb). Lembar kerja diperbaiki: *contig* dihitung dari celah N.
  - `git status` belum bisa dijalankan karena folder ini belum jadi repo git. Ditunda ke Hari 10; `.gitignore` sudah mengecualikan `*.fna` dan `*.zip`.
- **Catatan data (untuk bagian keterbatasan):**
  - Tidak ada sekuens plasmid di kesembilan assembly. Gen AMR *acquired* yang dibawa plasmid bisa tidak terdeteksi.
  - Sekitar 209 sampai 274 kb per genom (kira-kira 5%) berupa N. Gen yang jatuh di celah tidak terbaca.
  - Panjang dan GC sempat dihitung kasar sebelum QUAST. Aturan QC belum menyebut apakah *Total length* dihitung dengan atau tanpa N. Kedua cara tidak menyentuh batas FAIL, jadi tidak ada isolat yang dikeluarkan; yang terpengaruh hanya label WARN di `Notes`. Keputusannya diambil dan dicatat di Hari 4.
- **Pertanyaan yang muncul:**
  - Kenapa pengirim hanya menyetor kromosom? Apakah plasmid tidak di-*assemble*, atau sengaja tidak dikirim?
    - **Jawaban sementara (dicek 25 November 2026):** `Isolation_and_detection_of_antibiotics_resistance_.pdf` bukan paper dataset ini. Isinya Hardiati dkk. (2021), *J. Adv. Vet. Anim. Res.* 8(1):84–90, https://doi.org/10.5455/javar.2021.h489: 25 isolat dari swab kloaka broiler Sukabumi (Januari 2019), diuji dengan Kirby–Bauer dan PCR lima gen, tanpa sekuensing genom. Paper itu cocok sebagai pembanding di diskusi, bukan sebagai sumber metode.
    - BioProject PRJNA1075840 tidak menautkan publikasi dan tidak menjelaskan metode. Deskripsinya hanya "Whole genome sequence of 12 Samples". *Read* mentah juga tidak ada di SRA (pencarian PRJNA1075840 di SRA: 0 hasil), jadi assembly tidak bisa diulang.
    - Laporan assembly NCBI (pengirim: Genomik Solidaritas Indonesia) mencatat sekuensing Oxford Nanopore GridION, *assembly method* "medaka v. 1.11.1", dan *coverage* 22 sampai 58×. Medaka hanya alat *polishing*, jadi *assembler*-nya tidak disebut.
    - Dugaan, belum terbukti: *read* panjang Nanopore biasanya menghasilkan kromosom dan plasmid yang tertutup melingkar tanpa celah. Di sini kromosomnya berupa satu *scaffold* berisi 36 sampai 51 celah dengan panjang bervariasi, pola yang khas untuk *scaffolding* berbasis genom rujukan: *contig* diurutkan menurut kromosom rujukan, lalu panjang celah diperkirakan dari rujukan itu. Cara ini cenderung membuang *contig* yang tidak cocok dengan kromosom rujukan, termasuk plasmid. Dari data publik tidak bisa dipastikan apakah plasmid terbuang di langkah itu atau sengaja tidak dikirim.
    - Untuk laporan: tulis bahwa assembly hanya memuat kromosom, metode assembly tidak didokumentasikan, dan gen AMR yang dibawa plasmid kemungkinan besar terlewat. Jumlah gen *acquired* di hasil harus dibaca sebagai batas bawah.
  - Apakah QUAST di Galaxy punya opsi `--split-scaffolds`? Diperiksa di Hari 4.

### 2026-11-25 (Hari 4, keputusan sebelum melihat angka QUAST)
- **Keputusan 1, *Total length* untuk aturan QC:** memakai panjang **tanpa N**, yaitu baris *Total length* pada versi `_broken` (hasil pecahan di celah N ≥ 10). Alasan: N bukan basa hasil sekuensing (celah hasil perkiraan *scaffolding*), dan ambang QC.watch diturunkan dari panjang assembly yang pada umumnya berbasis *contig*. Panjang dengan N (baris bawaan pada versi asli) tetap dicatat di `Notes` sebagai pembanding. Label WARN dan FAIL hanya mengikuti panjang tanpa N.
- **Keputusan 2, jumlah *contig*:** memakai `# contigs` (≥ 500 bp, ambang bawaan `--min-contig 500`) dari versi `_broken`, sama untuk semua isolat. Angka `# contigs (>= 0 bp)` dicatat di `Notes` kalau berbeda dari angka NCBI (37 sampai 52).
- **Parameter yang dipilih di formulir:** QUAST 5.3.0+galaxy3 di usegalaxy.eu; *Assembly mode* = Co-assembly (satu laporan untuk 9 dataset; mode Individual hanya menerima satu dataset per *job* sehingga menghasilkan 9 laporan terpisah); tanpa rujukan; *Type of organism* = Prokaryotes (bawaan); *Are assemblies scaffolds rather than contigs?* = **Yes** (ini padanan `--split-scaffolds` di Galaxy, menjawab pertanyaan Hari 3); keluaran = HTML + Tabular; setelan lain bawaan.

### 2026-11-25 (Hari 4)
- **Langkah:** QC assembly dengan QUAST
- **Input:** 9 FASTA di history `ecoli-sukabumi-amr` (SID09 sampai SID20)
- **Parameter:** QUAST 5.3.0+galaxy3 di usegalaxy.eu, tanpa rujukan, mode Co-assembly, *split scaffolds* = Yes (`--split-scaffolds`), `--min-contig 500`, `--min-identity 95.0`, keluaran HTML dan tabular. Jumlah *contig* yang dipakai: `# contigs` (≥ 500 bp) versi `_broken`, sama untuk semua isolat. *Total length* untuk QC: versi `_broken` (tanpa N). Keputusan keduanya ditulis sebelum angka dilihat (entri di atas).
- **Hasil / file keluaran:** `results/assembly_quality.csv` (9 baris); `results/raw_tool_outputs/quast_report.tsv` (disalin dari pratinjau dataset 12 di Galaxy, bukan unduhan file asli). Isolat dikeluarkan: **tidak ada**. Panjang tanpa N 4,276 sampai 4,392 Mb, semuanya di pita WARN 4,1 sampai 4,4 Mb. Dengan N, panjangnya 4,497 sampai 4,611 Mb, di luar pita WARN. GC 50,70 sampai 50,95%; pita WARN GC (50,88 sampai 51,13%) mengenai SID09, SID10, SID11, SID12, SID17. Jumlah *contig* 37 sampai 52, cocok dengan hitungan Hari 3 dan laporan NCBI. N50 versi `_broken` 245.980 sampai 355.971 bp; versi asli sama dengan panjang kromosom karena satu *scaffold*. Celah N sekitar 4.566 sampai 6.027 per 100 kbp di versi asli, hampir 0 setelah dipecah.
- **Kendala dan solusinya:** mode *Individual* hanya menerima satu dataset per *job* (batch), jadi dipakai mode Co-assembly supaya satu laporan memuat semua isolat. Nilai GC `50.8` dan `50.7` di CSV tertulis tanpa nol di belakang (selisih format saja). Pita WARN panjang memberi label WARN ke semua isolat, jadi label ini tidak membedakan isolat satu dari yang lain.
- **Pertanyaan yang muncul:**
  - Apakah panjang tanpa N (sekitar 4,3 Mb) yang di bawah median QC.watch (5,1 Mb) menandakan sekitar 0,8 Mb sekuens tidak ada di assembly (plasmid, daerah di celah)? Jawaban sementara: celah N sendiri hanya 0,2 sampai 0,27 Mb, jadi panjang dengan N (4,5 sampai 4,6 Mb) pun masih di bawah median. Genom *E. coli* memang bervariasi 4,5 sampai 5,5 Mb, jadi ini bisa juga ukuran genom sebenarnya. Dibahas di bagian keterbatasan.
  - Menjawab pertanyaan Hari 1: pita WARN tidak mengubah aturan eksklusi. Karena semua isolat ber-WARN panjang, WARN GC pada lima isolat dicatat saja; tidak ada bukti kontaminasi dari angka ini.
  - Menjawab pertanyaan Hari 3: label opsi *split-scaffolds* di Galaxy adalah "Are assemblies scaffolds rather than contigs?".

### 2026-11-25 (Hari 5)
- **Langkah:** deteksi gen AMR dengan AMRFinderPlus
- **Input:** 9 FASTA (SID09 sampai SID20) di history `ecoli-sukabumi-amr`. Semua lolos QC Hari 4 (tidak ada yang dikeluarkan), jadi semuanya masuk analisis utama.
- **Parameter:** AMRFinderPlus 4.2.7+galaxy0, DB V4.2-2026-05-15.1, input nukleotida, `--organism Escherichia`, tanpa `--plus`, `--ident_min -1.0` (ambang terkurasi, bawaan 0,9), `--coverage_min 0.5`, `--translation_table 11`, kolom versi tambahan mati. Versi DB dibaca dari `tool_stderr` job (`Database version: 2026-05-15.1`). Satu *job* per isolat lewat mode *batch*; satu job memakan sekitar 342 detik.
- **Hasil / file keluaran:** `results/raw_tool_outputs/SIDxx_amrfinder.tsv` (9 file, header 22 kolom, belum diubah). Ukuran tiap file cocok dengan dataset di Galaxy. Jumlah baris data per isolat: SID09 1, SID10 2, SID12 1, SID19 1, SID20 7; SID11, SID14, SID16, SID17 nol (hanya header). Semua baris ber-*Method* `POINTX` dan *Element type* AMR; **tidak ada gen *acquired* sama sekali** (konsisten dengan assembly tanpa plasmid, lihat Hari 3). Tidak ada baris `PARTIALX`, `PARTIAL_CONTIG_ENDX`, `INTERNAL_STOPX`, atau `HMM`.
- **Kendala dan solusinya:**
  - Unduhan langsung lewat `curl` ditolak (403) walau history dipublikasikan. Unduhan lewat Chrome ternyata berhasil, tetapi mendarat di root folder proyek (`Galaxy14-[AMRFinderPlus on dataset 9_ ...].tabular` dan seterusnya), bukan di Downloads. Sebelum itu saya sempat menulis isi TSV dari `/api/datasets/<id>/display?preview=True` ke `results/raw_tool_outputs/`. Hash SHA-256 kesembilan file hasil tulisan identik dengan unduhan asli (dicek 25 November 2026), jadi isinya sama persis dengan keluaran Galaxy.
  - Nama file memakai `SIDxx_amrfinder.tsv` (bukan `SKBxx` seperti di lembar kerja), mengikuti skema `Sample_ID`.
- **Pertanyaan yang muncul (bahan Hari 6):**
  - Banyak baris bersubtipe `POINT_DISRUPT` (mis. `ompC_R308VfsTer16`, `uhpT_L228AfsTer25`, `nfsB_L22TfsTer35`, `marR_A70SfsTer11`, `ompC_S184Ter`): mutasi *frameshift*/stop yang merusak gen, bukan substitusi asam amino. Metodenya `POINTX`, jadi menurut aturan yang sudah ditetapkan tetap dihitung 1. Perlu kolom/penanda pembeda di kurasi supaya tidak tercampur dengan `POINT` biasa.
  - `parE_I355T` di SID20 berstatus `POINTX` dengan cakupan 63,02% (di bawah 90%). Aturan deteksi tidak memakai cakupan, jadi tetap 1; catat di `Notes`.
  - `gyrA_D87N` dan `gyrA_S83L` di SID20 berasal dari satu lokus yang sama (koordinat identik), tetap dua baris, jangan digabung.
  - Hit `ompC_*` dan `uhpT_*` ada di beberapa isolat dengan identitas ke rujukan 90 sampai 100%: perlu hati-hati menafsirkan sebagai resistansi tanpa uji fenotipik.

### 2026-11-25 (Hari 6)
- **Langkah:** membaca keluaran AMRFinderPlus; menulis `scripts/curate_hits.py`
- **Input:** `results/raw_tool_outputs/SID*_amrfinder.tsv` (9 file)
- **Parameter:** kategori counted = EXACTX, ALLELEX, BLASTX, POINTX (konstanta `COUNTED_METHODS` di atas skrip); nama kolom AMRFinderPlus versi 4: `Element symbol`, `Type`, `Subtype`, `Class`, `Subclass`, `Method`, `% Coverage of reference`, `% Identity to reference`, `Contig id`, `Start`, `Stop`. Pandas 3.0.1, Python 3.11.0 (`requirements.txt`).
- **Hasil / file keluaran:** `results/amr_hits_curated.csv` (12 baris, semuanya `counted`, tidak ada `note`). Hitungan manual SID20 (`awk` pada kolom Type dan Method, tanpa pandas): 7 baris AMR, 7 counted, 0 note, sama dengan keluaran skrip. Kesembilan isolat juga dicocokkan: SID09 1, SID10 2, SID11 0, SID12 1, SID14 0, SID16 0, SID17 0, SID19 1, SID20 7, total 12. Dijalankan dua kali, berkas keluaran identik (MD5 sama).
- **Keputusan desain (tidak mengubah aturan deteksi):**
  - Header CSV tidak ditambah kolom. Subtipe (`POINT` atau `POINT_DISRUPT`) dan *Method* ditulis di `Notes` sebagai `Subtype=...; Method=...`, supaya `build_matrix.py` bisa memisahkan mutasi titik dari gen *acquired* dan membedakan `POINT_DISRUPT` (frameshift/stop) dari substitusi.
  - `Drug_class_or_mechanism` = `Class/Subclass`, atau `Class` saja kalau keduanya sama.
  - `Notes` juga memuat: cakupan di bawah 90% (hanya `parE_I355T` di SID20, 63,02%, tetap `counted` sesuai aturan) dan lokus yang sama (`gyrA_D87N` dan `gyrA_S83L` di SID20, koordinat identik, tetap dua baris).
- **Uji jalur tepi:** (1) pola nama file cocok untuk `SID09_amrfinder.tsv` dan `Galaxy12-[AMRFinderPlus on SID09].tabular`, tidak cocok untuk `quast_report.tsv`; (2) *Method* tiruan `NEWX` pada salinan data (folder sementara, data asli tidak disentuh) memunculkan `UserWarning` dan jatuh ke `note`; (3) berkas `SID99_amrfinder.tsv` memicu keluar dengan galat karena tidak ada di metadata.
- **Kendala dan solusinya:** semua hit `POINTX`, jadi cabang `note` dan cabang gen *acquired* belum teruji oleh data asli, hanya oleh uji tiruan di atas. Hasil "tidak ada gen *acquired*" adalah temuan data (assembly tanpa plasmid, lihat Hari 3), bukan galat skrip.
- **Pertanyaan yang muncul:**
  - Apakah `POINT_DISRUPT` (frameshift/stop prematur) pantas disebut "resistansi" sama seperti substitusi `POINT`? Gen yang rusak bisa memberi resistansi lewat hilangnya fungsi (misalnya porin `ompC`), tetapi efeknya tetap perlu uji fenotipik. Untuk matriks Hari 7, kolom penanda memisahkan keduanya.

### 2026-11-25 (Hari 7)
- **Langkah:** membangun matriks presence/absence dengan `scripts/build_matrix.py`
- **Input:** `results/amr_hits_curated.csv`, `results/assembly_quality.csv`, `metadata/genome_metadata.csv`
- **Parameter:** sel = 1 bila ada hit `counted`; **NA** bila tidak ada `counted` tetapi ada hit `note` (bukan 0); 0 bila tidak ada hit sama sekali. Isolat dalam matriks = yang lolos batas FAIL QC (konstanta di skrip, sama dengan `analysis_notes.md`): 9 dari 9. `Feature_type` = `point_mutation` bila subtipe diawali `POINT`, selain itu `acquired`. `Feature_subtype` (kolom tambahan) menyimpan `POINT` atau `POINT_DISRUPT`, menjawab pertanyaan Hari 6. `Drug_class` diambil dari `Drug_class_or_mechanism`. Baris diurut: acquired dulu, lalu golongan, lalu nama fitur.
- **Hasil / file keluaran:** `results/amr_presence_absence.csv` (12 fitur × 9 isolat; 0 acquired, 12 mutasi titik, 0 sel NA). Angka 1 per isolat: SID09 1, SID10 2, SID11 0, SID12 1, SID14 0, SID16 0, SID17 0, SID19 1, SID20 7, cocok dengan jumlah fitur unik `counted` di tabel terkurasi (uji silang otomatis di skrip; skrip berhenti dengan galat kalau tidak cocok). Terbaca pandas, `Feature` unik. Dijalankan dua kali, hasil sama.
- **Uji data tiruan** (folder sementara, data asli tidak disentuh): gen *acquired* `blaTEM-1` di dua *contig* pada SID09 tetap 1 dan jejaknya masuk `Notes` ("gen sama di 2 contig"); `PARTIAL_CONTIG_ENDX` pada SID10 menghasilkan NA dan tercatat di `Notes`; `PARTIALX` pada SID11 untuk `tet(A)` menghasilkan NA. Cabang NA dan *acquired* tidak muncul di data asli, jadi hanya teruji lewat data tiruan.
- **Periksa dengan mata:** `marR_A70SfsTer11` hanya di SID12 dan `gyrA_D87N` serta `gyrA_S83L` hanya di SID20, cocok dengan TSV mentah (`POINT_DISRUPT` dan `POINT`).
- **Kendala dan solusinya:** kolom `Notes` matriks kosong untuk semua baris karena tidak ada hit `note` atau gen di banyak *contig*. Itu hasil data, bukan galat. `0` di matriks juga tidak membedakan "gen tidak ada" dari "gen ada di celah N atau plasmid yang tidak ada di assembly" (lihat Hari 3).
- **Pertanyaan yang muncul:**
  - Matriks hanya berisi mutasi titik (12 fitur). Figur Hari 8 perlu menyatakan terang bahwa panel *acquired* kosong karena assembly tanpa plasmid, bukan karena isolatnya bersih. Enam baris `POINT_DISRUPT` dan enam `POINT` perlu dibedakan warna atau tandanya.
  - Empat isolat (SID11, SID14, SID16, SID17) bernilai 0 di semua baris. Di heatmap tampil sebagai kolom kosong; tetap dimasukkan, karena "tidak ada hit" adalah hasil.

### 2026-11-25 (Hari 8)
- **Langkah:** membuat figur 1 dan 2 dengan `scripts/plot_figures.py`; mengumpulkan literatur
- **Input:** `results/amr_presence_absence.csv`; `metadata/genome_metadata.csv`
- **Parameter:** seaborn 0.13.2, matplotlib 3.11.2 (ditambahkan ke `requirements.txt`), dpi 300. Kategori sumber isolat dipetakan eksplisit di `SOURCE_BY_HOST` (Hewan: kambing, sapi, bebek, angsa; Pakan: pakan bebek, pakan ayam petelur; Lingkungan: 2 isolat), bukan dari NCBI. Host yang tidak ada di pemetaan membuat skrip berhenti.
- **Hasil / file keluaran:** `figures/fig1_amr_count_per_isolate.png` (batang bertumpuk: acquired / substitusi / frameshift-stop; jumlah per isolat SID09 1, SID10 2, SID11 0, SID16 0, SID17 0, SID14 0, SID19 1, SID12 1, SID20 7, cocok dengan Hari 7); `figures/fig2_amr_heatmap.png` (12 fitur × 9 isolat, dikelompokkan per golongan, pita kiri membedakan substitusi dan frameshift/stop, pita atas sumber isolat, warna NA di legenda walau tidak ada sel NA); `report/references.md` (7 paper)
- **Kendala dan solusinya:** render pertama menumpuk legenda dan kotak catatan di atas batang SID20, dan label sumbu x tertimpa pita sumber; diperbaiki lalu PNG dibuka ulang dan label terbaca. Kedua figur menyatakan bahwa panel acquired kosong karena assembly tanpa plasmid.
- **Literatur:** metadata paper diambil dari Crossref, lalu semua DOI dibuka dan dicocokkan satu per satu (25 November 2026: cocok). Paper sumber dataset tidak ditemukan. Paper #5 sampai #7 baru dibaca abstrak atau judulnya; baca isinya sebelum dikutip.
- **Pertanyaan yang muncul:** SID20 menyumbang 7 dari 12 fitur dan satu-satunya isolat dengan mutasi kuinolon (gyrA, parC, parE). Dengan n = 2 per kelompok lingkungan dan pakan, tidak ada perbandingan antar sumber yang bisa diklaim.

### 2026-11-26 (Hari 9)
- **Langkah:** menulis draf laporan
- **Input:** `results/*` (QC, tabel terkurasi, matriks, TSV mentah), `figures/*`, `report/references.md`, bagian aturan dan log di `analysis_notes.md`, PDF Hardiati 2021
- **Parameter:** -
- **Hasil / file keluaran:** `report/report.md` (draf 1: Abstract, Introduction, Methods, Results, Discussion, Data and code availability, References). Urutan penulisan: Methods, Results, Discussion, Abstract. Semua angka di Results dicocokkan dengan CSV (12 fitur; SID20 7, SID10 2, SID09/SID12/SID19 masing-masing 1, empat isolat 0; 6 `POINT` dan 6 `POINT_DISRUPT`; kelompok sumber 5 hewan, 2 pakan, 2 lingkungan). Panjang badan teks termasuk tabel sekitar 3.100 kata, di atas target 1.500 sampai 2.500; kalau perlu dipangkas, mulai dari Introduction dan subbagian *Implications*.
- **Kendala dan solusinya:**
  - Lembar kerja menyebut tiap kelompok sumber 2 sampai 3 isolat; datanya 5 hewan, 2 pakan, 2 lingkungan. Laporan memakai angka sebenarnya.
  - Paper #5 sampai #7 belum dibaca isinya, jadi dikutip hanya untuk klaim umum dan ditandai † di daftar rujukan serta `[TODO]` di teks. Klaim mutasi QRDR *gyrA*/*parC* butuh rujukan primer, dan keterangan tiap gen `POINT_DISRUPT` (*ompC*, *uhpT*, *nfsB*, *marR*) belum dicek ke katalog AMRFinderPlus.
  - Hardiati 2021 mendeteksi *gyrA* dengan PCR (amplikon 626 bp) pada 25/25 isolat, yaitu keberadaan gen, bukan mutasi; laporan menyatakan perbedaan ini dan tidak membandingkan angka.
  - Tiga hit *ompC* beridentitas 90,2 sampai 91,7% ke rujukan; disebut di Discussion, belum diselidiki.
- **Yang masih harus kamu kerjakan:** (1) isi atau hapus semua `[TODO]` di `report/report.md`; (2) baca paper #5 sampai #7 dan paper Hardiati sebelum mempertahankan klaimnya; (3) cek ulang kalimat klaim dengan tabel "Merumuskan klaim" di lembar kerja Hari 9 (tidak ada kata "resistant"/"susceptible" untuk isolat); (4) tulis ulang bagian yang kamu tidak bisa jelaskan tanpa membaca; (5) commit baru bisa setelah folder jadi repo git (Hari 10).
- **Pertanyaan yang muncul:** apakah identitas 90 sampai 92% pada *ompC* menandakan alel yang beragam atau galat assembly di daerah itu? Perlu pembanding dari genom rujukan *E. coli* bila ada waktu (Extension).

### 2026-11-26 (Hari 10)
- **Langkah:** merapikan README dan mempublikasikan repositori
- **Input:** seluruh folder proyek
- **Parameter:** akun GitHub `ollyblu`, repositori `ecoli-amr-sukabumi`, publik, cabang `main`. `.gitignore` mengecualikan genom mentah dan `*.pdf` (PDF pihak ketiga). `genome_metadata.xlsx` ikut di-*commit* karena `convert_to_csv` membutuhkannya.
- **Hasil / file keluaran:** https://github.com/ollyblu/ecoli-amr-sukabumi. Commit skrip penghasil figur: `[COMMIT_HASH]` (tercatat di Methods laporan). `README.md` tanpa `TODO`. Daftar berkas di GitHub tidak memuat `.fna`, `.zip`, `quast_*/`, `.pdf`, atau `CLAUDE.md`. `python run_all.py` di salinan bersih (skrip, metadata, tabel QC, TSV mentah) menghasilkan kedua CSV dan kedua PNG yang identik byte demi byte dengan yang di-*commit*.
- **Kendala dan solusinya:** hash commit baru ada setelah commit pertama, jadi hash ditambahkan ke laporan lewat commit kedua.
- **Belum selesai:** `[TODO]` di `report/report.md` (rujukan QRDR, katalog AMRFinderPlus, paper bertanda †); pengecekan repositori di browser.
- **Pertanyaan yang muncul:** laporan baru final setelah `[TODO]` terisi; hash di Methods perlu diperbarui kalau skrip berubah.

### YYYY-MM-DD
- **Langkah:**
- **Input:**
- **Parameter:**
- **Hasil / file keluaran:**
- **Kendala dan solusinya:**
- **Pertanyaan yang muncul:**
