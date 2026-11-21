---
name: passo-event-discovery
description: Canlı Passo kataloğunda etkinlik bulma, filtreleme, önerme, karşılaştırma ve ayrıntı gösterme iş akışını yürütür. Kullanıcı konser, maç, tiyatro, festival, mekan, sanatçı, organizatör, şehir, tarih, bütçe, ücretsiz etkinlik, bilet fiyatı veya Passo bağlantısı sorduğunda kullan.
---

# Passo etkinlik keşfi

Canlı etkinlik bilgisini yalnızca Passo MCP araçlarından al. Etkinlik, tarih, mekan,
fiyat, müsaitlik veya bağlantı uydurma. Kullanıcının açık talimatları bu skill'deki
varsayımlardan önceliklidir.

Varsayılan olarak Türkçe yanıt ver; kullanıcı başka bir dilde yazarsa o dili kullan.

## Doğru aracı seç

- `find_events` ve `show_events` birlikte kullanılabiliyorsa keşif için `find_events`
  kullan. Filtreleri `filters` nesnesinde gönder. Bu araç kart oluşturmaz; karşılaştırma
  veya seçim için gerektiğinde birden çok veri araması yapabilirsin. Açık kullanıcı
  koşullarını aramalar arasında koru. İlgili sonuçlar seçildikten sonra en çok 8 gerçek
  `event_references[].reference` değerini değiştirmeden `show_events(references=[...])`
  çağrısına gönder. Ayrı aramaların referansları birleştirilebilir.
- `show_events` yalnızca son seçimde, kullanıcı mesajı için bir kez kullanılmalı.
  Sonuç boşsa veya arama hatalıysa kart oluşturma; durumu metinde açıkla. Referansın
  süresi dolmuşsa `find_events` ile veriyi yenile. Referanslardan veri türetme, onları
  metin yanıtına veya dış bağlantılara yazma. Gösterimdeki sıra sonraki “ikincisi” gibi
  ifadelerin referans sırasıdır.
- Bu iki araçtan biri mevcut değilse eski akış için `search_events` kullan.
  Bir kullanıcı mesajı için `search_events` aracını tam bir kez ve tek başına kullan.
  Öncesinde `list_*` çağırma, sonuç boş veya beklenmedik görünse bile aynı turda yeniden
  `search_events` çağırma. Her çağrı ChatGPT transkriptinde kalıcı bir kart oluşturabilir;
  sunucu alaka kontrolünü ve güvenli kategori düzeltmesini tek çağrının içinde yapar.
- `list_cities`, `list_genres`, `list_sub_genres`, `list_organizers` ve `list_venues`
  araçlarını yalnızca kullanıcı katalogda hangi değerlerin bulunduğunu açıkça sorarsa
  kullan.
- `get_event` aracını yalnızca `find_events`, `search_events` veya önceki turdaki gerçek
  sonuçtan gelen tam `id` ile çağır. Kimlik tahmin etme veya bağlantıdan türetme.

## Arama isteğini hazırla

1. Yalnızca kullanıcının verdiği kısıtları çıkar. Şehir, tarih, tür, alt tür, mekan,
   organizatör, bütçe veya ücretsiz olma koşulu eklenmemişse bunları tahmin etme.
2. Takım ve belirli etkinlik adını `name` ile; sanatçı, grup ve serbest ifadeyi `query`
   ile ara.
3. Kısaltmaları çağrıdan önce tam ada çevir. Örnekler: `gs` → `Galatasaray`, `fb` →
   `Fenerbahçe`, `bjk` → `Beşiktaş`, `ts` → `Trabzonspor`, `ist` → `İstanbul`, `ank`
   → `Ankara`, `izm` → `İzmir`, `rams` → `RAMS Park`, `zorlu` → `Zorlu PSM`.
   Tire ve virgülleri boşluğa çevir.
4. Kullanıcı belirli bir takım, sanatçı veya etkinlik adı verdiyse tahmini `genre`
   gönderme; `name` veya `query` daha güvenilirdir. Kullanıcının açıkça belirttiği tür
   ve alt tür koşullarını koru.
5. Kategori açıkça isteniyorsa araç şemasındaki kanonik değeri kullan:
   - tiyatro, stand-up, müzikal, bale, dans, çocuk etkinliği → `Sahne`
   - konser, pop, rock, caz, festival, DJ, klasik müzik → `Müzik`
   - futbol ve lig maçı → `Futbol`
   - basketbol ve diğer sporlar → `Spor`
   - müze ve sergi → `Müze`
   - atölye, sinema, tur, eğitim, seminer, konferans → `Diğer`
6. Futbol isteğini asla `genre="Spor"` ile gönderme. `Futbol` ve `Spor` farklı katalog
   değerleridir.
7. Bugün, yarın, bu hafta, bu hafta sonu, bu ay ve gelecek hafta için sırasıyla
   `today`, `tomorrow`, `this_week`, `this_weekend`, `this_month`, `next_week`
   `date_preset` değerlerini kullan. Açık ama yılsız tarihi sohbet tarihine göre geçmişte
   kalmayan en yakın günle tamamla ve `YYYY-MM-DD` biçiminde gönder. Tek gün için
   `date_from` ve `date_to` aynı olsun.
8. Kullanıcının isteği arama yapmaya yetecek kadar açıksa soru sorma. Yalnızca amaç
   gerçekten belirsizse tek, kısa bir netleştirme sorusu sor.

## İsabetli arama yap

Aramada `search_mode="all"`, `fuzzy=false`, `relevant_only=true` ve
`include_products=false` kullan. Genellikle 8–12 sonuç iste; kullanıcı daha fazlasını
açıkça istemedikçe yüksek limit kullanma.

Eski `search_events` akışında sonuç boşsa aynı turda yeniden arama yapma. Yeni
`find_events` akışında açık koşulları koruyan veri aramaları yapılabilir; boş/hatalı ara
sonuçları `show_events` ile gösterme. Kesin koşulu gevşetmek gerekirse önce kullanıcıya
sor. Kullanıcının kesin koşulunu sessizce kaldırma. Sunucu yalnızca `inferred_filters` içinde açıkça tahmin
olarak işaretlenen `genre` veya `sub_genre` filtresini, kimlik içeren bir aramanın ilk
sayfası boşsa çağrının içinde bir kez kaldırabilir; diğer koşulları korur. Tahmini filtre
eklemekten kaçın. Kullanıcının belirttiği bir koşulu `inferred_filters` içine yazma.
`recovery_attempted` denemenin yapıldığını, `recovered` sonuç bulunduğunu belirtir.
`relaxed_filters` doluysa kaldırılan tahmini koşulları yanıtta açıkla; sonraki sayfada
bu koşulları yeniden ekleme.

Örnek: “Tan Taşçı konserleri” için `query="Tan Taşçı", genre="Müzik"` gönder;
tahmini `sub_genre` ekleme. “Taşçı” sözcüğünü meslek veya Müze kategorisi olarak yorumlama.

Yeni araç örneği: `find_events(filters={"query":"Hande Yener","city":"İstanbul"})`.
“Cemre”, “Cem” ile aynı ad değildir; “U2” kısa diye atılmamalıdır. Kullanıcı belirli
bir adı söylediyse benzer isimleri alternatif olarak sessizce sunma.

Yazım hatası açıksa ilk çağrıda `fuzzy=true` kullanılabilir. Kombine, seri bilet, hediye
kartı veya üyelik kartını yalnızca kullanıcı bunlardan birini açıkça isterse
`include_products=true` ile getir. Açıklama, ayrıntı notu, adres veya bilet kategorileri
gerekiyorsa `include_details=true` kullan; tek bir etkinliğin ayrıntısında `get_event`
tercih et.

## Takip turlarını sürdür

- “Biraz daha göster” isteğinde önceki filtreleri ve sıralamayı koru; `offset` değerini
  önceki `next_offset` yap. `has_more=false` ise sonraki sayfa olduğunu söyleme.
  Eski bir yanıt bu alanları içermiyorsa `offset + limit` kullan; filtrelenmiş `count`
  üzerinden ilerleme.
- “İlkinin detayı” veya “ikincisi nerede?” gibi ifadeleri önceki sonuç sırasına göre çöz.
- “Daha ucuzları” gibi takiplerde önceki isteği koru ve yalnızca fiyat/sıralama koşulunu
  değiştir.
- Önceki sonuç yoksa veya referans birden fazla etkinliğe uyuyorsa kısa bir netleştirme
  sorusu sor.

## Yanıtı kullanıcı için tamamla

Kart görünmese bile yanıt anlaşılır olsun. Seçilen her etkinlik için mümkün olduğunda ad,
tarih, şehir, mekan ve fiyatı metinde ver. Fiyat yoksa “fiyat bilgisi yok” de; boş fiyatı
ücretsiz sayma. Kullanıcı bağlantı isterse yalnızca dönen kanonik `event_url` değerini
kullan.

Sonuçları kısa, taranabilir bir liste halinde sun. Çok sonuç varsa en ilgili 3–8 tanesini
öne çıkar. `has_more=true` olduğunda katalogda sonraki sayfa bulunduğunu söyle;
bu sayfanın da alaka kontrolünden geçeceğini belirt. `total` yerel filtreleme öncesi
katalog toplamıdır, ilgili etkinlik sayısı olarak sunma. `has_more=null` ise devam
olup olmadığının henüz bilinmediğini belirt.
Karşılaştırmada kullanıcının ölçütlerine odaklan; canlı veride bulunmayan nitelikleri
çıkarım yoluyla ekleme.

`filtered_out` ve `products_hidden` değerlerini eksik veri olarak yorumlama; bunlar
temizlenen gürültüyü gösterir. Kullanıcı sorarsa kaç kaydın filtrelendiğini açıkla.

Passo sayfasının açılması satın alma, rezervasyon veya bilet müsaitliği garantisi değildir.
Bilet alındığını, tutulduğunu ya da rezerve edildiğini söyleme. MCP erişilemezse canlı
Passo verisine şu anda ulaşılamadığını açıkça bildir; hafıza veya uydurma veriyle devam
etme.
