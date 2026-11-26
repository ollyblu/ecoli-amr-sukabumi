# Hari 11 (opsional): AMRFinderPlus di komputer sendiri

Boleh dimajukan, misalnya bersamaan dengan Hari 5. Galaxy tetap jalur utama untuk laporan.

## Tujuan

AMRFinderPlus berjalan di WSL lewat conda pada satu isolat, dan hasilnya dibandingkan dengan keluaran Galaxy.

## Kaitan dengan silabus

`02-silabus-dry-lab.md`: baris perintah, conda, dan WSL.

## Langkah

- [ ] Pasang WSL (Ubuntu) dari PowerShell dengan `wsl --install`, lalu *restart*
- [ ] Pasang Miniconda di dalam WSL, tambahkan kanal `conda-forge` dan `bioconda`
- [ ] `conda create -n amr -c conda-forge -c bioconda ncbi-amrfinderplus`
- [ ] `conda activate amr`, lalu `amrfinder -u` untuk mengunduh database
- [ ] Catat `amrfinder --version` dan versi database
- [ ] Jalankan pada satu isolat: `amrfinder -n SIDxx.fna -O Escherichia -o SIDxx_local.tsv`
- [ ] Bandingkan dengan TSV Galaxy untuk isolat yang sama: jumlah baris, simbol gen, dan *Method*
- [ ] Kalau berbeda, periksa versi tool dan database lebih dulu
- [ ] Simpan perintah yang kamu pakai di `scripts/run_amrfinder_local.sh`
- [ ] Isi log, commit

Panduan resmi: https://github.com/ncbi/amr/wiki/Install-with-bioconda

## Hasil yang bisa dicek

- Satu TSV lokal dan catatan perbandingannya dengan Galaxy
- Versi tool dan database lokal tercatat

## Cek dirimu

1. Kalau Galaxy dan lokal memakai versi tool sama tapi database berbeda, perbedaan hasil seperti apa yang kamu duga?
2. Apa untungnya menjalankan tool sendiri dibanding lewat Galaxy?

## Templat log

```
### YYYY-MM-DD (Hari 11)
- **Langkah:** AMRFinderPlus lokal untuk satu isolat
- **Input:** data/raw_genomes/<file>.fna
- **Parameter:** amrfinder <versi>, DB <versi>, -O Escherichia
- **Hasil / file keluaran:** <file>; perbedaan dengan Galaxy: <...>
- **Kendala dan solusinya:**
- **Pertanyaan yang muncul:**
```

Sebelumnya: [Hari 10](hari-10-readme-github.md) · Berikutnya: [Hari 12](hari-12-opsional-notebook.md)
