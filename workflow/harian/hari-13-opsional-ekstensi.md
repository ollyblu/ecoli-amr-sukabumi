# Hari 13 dan seterusnya (opsional): satu ekstensi

Pilih **satu** ekstensi dulu. Masing-masing bisa makan 2 sampai 4 sesi. Gunanya sebagai bahan diskusi saat wawancara iGEM.

## Pilihan

| Ekstensi | Pertanyaan | Tool di Galaxy (per 18 November 2026) | Hasil |
|---|---|---|---|
| B: pembanding | Apakah database lain memberi hasil yang sama? | ABRicate 1.4.0+galaxy1 dengan database CARD | Tabel perbandingan AMRFinderPlus dan ABRicate per isolat |
| C: MLST | Apakah isolat-isolat ini satu klon atau berbeda-beda? | MLST 2.35.0+galaxy0 | *Sequence type* tiap isolat, ditambahkan ke metadata dan figur |
| A: plasmid | Gen AMR mana yang kemungkinan dibawa plasmid? | Lihat PDF panduan bagian Extension A | Daftar gen beserta *contig* dan dugaan lokasinya |

Versi tool bisa berubah. Cek ulang di panel Galaxy dan catat yang benar-benar kamu pakai.

Saran urutan: C paling ringan dan langsung memperkaya figur. B melatih cara membandingkan dua database. A paling sulit karena assembly berlevel *Chromosome* bisa memotong plasmid.

## Langkah umum

- [ ] Tulis aturan analisis ekstensi di `../analysis_notes.md` **sebelum** menjalankan tool, sama seperti Hari 1. Contoh untuk B: kapan hasil dua tool dianggap "sesuai"
- [ ] Jalankan tool dengan setelan yang sama untuk semua isolat yang lolos QC
- [ ] Simpan keluaran mentah di `results/raw_tool_outputs/`
- [ ] Tulis atau perluas skrip untuk merangkum hasil
- [ ] Tambahkan satu subbagian di laporan dan README
- [ ] Isi log, commit

## Cek dirimu

1. B: kalau ABRicate menemukan gen yang tidak ditemukan AMRFinderPlus, apa saja kemungkinan penyebabnya?
2. C: kalau dua isolat dari inang berbeda punya *sequence type* sama, apa yang boleh dan tidak boleh kamu simpulkan?
3. A: kenapa level assembly membatasi kesimpulan tentang plasmid?

## Templat log

```
### YYYY-MM-DD (Hari 13+, Extension <B/C/A>)
- **Langkah:**
- **Input:**
- **Parameter:** <tool> <versi>, database <versi>
- **Hasil / file keluaran:**
- **Kendala dan solusinya:**
- **Pertanyaan yang muncul:**
```

Sebelumnya: [Hari 12](hari-12-opsional-notebook.md) · Kembali ke [daftar hari](README.md)
