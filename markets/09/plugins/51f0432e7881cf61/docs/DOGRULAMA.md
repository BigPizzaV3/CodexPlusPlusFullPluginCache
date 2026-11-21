# Doğrulama — 4 Ekim 2026

Paket sürümü 1.0.3; önceki doğrudan MCP kontrolünde sunucunun bildirdiği sürüm 1.0.0.

| Kontrol | Sonuç |
|---|---|
| Agent Plugins 1.0 plugin.json ve mcp.json | Yerel şema doğrulaması; ayrıca OpenAI liste alanlarına ilişkin yerel sınır ve içerik kontrolleri |
| Kimlik | PerfectSens / Ömer Bilgin Bilgili / https://perfectsens.com |
| MCP | https://mcp.perfectsens.com/mcp; Streamable HTTP |
| Destek | https://perfectsens.com/support/ — önceki canlı kontrolde HTTP 200, iletişim ve ChatGPT kapsamı doğrulandı |
| Gizlilik | https://perfectsens.com/privacy/ — önceki canlı kontrolde HTTP 200, site ve ChatGPT/MCP kapsamı doğrulandı |
| Şartlar | https://perfectsens.com/terms/ — önceki canlı kontrolde HTTP 200, işletici ve ücretsiz hizmet bilgisi doğrulandı |
| Ticaret | Yayınlanmış şartlar ve araç kapsamına göre commerce=false |
| Görseller | Orijinal logodan 512×512 ve 128×128 PNG; ZIP içindeki dosyalar kontrol edildi |
| İnceleme senaryoları | Manifestte tam 5 olumlu ve 3 olumsuz senaryo |
| Hesaplama örneği | Valorant 800 DPI / 0.4 = 40.82 cm/360; CS2 800 DPI = 1.273; CS2 1600 DPI = 0.636 |
| Önceki canlı araç kontrolleri | 7 araç çağrısı başarılı; 8 aracın gerekli boolean etiketleri mevcut |
| Yeni yerel video | 365,6 saniye, 1920×1080; tamamlanmış web sitesi testi ve PNG üzerinden ChatGPT yorumu görüldü |
| Barındırılan video | https://youtu.be/EJuko6rVhP4; girişsiz HTTP 200, oynatıcı durumu OK, özel video değil, süre 366 saniye |
| Demo alanı | extensions.com.openai.review.demo_recording_url içine gerçek bağlantı yazıldı |

Yerel Agent Plugins şeması, OpenAI'ye özgü tüm portal kurallarını denetlemez. Liste alanlarına ek kontroller uygulandı; nihai portal doğrulaması yapılmadı. Politika sayfalarının erişimi ve kapsamı incelendi; işletici beyanlarının arka uç denetimi veya e-posta teslim testi yapılmadı.

## Portal öncesi ve portalda kalanlar

1. Ülke kapsamını portalda seçin. Kullanıcı tercihi sağlanmadığından bu alan tahminle doldurulmadı.
2. Doğru doğrulanmış geliştirici kimliğiyle alan adı doğrulamasını, MCP bağlantısını ve sunucu taramasını tamamlayın. Arayüz kaynağının CSP bilgileri sunucu ve hedef ortam üzerinden değerlendirilir; videodaki geliştirme anahtarını değiştirmek ayrı bir başvuru adımı değildir.
3. Kaydedilen sürümde inceleme senaryolarını çalıştırın ve geliştirici politika beyanlarını tamamlayın. Yerel doğrudan araç kontrolleri, portalda yapılacak son senaryo çalıştırmalarının yerine geçmez.

Yükleme, incelemeye gönderim, onay ve yayınlama ayrı aşamalardır. Paket bu işlemleri gerçekleştirmez. Video ayrıntıları VIDEO-DEGERLENDIRME.md içindedir.

Kaynaklar:
- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/deploy/app-review
- https://agent-plugins.org/schemas/1.0.0/plugin.schema.json
- https://agent-plugins.org/schemas/1.0.0/mcp.schema.json
