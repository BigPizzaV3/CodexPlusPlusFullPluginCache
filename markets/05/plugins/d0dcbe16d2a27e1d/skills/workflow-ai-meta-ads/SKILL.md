---
name: workflow-ai-meta-ads
description: Mengurus workflow penuh Meta Ads apabila user mahu merancang, menyediakan, atau melancarkan iklan Conversion, WhatsApp Leads, atau Awareness menggunakan Meta MCP yang telah disambungkan.
---

# Workflow AI Meta Ads

Gunakan skill ini sebagai workflow utama. Ia menyelaraskan `Copywriting Skill`, `Poster Design Skill`, penjanaan creative, media bridge jika diperlukan, dan Meta MCP.

Skill ini perlu dicetuskan secara automatik apabila user menggunakan bahasa biasa seperti `launch ads`, `buat iklan Meta`, `sediakan kempen WhatsApp`, atau meminta copy, poster, dan setup Meta Ads dalam satu workflow. User tidak perlu menaip nama skill atau simbol `$`.

## Kebergantungan Tool

- Gunakan tool image generation atau design yang tersedia untuk menghasilkan creative sebenar.
- Gunakan Meta MCP yang telah disambungkan oleh user untuk operasi Meta Ads.
- Gunakan Cloudinary atau Netlify yang telah disambungkan hanya apabila URL media awam benar-benar diperlukan.
- Jika Meta MCP tidak tersedia, teruskan bahagian strategy, copy, dan creative yang boleh disiapkan, kemudian beritahu dengan jelas bahawa setup atau launch Meta belum dilakukan. Jangan mendakwa campaign telah diwujudkan atau dilancarkan.

## Skop V1

Sokong hanya tiga jenis kempen:

- **Conversion** — menghantar orang ke destinasi conversion yang boleh diukur.
- **WhatsApp Leads** — memulakan perbualan WhatsApp untuk lead.
- **Awareness** — membina reach atau awareness tanpa menjanjikan conversion.

Jika user meminta jenis lain, terangkan bahawa V1 belum menyokongnya dan jangan menyamar sebagai salah satu jenis di atas.

## Peraturan Utama

- Semak conversation, fail, aset, dan tool yang tersedia sebelum bertanya soalan.
- Jangan tanya maklumat yang boleh diambil dengan selamat melalui tool read-only.
- Tanya hanya maklumat kritikal yang benar-benar mengubah setup atau kebenaran untuk spend.
- Jangan reka fakta produk, testimoni, harga, diskaun, tarikh, claim, tracking event, audience, ID aset, atau capability tool.
- Jangan minta atau simpan credential dalam skill atau chat. Gunakan connection yang telah disediakan oleh student.
- Jangan aktifkan delivery atau spend tanpa approval jelas selepas final summary.
- Kekalkan semua campaign, ad set, creative, dan ad dalam keadaan tidak aktif sebelum approval, jika objek perlu diwujudkan untuk validation.
- Gunakan Cloudinary atau Netlify hanya sebagai media bridge apabila Meta MCP memerlukan URL awam. Jangan jadikannya langkah wajib.

## Workflow

### 1. Fahami arahan

Kenal pasti:

- apa yang diiklankan;
- matlamat bisnes;
- destinasi selepas klik atau tindakan yang dikehendaki;
- market, bahasa, dan audience;
- offer dan fakta yang boleh dibuktikan;
- aset brand dan creative yang tersedia;
- budget, tempoh, dan batas spend.

Jika jenis kempen belum disebut, cadangkan satu daripada tiga jenis V1 berdasarkan matlamat:

- jualan atau tindakan di website/app → **Conversion**;
- prospek perlu chat dengan team → **WhatsApp Leads**;
- reach, recall, atau pengenalan brand → **Awareness**.

Jelaskan cadangan secara ringkas dan minta keputusan hanya jika pilihan itu tidak boleh dibuat dengan yakin daripada matlamat user.

### 2. Periksa context dan aset melalui tool

Gunakan operasi read-only yang tersedia untuk menyemak, jika relevan:

- Meta ad account dan mata wang;
- Facebook Page dan identiti Instagram;
- Pixel/dataset dan conversion event untuk Conversion;
- akaun atau nombor WhatsApp yang tersedia untuk WhatsApp Leads;
- creative sedia ada, logo, brand guide, landing page, dan URL;
- timezone account dan sebarang batas platform yang boleh dibaca.

Jika beberapa aset hampir sama tersedia dan pilihan memberi kesan material, tunjuk pilihan ringkas kepada user. Jangan pilih ad account, Page, Pixel, WhatsApp destination, atau identiti secara rawak.

### 3. Tanya hanya jurang kritikal

Maklumat umum yang biasanya mesti jelas sebelum final setup:

- jenis kempen atau matlamat yang cukup jelas untuk memilihnya;
- produk/offer dan fakta utama;
- destinasi kempen;
- lokasi, bahasa, dan audience yang dituju;
- budget beserta unitnya, jadual, dan timezone;
- identiti brand yang akan digunakan;
- approval terhadap claim sensitif atau fakta yang tidak boleh disahkan.

Keperluan tambahan mengikut jenis:

- **Conversion:** URL/destinasi, Pixel/dataset, conversion event, dan kaedah tracking yang benar-benar tersedia.
- **WhatsApp Leads:** WhatsApp destination yang betul, tujuan perbualan, dan siapa yang akan mengendalikan lead.
- **Awareness:** market, mesej utama yang mahu diingati, serta reach/awareness intent.

Gabungkan soalan dalam satu kumpulan pendek. Jangan tanya preference kecil yang boleh diselesaikan dengan cadangan profesional dan ditunjukkan dalam final summary.

### 4. Bentuk strategi ringkas

Tentukan:

- satu matlamat utama;
- satu audience utama bagi setiap ad set yang dicadangkan;
- satu offer atau mesej utama;
- angle copy yang paling sesuai;
- format creative yang sesuai dengan placements yang dirancang.

Elakkan mencampurkan terlalu banyak matlamat, angle, atau offer dalam satu ad.

### 5. Gunakan Copywriting Skill Coach Adam

Baca dan ikuti `../copywriting-skill-coach-adam/SKILL.md` jika fail sibling itu tersedia. Berikan brief yang telah disahkan. Minta output sekurang-kurangnya:

- chosen angle dan sebab;
- copy akhir dalam susunan Hook → Exaggeration → Intro Product/Service → USP → Benefit → Offer → CTA;
- headline;
- description jika diperlukan;
- CTA recommendation;
- poster message hierarchy;
- elemen yang dibuang kerana maklumat tidak tersedia;
- fact-check notes.

Copy mesti berasaskan fakta yang diberi atau disahkan, menggunakan bahasa ICP, dan dipecahkan kepada baris pendek untuk bacaan mobile. Jangan paksa USP atau Offer jika maklumat itu tiada.

### 6. Gunakan Poster Design Skill Coach Adam dan hasilkan creative

Baca dan ikuti `../poster-design-skill-coach-adam/SKILL.md` jika fail sibling itu tersedia. Hantar ICP, chosen angle, approved facts, brand assets, copy akhir, Hook, message hierarchy, serta placements yang dirancang.

Poster mesti menterjemahkan emosi dan visual story angle yang dipilih. Dream mesti menunjukkan desired outcome; Pain/Problem mesti menunjukkan simptom atau akibat; Educate mesti menunjukkan satu insight tanpa menjadi infographic. Jangan menampal seluruh primary text pada artwork.

Hasilkan creative dalam workflow semasa menggunakan tool imej/design yang tersedia. Pilih satu konsep dan satu focal point. Jangan hanya menulis prompt dan menganggap poster telah siap. Semak hasil secara visual sebelum meneruskan.

Jika imej mengandungi teks yang rosak, anatomi pelik, fakta salah, logo berubah, atau hierarchy lemah, baiki atau hasilkan semula sebelum setup Meta.

### 7. Sediakan media untuk Meta hanya jika perlu

Utamakan upload terus melalui Meta MCP jika disokong.

Jika Meta MCP memerlukan URL media awam:

1. gunakan Cloudinary atau Netlify yang sudah disambungkan;
2. upload hanya fail creative yang diperlukan;
3. sahkan URL boleh dicapai dan memulangkan jenis fail yang betul;
4. jangan upload credential, fail kerja dalaman, atau data customer;
5. rekod URL media dalam final summary.

### 8. Petakan Meta MCP tanpa mereka-reka tool

Periksa capability dan dokumentasi tool yang benar-benar tersedia. Petakan hanya operasi yang boleh disahkan untuk:

- memilih ad account dan identiti;
- menyediakan campaign;
- menyediakan ad set;
- upload atau mendaftar creative;
- menyediakan ad;
- membaca semula status dan konfigurasi;
- mengaktifkan/publish selepas approval.

Jangan cipta nama function, parameter, enum, atau urutan API. Jika tool tidak menerangkan perbezaan antara create, publish, dan activate; jika status delivery tidak jelas; atau jika mapping aset tidak dapat dipastikan, berhenti sebelum mutation dan minta:

- nama/versi Meta MCP;
- SOP atau panduan tool yang digunakan;
- contoh urutan tool yang sah, jika ada.

### 9. Sediakan setup tanpa spend

Sediakan pelan konfigurasi penuh dahulu. Jika Meta MCP membenarkan objek draft/paused yang dijamin tidak deliver, objek itu boleh diwujudkan untuk validation. Jika jaminan tersebut tidak jelas, kekalkan sebagai pelan sahaja sehingga approval.

Jangan gunakan status aktif secara default. Jangan publish sekadar untuk menguji.

### 10. Validate

Semak sebelum meminta approval:

- jenis kempen sepadan dengan matlamat;
- ad account, Page/Instagram identity, dan destinasi betul;
- Pixel/dataset dan event betul untuk Conversion;
- WhatsApp destination betul untuk WhatsApp Leads;
- budget, jenis budget, tarikh, timezone, dan mata wang jelas;
- audience, lokasi, bahasa, exclusions, dan placements tidak bercanggah;
- URL dan tracking yang digunakan boleh dicapai;
- copy dan poster menggunakan angle yang sama;
- claim, harga, offer, testimoni, dan tarikh datang daripada fakta yang diluluskan;
- creative sesuai dengan placements dan tiada kerosakan visual;
- semua objek pra-approval tidak deliver dan tidak spend;
- tiada credential atau data sensitif dimasukkan.

Jika validation gagal, baiki perkara yang selamat atau minta maklumat yang benar-benar diperlukan. Jangan minta approval atas setup yang belum konsisten.

### 11. Tunjukkan final summary

Tunjukkan dalam bahasa mudah:

- Campaign type dan matlamat
- Ad account dan identiti
- Audience, lokasi, bahasa
- Budget, jadual, timezone, mata wang
- Destination/tracking
- Chosen angle
- Copy akhir
- Creative akhir atau preview
- Placements/format
- Aset Meta yang akan digunakan
- Media bridge URL, hanya jika digunakan
- Perubahan yang akan berlaku selepas approval

Sebut jumlah atau batas spend dengan jelas. Jangan sembunyikan default penting.

### 12. Minta explicit approval

Gunakan soalan yang mengikat approval kepada setup yang baru diringkaskan, contohnya:

> Saya sedia untuk publish dan aktifkan setup di atas dengan budget RM___ bagi tempoh ___. Balas **APPROVE LAUNCH** untuk teruskan, atau beritahu apa yang mahu diubah.

Jawapan umum seperti “ok”, “teruskan fikir”, atau approval lama untuk versi lain tidak cukup jika budget, audience, creative, destination, atau jadual telah berubah secara material.

### 13. Launch selepas approval

Selepas menerima explicit approval:

1. gunakan operasi Meta MCP yang telah disahkan;
2. create/publish/activate mengikut SOP MCP sebenar;
3. baca semula campaign, ad set, creative, dan ad;
4. sahkan status sebenar tanpa menganggap tool call berjaya;
5. laporkan ID/nama, status, budget, jadual, dan sebarang warning.

Jika sebahagian operasi gagal, hentikan retry yang boleh menghasilkan duplicate atau spend berganda. Semak state semasa dahulu, kemudian laporkan kegagalan dan tindakan paling selamat.

## Definisi Selesai

Workflow selesai hanya apabila salah satu berlaku:

- selepas approval, setup berjaya dilancarkan dan status dibaca semula; atau
- terdapat blocker yang jelas, tiada spend tidak sengaja berlaku, dan user diberitahu tepat apa yang diperlukan untuk meneruskan.
