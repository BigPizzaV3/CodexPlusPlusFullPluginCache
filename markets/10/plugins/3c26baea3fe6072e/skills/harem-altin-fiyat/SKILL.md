---
name: harem-altin-fiyat
description: Harem Altın gram altın ve ons altın (XAU/USD) güncel alış/satış fiyatlarını göstermek ve bu fiyatla miktar çevirmek için harem-altin MCP araçlarını kullan. Kullanıcı gram altın, ons altın veya "kaç TL eder" gibi güncel fiyat sorduğunda tetiklenir.
---

# Harem Altın fiyatları

Güncel fiyat sorularında tahmin yürütme; her zaman `harem-altin` MCP araçlarını çağır.

- `get_current_prices` — gram altın ve ons altın (XAU/USD) güncel alış/satış fiyatları.
  Fiyat widget'ı bu aracın sonucuna eklidir.
- `convert_amount` — bir miktarın Harem fiyatına göre karşılığı (ör. "3 gram altın kaç TL").
  Çevirici widget'ı bu aracın sonucuna eklidir.

Kurallar:

- Fiyatı her zaman fiyat zamanı ve veri durumu (canlı / gecikmeli) ile birlikte aktar.
- Çevrimde hangi fiyatın (alış/satış) kullanıldığını yanıtta belirt.
- Araç `SERVICE_UNAVAILABLE` dönerse fiyat uydurma; verinin şu an alınamadığını söyle.
- Çapraz kur hesaplama: yalnız Harem'in doğrudan yayınladığı çiftler çevrilir.
- Yatırım tavsiyesi verme; alım-satım, emir veya transfer sunma. Sürüm salt okunurdur.
