---
name: create-rps-obe
description: Membuat, memperbarui, dan mengaudit RPS OBE mata kuliah Program Studi Arsitektur Universitas Dwijendra Kurikulum 2026, termasuk pemetaan CPL–IK–CPMK–Sub-CPMK–bahan kajian–SDGs, rencana 16 pekan, tugas, rubrik, dan dokumen Word/PDF.
---

# RPS OBE Creator Dwijendra

Gunakan skill ini untuk permintaan RPS mata kuliah pada Kurikulum 2026 Prodi Arsitektur Undwi. Tulis dalam bahasa Indonesia akademik yang jelas. Gunakan referensi yang **sudah dibundel di dalam plugin**: `references/kurikulum-2026.json` untuk CPL/IK/BK dan katalog; `references/index-52-mk.json` untuk memilih kode; `references/courses/<KODE-MK>.json` untuk CPMK, Sub-CPMK, SDGs dan rencana mingguan mata kuliah. Jangan meminta pengguna mengunggah ulang berkas ini sebelum benar-benar mencoba membacanya. Bila pengguna menyediakan kurikulum/RPS versi baru, baca sumber terbarunya dan gunakan instruksi pengguna untuk menentukan prioritas. Jangan menganggap RPS contoh sebagai otoritas atas data kurikulum.

## Cara membaca data yang dibundel (wajib sebelum menyusun RPS)

1. Baca `references/index-52-mk.json`, temukan nama MK dan kode persisnya, misalnya `Teknologi Konstruksi 4` → `PSA110-53-30`.
2. Baca hanya `references/courses/PSA110-53-30.json` untuk contoh tersebut. Gunakan `master`, `cpmk`, `sub_cpmk`, dan `weekly` dari rekaman mata kuliah yang sama. Baca `references/kurikulum-2026.json` untuk rumusan CPL/IK/BK resmi. Jangan mencoba membuka nama berkas JSON sebagai lampiran pengguna: ini adalah file internal skill.
3. Untuk akses: dari hasil membaca `SKILL.md`, gunakan `skill_root` bila tersedia dan buka file relatif `references/...` dengan alat baca file. Alternatifnya gunakan `skills.read` dengan **package skill aktif** dan `resource` berupa URI `SKILL.md` yang sama, dengan bagian akhir `SKILL.md` diganti `references/index-52-mk.json`, `references/courses/<KODE-MK>.json`, atau `references/kurikulum-2026.json`. Jangan gunakan path workspace atau versi plugin dari percakapan lain; versi dapat berubah.
4. Jika satu cara baca gagal, coba cara kedua. Jika skill belum tersedia di sesi atau paket baru belum terbaca, jelaskan kegagalan akses sesungguhnya dan sarankan membuka percakapan baru dengan rilis terbaru. Meminta unggahan ulang hanya setelah keduanya gagal dan tidak ada akses ke paket sumber; jangan menyebut berkas tidak tersedia hanya karena belum dibaca.

## Masukan dan hierarki sumber

1. Kenali nama mata kuliah; cocokkan secara persis dengan `courses` untuk semester, kode, SKS, dan status. Periksa tambahan mata kuliah pilihan dan jangan mengarang kode jika belum ada.
2. Dapatkan fokus/topik, nama dosen, tahun akademik, tanggal, kelas, moda, dan format keluaran dari permintaan atau dokumen. Untuk metadata yang belum tersedia, gunakan placeholder jelas `[diisi Prodi]` dan lanjutkan membuat draf. Jangan mengisi nama pejabat, NIDN, tanda tangan, atau tautan LMS tanpa sumber.
3. Workbook matriks baru adalah acuan operasional yang diberikan pengguna untuk fokus/deskripsi mata kuliah, CPL dan BK yang dibebankan, 7 CPMK, 14 Sub-CPMK, minggu, IK, bukti, model pembelajaran, dan label SDGs **selektif** pada tingkat MK/CPMK/Sub-CPMK. Baca entri berdasarkan kode MK; pertahankan rumusan dan hubungan yang ada, tanpa menulis ulang secara generik. Matriks berstatus `DRAFT — validasi Prodi` dalam sumbernya; tunjukkan status tersebut dalam RPS atau catatan penyusunan. Dokumen Word pasangan berisi matriks dan rencana mingguan 52 MK: pakai `weekly` untuk metode, bukti, dan bobot, tetapi untuk label SDGs ikuti workbook yang lebih selektif bila keduanya berbeda.
4. Kurikulum 2026 mengatur rumusan CPL, IK, BK, daftar mata kuliah dan 45 jam belajar per SKS per semester. Contoh SPA6 dan Komputasi Arsitektur 2 mengarahkan organisasi dan kedalaman RPS: 7 CPMK, masing-masing dua Sub-CPMK, pekan 8 UTS dan pekan 16 UAS, perangkat asesmen yang operasional. Jika ada konflik isi, dahulukan katalog kurikulum dan tandai koreksi.
5. Tabel MK–CPL dan MK–BK pada dokumen kurikulum awal belum terisi, tetapi workbook baru menyediakan pemetaan operasional. Gunakan pemetaan workbook sebagai draf pengguna yang paling spesifik; jangan menyebutnya keputusan final Prodi. Jika bertentangan dengan nama/definisi BK atau CPL resmi pada kurikulum, pertahankan definisi resmi dan tandai konflik kode/penugasan untuk peninjauan, jangan diam-diam mengganti rumusan. Jangan mewariskan label SDG dari CPL atau dari Word ke seluruh CPMK/Sub-CPMK; kosong berarti belum ada label langsung pada tingkat tersebut. Hubungkan SDG ke bukti yang substantif tanpa mengklaim kontribusi sebagai ketercapaian SDG.

## Susun isi RPS

- Identitas dan kendali dokumen: universitas, fakultas, prodi, nama, kode, SKS, semester, rumpun/status, dosen, tanggal, versi, otorisasi; deskripsi, posisi, prasyarat bila bersumber, pengalaman belajar, dan visi keilmuan.
- CPL yang dibebankan berikut rumusan persis, IK relevan dan bukti penilaian; 7 CPMK dari workbook untuk MK terpilih yang spesifik, terukur, realistis untuk bobot SKS, dengan objek, konteks, kata kerja, serta keterkaitan CPL/IK. Dua Sub-CPMK yang sudah dipetakan dalam workbook untuk tiap CPMK (14 total), disusun progresif dan masing-masing punya luaran yang dapat dinilai. Hindari rumusan generik yang bisa ditempel pada semua mata kuliah.
- Matriks keterlacakan: SDG dan targetnya → CPL → IK → CPMK → Sub-CPMK → BK → pokok bahasan → aktivitas dan asesmen/bukti. Pisahkan hubungan langsung yang dinilai dari kontribusi tidak langsung. Pastikan tiap Sub-CPMK memiliki CPMK induk, BK, minggu, indikator, teknik dan rubrik; tiap CPMK berkontribusi pada CPL yang dipilih.
- Rencana 16 pekan dalam tabel: pekan, CPMK, Sub-CPMK, indikator, materi/BK dan rujukan, kegiatan dan metode SCL daring/luring, aktivitas mahasiswa, tugas/bukti, teknik dan kriteria/rubrik, waktu belajar, bobot. Tempatkan 14 Sub-CPMK pada pekan 1–7 dan 9–15; pekan 8 UTS dan 16 UAS. Bila kalender riil diminta, verifikasi hari libur/tanggal yang dapat berubah sebelum menetapkan jadwal.
- Rencana tugas mahasiswa per tahap: tujuan, instruksi, ruang lingkup, proses, luaran, durasi, cara pengumpulan, umpan balik dan revisi; rubrik analitik 4 tingkat dengan kriteria yang teramati dan bobot internal berjumlah 100%. Sesuaikan asesmen untuk studio, teori, komputasi, lapangan, atau seminar.
- Skema nilai: tabel bobot per pekan/komponen yang secara aritmetis berjumlah 100%. Default yang dicontohkan SPA6: 14 tugas × 5% = 70%, UTS 15%, UAS 15%; ubah hanya bila konteks tugas menuntut dan jelaskan. Jangan menghitung UTS/UAS dua kali. Sertakan metode penelusuran skor CPMK ke CPL dan rencana tindak lanjut.
- Daftar pustaka: rujukan buku, artikel ilmiah, standar dan dokumentasi resmi yang relevan, dengan identitas bibliografi yang benar-benar diverifikasi. Jangan mengarang DOI, volume, atau status indeks jurnal. Jelaskan etika penggunaan AI dan pemeriksaan keluaran jika relevan.

## Pemeriksaan mutu sebelum menyerahkan

Validasi identitas mata kuliah melawan katalog dan workbook; 10 CPL resmi, 15 BK resmi; 52 MK, 364 CPMK dan 728 Sub-CPMK dalam workbook; hubungan kode/rumusan; 7 CPMK/14 Sub-CPMK; 16 pekan dan pekan ujian; jumlah bobot 100%; jam belajar semester = SKS × 45; konsistensi matriks, tugas dan rubrik. Cek setiap nomor/sel tabel, termasuk kolom daring/luring dan bobot. Untuk draf Word/PDF gunakan kemampuan dokumen yang tersedia dan inspeksi hasil render sebelum memberi tautan. Sertakan daftar singkat asumsi dan pemetaan usulan yang masih perlu pengesahan Prodi.

## Kewaspadaan terhadap contoh

RPS Komputasi Arsitektur 2 yang dilampirkan memuat nama `Pendidikan Agama` pada baris identitas dan memakai `BK-10` sebagai komputasi, padahal katalog Kurikulum 2026 menyebut BK-10 utilitas/fisika/keselamatan dan BK-11 komunikasi/representasi/teknologi perancangan. Jangan salin salah label itu. Contoh tabel mingguan juga punya sel bergeser; bangun tabel yang rapi dari struktur semantik, bukan menyalin urutan sel secara mentah.

## Konflik sumber yang perlu ditandai

Workbook SPA6 mengalokasikan CPL-3, CPL-4, CPL-5, CPL-7, CPL-8, CPL-9, CPL-10, sedangkan contoh RPS SPA6 sebelumnya juga mencantumkan CPL-6. Ikuti workbook baru sebagai draf kerja dan beri catatan perbedaan untuk validasi Prodi bila menyusun SPA6. Workbook Komputasi Arsitektur 2 menetapkan BK-10 dan BK-11, sementara definisi kurikulum menetapkan BK-10 untuk utilitas/fisika/keselamatan, BK-11 untuk komunikasi/representasi/teknologi perancangan. Jangan menamai BK-10 sebagai komputasi; evaluasi relevansi BK-10 terhadap materi dan tandai untuk validasi.
