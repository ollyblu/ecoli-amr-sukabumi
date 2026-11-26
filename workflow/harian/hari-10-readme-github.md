# Hari 10: README dan GitHub

## Tujuan

Repositori GitHub publik berisi README tanpa `TODO`, skrip, hasil, figur, dan laporan, tanpa genom mentah.

## Prasyarat

- Draf laporan Hari 9 selesai

## Langkah

- [x] Isi semua `TODO` di `README.md` dari hasil nyata. Cari sisanya dengan `grep -n TODO README.md`
- [x] Pastikan README menyebut cara menjalankan ulang: aksesi di `metadata/`, server Galaxy dan versi tool, lalu `python run_all.py`
- [x] Tampilkan kedua figur di README dengan tautan relatif
- [x] Jalankan `git status` dan `git ls-files`; pastikan tidak ada `.fna`, `.zip`, `.pdf` pihak ketiga, atau folder `quast_*/`
- [x] Salin folder ke tempat bersih (skrip, metadata, tabel QC, TSV mentah), jalankan `python run_all.py`, dan bandingkan hasilnya dengan berkas di repositori
- [x] Buat repositori publik di GitHub, tambahkan *remote*, lalu push
- [ ] Buka repositori di browser: figur tampil, tautan antarberkas jalan, `data/raw_genomes/` tidak ada
- [x] Tambahkan *commit hash* versi skrip penghasil figur ke bagian *Methods* laporan
- [ ] Isi log, lalu perbarui centang di `05-jadwal-mingguan.md`

## Hasil yang bisa dicek

- Tautan repositori publik
- `grep TODO` tidak menemukan apa pun di README
- Orang lain bisa mengikuti README tanpa bertanya padamu

## Cek dirimu

Latih jawaban lisan, satu sampai dua menit per pertanyaan:

1. Ceritakan proyekmu dalam tiga kalimat untuk orang yang bukan biolog.
2. Kenapa memilih dataset ini, dan kenapa Kelompok B tidak dipakai?
3. Apa beda *reads* dan *assembly*, dan kenapa kamu mulai dari *assembly*?
4. Kalau diulang, apa yang akan kamu ubah?

Proyek ini memperbesar peluangmu saat seleksi kalau kamu bisa menjelaskannya dengan bahasamu sendiri. Tidak ada proyek yang menjamin lolos.

## Templat log

```
### YYYY-MM-DD (Hari 10)
- **Langkah:** merapikan README dan mempublikasikan repositori
- **Input:** seluruh folder proyek
- **Parameter:** -
- **Hasil / file keluaran:** <URL repositori>
- **Kendala dan solusinya:**
- **Pertanyaan yang muncul:**
```

Sebelumnya: [Hari 9](hari-09-laporan.md) · Berikutnya (opsional): [Hari 11](hari-11-opsional-jalur-lokal.md)
