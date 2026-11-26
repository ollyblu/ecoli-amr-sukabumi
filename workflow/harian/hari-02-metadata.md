# Hari 2: metadata

## Tujuan

`metadata/genome_metadata.csv` berisi 9 baris, satu per isolat Kelompok A, dengan nilai yang disalin persis dari NCBI.

## Prasyarat

- Hari 1 selesai, termasuk dua TODO
- Daftar 9 aksesi GCA dari `../dataset_candidates.md`

## Langkah

- [x] Putuskan skema `Sample_ID`, misalnya `SID09` untuk isolat 9 dan `SID16` untuk isolat 16. Skema ini jadi label figur, jadi pilih yang pendek. Catat keputusannya di log.
- [x] Untuk tiap aksesi, buka `https://www.ncbi.nlm.nih.gov/datasets/genome/<AKSESI>/`
- [x] Dari halaman genom, buka tautan BioSample (berawalan SAMN)
- [x] Salin *host*, *isolation_source*, *collection_date*, *geo_loc_name*, dan nama *strain* atau *isolate* ke kolom yang sesuai
- [x] Isi `Assembly_level` dari halaman genom dan `Download_date` dengan tanggal hari ini
- [x] Atribut yang tidak ada ditulis `not reported`
- [x] Cocokkan ulang dua baris secara acak dengan halaman web
- [ ] Isi log, commit (`Add genome metadata for 9 Sukabumi isolates`). Log sudah diisi; commit menunggu repositori git dibuat (Hari 10)

Centang per aksesi:

| Aksesi | Isolat | Selesai |
|---|---|---|
| GCA_037201825.1 | 16 | [x] |
| GCA_037201885.1 | 17 | [x] |
| GCA_037201895.1 | 11 | [x] |
| GCA_037201835.1 | 9 | [x] |
| GCA_037201905.1 | 10 | [x] |
| GCA_037201845.1 | 19 | [x] |
| GCA_037201855.1 | 14 | [x] |
| GCA_037201875.1 | 12 | [x] |
| GCA_037201865.1 | 20 | [x] |

Header kolom: `Sample_ID, Assembly_accession, BioProject, BioSample, Organism, Strain_or_isolate, Host, Collection_source, Collection_date, Location, Assembly_level, Download_date`.

**Jalur CLI (opsional).** `datasets summary genome accession <AKSESI...>` menghasilkan JSON yang bisa kamu olah dengan Python. Simpan skripnya di `scripts/` dan tetap cocokkan beberapa baris secara manual.

## Aturan menyalin

- Jangan menerjemahkan. Kalau BioSample menulis `Anas platyrhynchos javanica`, tulis itu, bukan "itik".
- Jangan menebak. Kolom kosong di NCBI berarti `not reported`.
- Nilai yang mengandung koma diberi tanda kutip ganda supaya kolom CSV tidak bergeser.

## Hasil yang bisa dicek

- 10 baris di CSV (1 header, 9 data)
- Tidak ada sel kosong
- `pandas.read_csv` membacanya tanpa galat dan menghasilkan 12 kolom

## Cek dirimu

1. Apa beda BioProject, BioSample, dan aksesi assembly? Mana yang menyimpan keterangan inang?
2. Kenapa GCA yang dipakai dan GCF tidak dihitung?
3. Kolom mana yang nanti dipakai untuk mengelompokkan isolat di figur?

## Templat log

```
### YYYY-MM-DD (Hari 2)
- **Langkah:** mengisi metadata dari BioSample
- **Input:** 9 aksesi GCA Kelompok A
- **Parameter:** skema Sample_ID = <...>
- **Hasil / file keluaran:** metadata/genome_metadata.csv (9 baris)
- **Kendala dan solusinya:**
- **Pertanyaan yang muncul:**
```

Sebelumnya: [Hari 1](hari-01-aturan.md) · Berikutnya: [Hari 3](hari-03-unduh-dan-galaxy.md)
