---
name: auto-submit-ojs
description: "Mengendalikan browser secara aman untuk membantu penulis membuat akun OJS, melengkapi profil, submit artikel baru beserta file pendukung, serta resubmit revisi atau response to reviewers. Gunakan ketika pengguna menyebut OJS, auto submit jurnal, registrasi jurnal, submit manuskrip, resubmit revisi, upload revision, atau meminta tindakan langsung pada portal jurnal. Jangan gunakan untuk sekadar mencari jurnal, menulis atau menilai artikel, menghubungi editor di luar alur OJS, maupun menjamin penerimaan."
---

# Auto Submit OJS

Jalankan tindakan OJS melalui browser yang disetujui host. Perlakukan setiap portal sebagai instalasi yang dapat memiliki versi, tema, label, bahasa, plugin, dan persyaratan berbeda.

## Mode aktivasi

Jika dipanggil tanpa tugas substantif, baca dan tampilkan hanya [formulir-input.md](references/formulir-input.md). Jangan membuka situs atau membuat akun.

Jika pengguna sudah memberikan tujuan, URL OJS, dan berkas atau metadata yang cukup, lanjutkan dari tahap yang relevan tanpa mengulang pertanyaan yang sudah terjawab. Kelompokkan hanya kekurangan kritis dalam satu pertanyaan singkat.

## Persiapan browser

Gunakan tool browser-control resmi yang tersedia pada host. Pada ChatGPT/Codex, baca dan ikuti skill `control-browser` sebelum interaksi browser. Jangan mengganti tool resmi dengan skrip browser mandiri, meminta kata sandi di chat, mengekspor cookie, atau menyimpan kredensial dalam file/log.

Minta pengguna masuk melalui pengambilalihan browser yang aman ketika login diperlukan. Serahkan CAPTCHA, 2FA, OTP, tautan verifikasi email, dan tantangan keamanan kepada pengguna. Pada cloud browser ChatGPT, jangan menawarkan atau memulai passkey/WebAuthn; gunakan password, SSO, atau kode email yang didukung dan laporkan blocker bila passkey adalah satu-satunya pilihan. Jangan mencoba melewati mekanisme keamanan.

## Kontrak eksekusi

1. Tentukan mode: `REGISTRASI`, `SUBMISSION_BARU`, `RESUBMISSION_REVISI`, atau gabungan berurutan.
2. Validasi URL, domain jurnal, tujuan pengguna, file yang tersedia, dan otorisasi tindakan final.
3. Buka situs dan petakan elemen berdasarkan teks/role/label yang terlihat, bukan selector rapuh atau asumsi versi.
4. Ikuti [alur-ojs.md](references/alur-ojs.md) untuk mode yang dipilih.
5. Isi hanya data yang berasal dari pengguna, file, atau halaman jurnal. Jangan mengarang metadata, afiliasi, ORCID, penulis, konflik kepentingan, pendanaan, kata kunci, abstrak, ataupun jawaban checklist.
6. Simpan progres/draf pada OJS bila aman dan tersedia. Setelah setiap perpindahan tahap, periksa pesan sukses, daftar file, dan metadata yang tampil.
7. Jalankan pemeriksaan prafinal pada [keselamatan-dan-laporan.md](references/keselamatan-dan-laporan.md).
8. Klik tindakan final hanya jika sudah diotorisasi secara eksplisit untuk submission yang tepat dan tidak ada deklarasi pribadi yang belum dikonfirmasi.
9. Verifikasi hasil dari halaman konfirmasi/dashboard; catat ID submission, judul, jurnal, waktu, file, dan status hanya jika benar-benar terlihat.
10. Tampilkan laporan akhir sesuai format referensi. Bedakan `SELESAI`, `DRAF TERSIMPAN`, `MENUNGGU PENGGUNA`, `TERBLOKIR`, dan `TIDAK DIDUKUNG`.

## Gerbang pertanyaan kritis

Berhenti dan tanyakan satu pertanyaan terfokus hanya jika diperlukan:

- login, verifikasi akun, CAPTCHA, 2FA, OTP, atau persetujuan akses browser;
- URL/domain, jurnal tujuan, mode, atau submission revisi yang masih ambigu;
- metadata wajib atau file wajib belum tersedia;
- urutan/identitas kontributor, corresponding author, section, bahasa, atau tipe komponen file tidak pasti;
- checklist berisi pernyataan hukum/etik/faktual yang belum dikonfirmasi pengguna;
- tombol final belum diotorisasi, kecuali permintaan awal jelas menyatakan submit/resubmit sampai selesai;
- situs meminta pembayaran, perjanjian lisensi, pengalihan hak cipta, tanda tangan, atau tindakan di luar cakupan;
- terdapat risiko duplikasi submission atau domain/akun tidak sesuai.

Lanjutkan semua pekerjaan yang tidak terblokir terlebih dahulu. Jangan meminta konfirmasi kosmetik atau mengulang data yang sudah ada.

## Batas tindakan

- Jangan menyetujui originalitas, larangan simultaneous submission, authorship, etika, konflik kepentingan, lisensi, copyright transfer, biaya, atau kebijakan atas nama pengguna tanpa konfirmasi eksplisitnya.
- Jangan melakukan pembayaran, menandatangani, menghapus submission/file, menarik artikel, mengirim pesan bebas kepada editor, atau mengganti metadata ilmiah tanpa instruksi eksplisit.
- Jangan memilih jurnal atau section secara spekulatif; tampilkan pilihan bila materi tidak menentukan satu jawaban.
- Jangan mengunggah manuskrip yang jelas salah versi atau mengandung kredensial/rahasia yang tidak diperlukan.
- Jangan mengklaim submission sukses tanpa halaman konfirmasi atau status dashboard yang memadai.
- Jangan menjanjikan artikel diterima, diproses editor, atau bebas desk rejection.
- Jangan mencoba mengakali pembatasan situs, rate limit, CAPTCHA, robots, atau kebijakan jurnal.

## Penanganan kendala

Jika tool browser tidak tersedia, laporkan bahwa otomasi belum dapat dijalankan dan berikan checklist data/berkas yang sudah siap; jangan mengaku telah membuka atau mengirim submission. Jika sesi terputus, inspeksi dashboard setelah tersambung kembali sebelum mengulangi klik agar tidak terjadi duplikasi. Jika situs berubah atau selector gagal, ambil ulang struktur halaman dan lanjutkan berdasarkan elemen yang terlihat.

## Kontrak hasil, validasi, dan portabilitas

Jalankan alur one-step secara end-to-end dari intake lengkap hingga selesai atau hingga satu blocker kritis. Hasil akhir/deliverable wajib berupa tindakan OJS yang benar-benar terverifikasi dan laporan status, bukan sekadar rencana. Batasi pertanyaan pada kredensial atau hal krusial/material yang mengubah hasil.

Perlakukan tindakan destructive, irreversible, financial, atau high-risk sebagai gerbang izin eksplisit. Preserve user data dan unrelated work: jangan menimpa berkas sumber, menghapus file, atau mengubah submission lain. Verify setiap output dari halaman OJS dan do not claim success without verification. Untuk simulasi, cakup skenario credential blocker dan tool unavailable tanpa tindakan eksternal nyata.

Portable core ini menggunakan format Agent Skills dengan `SKILL.md` dan resource relatif. Do not promise automatic installation pada semua host. Host lain dapat require manual adaptation untuk tool browser, jalur impor, metadata, dan izin situs; kompatibilitas hanya boleh diklaim setelah dibuktikan pada host tersebut.

## Sumber operasional

Gunakan halaman `Author Guidelines`, `Submission Preparation Checklist`, `Privacy Statement`, dan instruksi yang tampil pada jurnal sebagai sumber utama untuk field jurnal tersebut. Gunakan panduan resmi PKP sebagai pedoman umum; aturan portal jurnal yang sedang dibuka tetap menentukan langkah aktual.
