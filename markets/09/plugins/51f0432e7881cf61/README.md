# PerfectSens — 1.0.3

Geliştirici: **Ömer Bilgin Bilgili**  
Web sitesi: https://perfectsens.com  
MCP sunucusu: https://mcp.perfectsens.com/mcp  
Demo: https://youtu.be/EJuko6rVhP4

Bu Agent Plugins 1.0 paketi mevcut PerfectSens sunucusuna bağlanır. ZIP sunucu kodunu taşımaz veya değiştirmez.

## Paket içeriği

- Geliştirici adı, web sitesi ve yayındaki destek, gizlilik ve kullanım şartları bağlantıları.
- Orijinal markadan üretilmiş 512×512 logo ve 128×128 sohbet simgesi.
- İngilizce liste metinleri, Türkçe çeviri ve üç başlangıç istemi.
- Beş olumlu ve üç olumsuz inceleme senaryosu.
- Ücretsiz hizmete uygun ticaret beyanı ve sürüm notları.
- Kullanıcının verdiği YouTube bağlantısı, `extensions.com.openai.review.demo_recording_url` alanında.

## Demo ve doğrulama

Yeni 365,6 saniyelik yerel kayıtta dönüşüm, karşılaştırma, etkileşimli test ayarları, web sitesinde tamamlanan test ve dışa aktarılan sonuç PNG'sinin ChatGPT yorumu görülüyor. YouTube bağlantısı oturum açılmadan HTTP 200 döndürüyor; video başlığı “perfectsens MCP”, süresi 366 saniye ve oynatıcı durumu `OK`. MP4 dosyası ZIP'e gömülmedi.

Yerel kayıt incelemesi ve bağlantı kontrolü ayrıntıları `docs/VIDEO-DEGERLENDIRME.md` dosyasındadır. PNG üzerinden yorumlama, MCP `analyze_result` aracının çağrıldığı anlamına gelmez.

## Portalda tamamlanacaklar

Ülke kapsamı kullanıcı tarafından seçilmediği için `publication.countries` eklenmedi; portalda seçilmelidir. Videoda özel uygulamalar için görülen CSP anahtarı bir geliştirme ayarıdır; bu anahtarın değiştirilmesi veya bunun için yeni kayıt çekilmesi bir paket gereksinimi olarak sunulmaz. Sunucunun arayüz kaynağında bildirdiği CSP ile bu ayar ayrı konulardır.

Doğru doğrulanmış geliştirici kimliği, alan adı doğrulaması, MCP bağlantısı ve taraması, son inceleme senaryoları ve politika beyanları portalda tamamlanır. Yerel paket doğrulaması yayın onayı değildir.

Resmî başvuru süreci: https://developers.openai.com/plugins/deploy/submission
