# Demo kaydı — 1.0.3

İnceleme bağlantısı: https://youtu.be/EJuko6rVhP4  
Yerel kaynak: 2026-10-04 03-48-51.mp4  
Yerel süre: 365,6 saniye; YouTube süresi: 366 saniye  
Görüntü: 1920×1080, 60 fps, H.264

Bu belge, önceki 122 saniyelik kayda ait değerlendirmeyi günceller. Yeni yerel video çözülerek altı saniye aralıklı kareler çıkarıldı; genel akış ve ilgili sahneler tam boyutta incelendi. Aşağıdaki zamanlar yaklaşık değerlerdir. Ses içeriği değerlendirilmedi.

| Zaman | Görülen davranış |
|---|---|
| 0:45 | Valorant 800 DPI / 0.4 dönüşümü: CS2 1.273 ve 40.82 cm/360 |
| 1:03–1:09 | Ayar karşılaştırması: 40.82 ve 51.95 cm/360; fiziksel mesafe farkı açıklanıyor |
| 2:39–2:51 | 3D widget ayarlarında Valorant / 800 / 0.4 ve hızlı mod; ilk açılışta “CSP kapalı” etiketi |
| 2:57 | Web sitesindeki teste geçiş |
| 3:03–4:21 | Gerçek Gridshot, flick, yavaş ve hızlı takip bölümleri; üç aday turu |
| 4:27 | Tamamlanmış test sonucu: 31.84–49.80 cm/360 bandı, seçilen 40.82 cm/360 ve düşük güvenilirlik |
| 4:33–4:39 | Sonuç PNG olarak dışa aktarılıyor |
| 4:45 | ChatGPT widget'ında Pointer Lock kullanılamıyor; oynanan test web sitesinde tamamlandı |
| 5:21 | Özel uygulamalar için CSP zorlama ayarı açılıyor |
| 5:33 | Gerçek sonuç PNG'si ChatGPT'ye yükleniyor ve düşük güvenilirlik belirtilerek yorumlanıyor |
| 6:03 | Donanım DPI değiştirme isteğine uygulamanın yetenek sınırı açıklanıyor |

## Bağlantı kontrolü

4 Ekim 2026 tarihinde YouTube kısa bağlantısı normal izleme sayfasına yönlendi ve oturum açılmadan HTTP 200 döndü. Video kimliği `EJuko6rVhP4`, başlığı “perfectsens MCP”, kanal adı “ömer bilgin”, süre 366 saniye. YouTube oynatıcı yanıtında `playabilityStatus.status=OK`, `isPrivate=false` ve `playableInEmbed=true`; oEmbed bilgisi de erişilebilir.

Bu kontrol, sunucunun bağlantıyı oynatılabilir bildirdiğini doğrular. Barındırılan videonun tamamı ikinci kez oynatılmadı; içerik incelemesi konuşmaya eklenmiş yerel kayıt üzerinden yapıldı. Bağlantı inceleme boyunca erişilebilir tutulmalıdır.

## Doğrulama sınırları

- Kayıt tamamlanmış web sitesi testini ve sonuç PNG'sinin ChatGPT tarafından yorumlanmasını gösterir. MCP `analyze_result` veya `compare_results` araçlarının çağrıldığı bu akışta doğrulanmadı.
- İlk widget açılışında “CSP kapalı” etiketi vardır; kullanıcı geliştirme ayarını daha sonra değiştirmiştir. Bu ayar değişikliği ayrı bir demo gereksinimi değildir. Kayıt, sunucunun arayüz kaynağında bildirdiği CSP yapılandırmasının doğruluğunu tek başına kanıtlamaz veya çürütmez; bu yapılandırma MCP taraması ve hedef ortam testiyle değerlendirilir.
- Gömülü görünümde Pointer Lock reddedildiğinde sunulan web sitesi geçişi kullanılmıştır. Bu kayıt, testin ChatGPT içinde tamamlandığı iddiasını desteklemez.

Video adresi manifestin `extensions.com.openai.review.demo_recording_url` alanına eklenmiştir.
