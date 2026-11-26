# Hari 6: membaca keluaran AMRFinderPlus dan mengurasi hit

## Tujuan

Kamu paham setiap kolom keluaran AMRFinderPlus, punya hitungan manual untuk satu isolat, dan `results/amr_hits_curated.csv` dibuat oleh `scripts/curate_hits.py`.

## Prasyarat

- 9 TSV mentah dari Hari 5
- Ringkasan kategori *Method* dan aturan deteksi di `../analysis_notes.md`

## Bagian A: membaca satu TSV (sekitar 45 menit)

- [x] Buka satu TSV dengan `pandas.read_csv(path, sep="\t")` dan tampilkan `df.columns`
- [x] Tulis nama kolom yang benar-benar ada di log. Versi 4 memakai nama seperti `Element symbol`, `Type`, `Subtype`, `Class`, `Method`; versi 3 memakai `Gene symbol`, `Element type`, dan seterusnya
- [x] Petakan nama kolom itu ke konsep berikut:

| Konsep | Nama kolom di filemu | Gunanya |
|---|---|---|
| Simbol gen | `Element symbol` | Nama gen atau mutasi, misalnya `blaTEM-1` atau `gyrA_S83L` |
| Tipe elemen | `Type` | AMR, VIRULENCE, atau STRESS. Hanya AMR yang dipakai |
| Subtipe | `Subtype` (di data ini `POINT` dan `POINT_DISRUPT`) | AMR untuk gen, POINT untuk mutasi titik |
| *Class* dan *Subclass* | `Class`, `Subclass` | Golongan antibiotik terkait |
| *Method* | `Method` | Dasar keputusan 1 atau catatan |
| *% Identity* dan *% Coverage* | `% Identity to reference`, `% Coverage of reference` | Seberapa mirip dan seberapa lengkap |
| *Contig id*, *Start*, *Stop* | `Contig id`, `Start`, `Stop` | Posisi di genom |

- [x] Hitung manual untuk **satu isolat**: jumlah baris AMR, jumlah yang dihitung 1, jumlah yang masuk catatan. Tulis ketiga angka di log. Angka ini jadi uji untuk skripmu

## Bagian B: `scripts/curate_hits.py` (sekitar 1 jam)

Spesifikasi, bukan kode jadi:

- [x] Baca semua TSV di `results/raw_tool_outputs/` (kecuali laporan QUAST)
- [x] Ambil `Sample_ID` dari nama file, cocokkan dengan `metadata/genome_metadata.csv`, dan hentikan skrip dengan pesan galat kalau ada yang tidak cocok
- [x] Saring tipe elemen = AMR
- [x] Petakan *Method* ke `Detection_category`: EXACTX, ALLELEX, BLASTX, POINTX menjadi `counted`; sisanya `note`. Kategori yang tidak dikenal jatuh ke `note` **dengan peringatan**, tidak dibuang diam-diam
- [x] Simpan daftar kategori `counted` sebagai satu konstanta di bagian atas skrip, supaya mudah dicocokkan dengan aturan
- [x] Tulis `results/amr_hits_curated.csv` dengan header yang sudah ada: `Sample_ID, Feature, Drug_class_or_mechanism, Detection_category, Pct_identity, Pct_coverage, Tool, Tool_version, DB_version, Notes`
- [x] Bandingkan hasil skrip dengan hitungan manual Bagian A. Kalau beda, cari penyebabnya sebelum lanjut dan catat di log
- [x] Buat `requirements.txt` dengan versi dipatok (`pandas==x.y.z` sesuai yang terpasang)
- [ ] Isi log, commit (`Add curate_hits.py and curated AMR hits`)

## Jebakan

- Nama file unduhan Galaxy kadang berbentuk `Galaxy12-[AMRFinderPlus on SID09].tabular`. Bersihkan dengan pola yang jelas dan uji polanya pada kesembilan nama.
- Gen yang sama bisa muncul di dua *contig* pada satu isolat. Di tabel terkurasi biarkan dua baris; catat kejadiannya di `Notes`.
- Mutasi titik bernama seperti `gyrA_S83L`. Jangan dipotong jadi `gyrA`.

## Hasil yang bisa dicek

- Hitungan manual satu isolat tercatat dan sama dengan keluaran skrip
- `amr_hits_curated.csv` hanya berisi baris AMR, dan kolom `Detection_category` hanya berisi `counted` atau `note`
- Skrip bisa dijalankan ulang dari awal dan menghasilkan file yang sama

## Cek dirimu

1. Apa beda EXACTX dan BLASTX, dan kenapa keduanya sama-sama dihitung 1?
2. Kenapa kategori yang tidak dikenal harus memunculkan peringatan?
3. Hit dengan *identity* 100% tapi *coverage* 55%: masuk kategori apa kemungkinan besar, dan bagaimana kamu menuliskannya?

## Templat log

```
### YYYY-MM-DD (Hari 6)
- **Langkah:** membaca keluaran AMRFinderPlus; menulis curate_hits.py
- **Input:** results/raw_tool_outputs/*_amrfinder.tsv
- **Parameter:** kategori counted = EXACTX, ALLELEX, BLASTX, POINTX; nama kolom versi <...>
- **Hasil / file keluaran:** results/amr_hits_curated.csv; hitungan manual <Sample_ID>: <n> baris AMR, <n> counted, <n> note
- **Kendala dan solusinya:**
- **Pertanyaan yang muncul:**
```

Sebelumnya: [Hari 5](hari-05-amrfinderplus.md) · Berikutnya: [Hari 7](hari-07-matriks.md)
