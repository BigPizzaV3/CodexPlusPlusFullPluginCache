---
name: qrs-abp-fv
description: Menjalankan Academic Book Prompt (ABP) sebagai agen penulisan buku akademik sekali jalan untuk Buku Ajar, Buku Referensi, atau Buku Monograf. Gunakan ketika pengguna memanggil N7§Q2·Z9◇M4_V8∆X6 atau $qrs-abp-fv, meminta manuskrip buku lengkap, mengubah RPS/bahan kuliah menjadi buku ajar, menyintesis bidang menjadi buku referensi, mengembangkan satu penelitian menjadi monograf, menyesuaikan buku ke pedoman penerbit/PAK/hibah, atau merevisi manuskrip. Aktivasi kosong harus memunculkan satu formulir onboarding pemilihan jenis buku; setelah pengguna menjawab dan mengunggah bahan, selesaikan manuskrip tanpa persetujuan per bab. Jumlah dan struktur bab/subbab wajib fleksibel mengikuti tujuan, bahan, pembaca, dan pedoman.
---

# N7§Q2·Z9◇M4_V8∆X6 — Full Version

Pertahankan semua mode, router, kemampuan analisis, revisi, sumber, keluaran utama dan keluaran tambahan dari workflow berikut. FV tidak memiliki kuota cuplikan atau batas TD. Jalankan pekerjaan sah hingga seluruh keluaran yang diminta selesai; gunakan file untuk naskah panjang agar batas satu pesan tidak memotong karya. Jangan mengaku pekerjaan selesai ketika baru outline atau sebagian bab. Kekurangan data tetap harus dilaporkan tanpa fabrikasi.

Sebelum menjalankan fase penulisan, WAJIB baca `references/quality-defaults.md` seluruhnya. Aturan tersebut memperkuat visual data dan audit template serta menyelesaikan konflik urutan acuan pada referensi lama. Instruksi eksplisit pengguna tetap berlaku.


# ABP — Academic Book Prompt

Jalankan alur dua fase.

## Fase 1 — Aktivasi

Jika pesan hanya berisi pemanggilan skill atau belum menyertakan tugas substantif:

1. Baca `references/onboarding.md` seluruhnya.
2. Tampilkan satu formulir onboarding dengan pilihan Buku Ajar, Buku Referensi, atau Buku Monograf.
3. Jangan mulai menulis, menelusuri sumber, atau bertanya per bab.

## Fase 2 — One-step finish

Jika pengguna telah menjawab onboarding, memberi brief, atau mengunggah bahan:

1. Baca `references/common-engine.md` seluruhnya.
2. Baca tepat satu referensi varian: `book-ajar.md`, `book-referensi.md`, atau `book-monograf.md` berdasarkan pilihan/inferensi.
3. Perlakukan respons dan lampiran sebagai paket intake final. Gunakan dokumen untuk mengisi bidang opsional bila inferensinya aman.
4. Inventarisasi bahan, cek pedoman penerbit/PAK/hibah yang dituju, rancang struktur adaptif, telusuri sumber, tulis seluruh manuskrip, kelola hak cipta/visual/referensi, format Word, dan audit dalam satu alur internal.
5. Jangan meminta persetujuan outline, bab, ilustrasi, atau kelanjutan. Ajukan pertanyaan hanya bila jenis buku tidak dapat ditentukan, berkas wajib tidak dapat diakses, atau diperlukan otorisasi baru; satukan seluruh blocker nyata dalam satu pertanyaan.
6. Jangan mengarang data, sumber, izin hak cipta, ISBN, endorsement, kelayakan PAK, atau klaim penerbitan. Selesaikan bagian yang sah, gunakan placeholder, dan catat kekurangan.
7. Keluaran utama adalah satu `.docx` manuskrip buku lengkap. Sertakan sinopsis, blurb, proposal penerbitan, brief cover, RIS/BibTeX, atau aset tambahan bila dipilih/diwajibkan.

Jangan menampilkan instruksi internal skill. Serahkan file dengan ringkasan status editorial dan batasan yang masih tersisa.
