# Hari 3: unduh genom dan unggah ke Galaxy

## Tujuan

Sembilan file FASTA ada di satu *history* Galaxy di usegalaxy.eu, masing-masing bernama sesuai `Sample_ID`.

## Prasyarat

- `genome_metadata.csv` sudah berisi 9 baris dan skema `Sample_ID` sudah final
- Akun https://usegalaxy.eu (gratis)

## Langkah

- [x] Unduh genom dengan salah satu cara:
  - **Web:** di halaman genom NCBI klik *Download*, pilih GenBank dan *Genome sequences (FASTA)*. File genomnya ada di `ncbi_dataset/data/GCA_.../GCA_..._genomic.fna` di dalam `.zip`.
  - **CLI:** `datasets download genome accession GCA_037201825.1 GCA_037201885.1 ... --include genome --filename sukabumi.zip`
- [x] Ekstrak, lalu taruh kesembilan `.fna` di `data/raw_genomes/`
- [ ] Jalankan `git status` dan pastikan tidak ada file `.fna` atau `.zip` yang muncul. `.gitignore` sudah mengecualikan keduanya. *Ditunda ke Hari 10: folder ini belum jadi repo git*
- [x] Hitung jumlah urutan per file (`grep -c '>' data/raw_genomes/*.fna`). Hasilnya 1 per file. Kesembilan assembly ini berlevel *Chromosome*: tiap file berisi satu *scaffold* kromosom, yaitu *contig-contig* yang sudah diurutkan dan disambung dengan celah berisi huruf N. Tidak ada sekuens plasmid
- [x] Hitung celah N per file. Jumlah *contig* = jumlah celah + 1, dan seharusnya sama dengan angka *contig* di NCBI (37 sampai 52). Yang dihitung hanya blok minimal 10 N; blok yang lebih pendek adalah basa ambigu di dalam *contig*, bukan celah antar-*contig*:
  ```bash
  for f in data/raw_genomes/*.fna; do echo "$f $(grep -v '>' "$f" | tr -d '\n\r' | grep -oiE 'N{10,}' | wc -l)"; done
  ```
- [x] Login ke usegalaxy.eu, buat *history* baru bernama `ecoli-sukabumi-amr`
- [x] Klik *Upload*, pilih kesembilan `.fna`, set tipe `fasta`, lalu *Start*
- [x] Ganti nama tiap dataset ke `Sample_ID`-nya (ikon pensil)
- [x] Isi log, commit (tanpa genom). *Log terisi; commit ditunda ke Hari 10*

## Kalau macet

- Galaxy tidak membaca `.zip` sebagai FASTA. Ekstrak dulu.
- Dataset merah berarti gagal. Klik ikon informasi untuk membaca pesan galatnya, lalu catat di log.
- Unggahan lambat itu biasa. Satu genom *E. coli* sekitar 5 MB.

## Hasil yang bisa dicek

- 9 dataset hijau di *history* `ecoli-sukabumi-amr`
- Nama tiap dataset sama persis dengan `Sample_ID` di CSV
- `git status` bersih dari file genom

## Cek dirimu

1. Baris yang diawali `>` di file FASTA berisi apa? Kenapa di proyek ini jumlahnya 1, padahal NCBI mencatat 37 sampai 52 *contig*? Apa bedanya *contig* dan *scaffold*?
2. Kenapa nama dataset di Galaxy perlu diganti sebelum menjalankan tool?
3. Kenapa genom mentah tidak ikut diunggah ke GitHub, padahal datanya publik?

## Templat log

```
### YYYY-MM-DD (Hari 3)
- **Langkah:** unduh 9 genom dan unggah ke Galaxy
- **Input:** 9 aksesi GCA
- **Parameter:** cara unduh = <web/CLI>; server = usegalaxy.eu; history = ecoli-sukabumi-amr
- **Hasil / file keluaran:** data/raw_genomes/*.fna (9 file, tidak di-commit); jumlah urutan per file: <...>; jumlah celah N per file: <...>
- **Kendala dan solusinya:**
- **Pertanyaan yang muncul:**
```

Sebelumnya: [Hari 2](hari-02-metadata.md) · Berikutnya: [Hari 4](hari-04-quast.md)
