# GİB özelge araştırması

Vergi konusundaki idari görüş veya belirli bir özelge gerektiğinde bu akışı kullan.
Özelgeyi içtihat veya mahkeme kararı olarak sınıflandırma. Genel değerlendirmede
önce ilgili mevzuatı incele; yalnız özelge bulma talebini genişletme.

1. Vergi türünü, işlemi ve gerekiyorsa dönemi belirle. Sonucu değiştiren bilgi
   eksikse tek soru sor; cevaba bağlı uygulama değerlendirmesini beklet.
2. Ana skill'in anonimleştirme kuralını bütün araç girdilerine uygula;
   `gib_ozelge_ara` aracını kimliksiz bir `sorgu` ile çağır. Özel olayı
   ayırt eden ayrıntıları taşımak yerine hukuki işlem ve vergi kavramlarını kullan.
   GİB sorgudaki her kelimenin özelgede geçmesini ister ve VEYA araması yoktur;
   kelime ekledikçe sonuç sıfıra iner. Sorunun özünü 2-3 temel vergi kavramına
   indir: "binek otomobil KDV indirim", "kira geliri istisna". Soru cümlesi, soru
   kelimesi (nasıl, mı, nedir), noktalama ve kesme ekini (GVK'nın yerine GVK) yazma.
   Tam ifade için yalnız tek bir tırnaklı ifade kullan; yanına kelime eklersen
   sonuç sıfır olur. Sonuç yoksa kelime sayısını azaltıp bir kez daha dene.
   Parametreleri mevcut araç şemasından doğrula; desteklenmeyen filtre uydurma.
3. Adayın kurum, başlık, tarih, numara ve kaynak bağlantısını incele. İlgili
   olanı `id` değeriyle `belge_getir` üzerinden oku. `next_page` varsa ilgili
   olay, gerekçe ve sonuç tamamlanana kadar gereken sayfalara devam et.
4. Özelgedeki olay ile kullanıcının olayı arasındaki farkları belirt. Görüşü
   otomatik olarak herkese uygulanacak hüküm diye sunma. Yargı kararı gerekiyorsa
   ana akıştan ayrıca uygun içtihat alt akışına geç.
5. Bulguyu özelge numarası, kaynak tarihi, kurum ve bağlantıyla aktar. Belgenin
   kalıcı arşivde bulunması görüşün güncel mevzuatla uyumlu olduğunu tek başına
   kanıtlamaz. Yeterli kanıt elde edilince dur.

Boş arama ile erişim/okunamama hatasını ayır. Yoğunluk/kota yanıtında verilen
bekleme bilgisini uygula; yeni bir gerekçe olmadan aynı çağrıyı tekrarlama.
