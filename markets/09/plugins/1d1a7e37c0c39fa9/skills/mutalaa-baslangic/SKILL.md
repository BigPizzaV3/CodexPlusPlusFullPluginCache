---
name: mutalaa-baslangic
description: Mütalaa eklentisine bağlanmak, kurulumu tamamlamak veya bağlantıyı denemek için kullan. Hukuk sorularında turk-hukuk-mevzuat-ictihat-vergi skill'ini kullan.
---

# Mütalaa eklentisi ile başla

## Kurulum veya bağlantı sorusu

Araç listesi, OAuth veya API anahtarı gibi teknik ayrıntı anlatma. Araçlar
görünüyorsa bağlı olduğunu bir cümleyle söyle ve kullanıcının hukuki sorusunu
iste. Kullanıcı kurulumu sormadan hukuki soru sorduysa kurulumu anlatma,
doğrudan araştırmaya geç.

## Bağlantı

Mütalaa eklentisinin araçlarını ve mevcut parametre şemalarını istemcinin araç
keşfiyle bul; araç adlarına eklenen istemci/eklenti öneklerini dikkate al.
Araçlar bağlantı istemiyorsa yeniden giriş talep etme.

Araçlar ilk anda görünmüyorsa eklentiyi yok sayma, önce istemcinin araç aramasıyla
`Mütalaa eklentisi` ve `mevzuat_ara` diye ara. Arama da sonuç vermezse veya oturum
geçersizse kullanıcıyı eklentinin bağlantı ayarına yönlendir. ChatGPT'de Mütalaa eklentisini bağlayıp Mütalaa hesabıyla
OAuth girişini tamamlasın. Claude'da Mütalaa eklentisinin Connectors sekmesinden
bağlansın. Yeni bir sohbet açıp yeniden deneyebilir. Telefonda uygulama kurulum
seçeneği göstermiyorsa aynı hesabın telefon tarayıcısındaki katalog/eklenti
ayarlarını kullanabilir; ardından mobil uygulamada yeni sohbet açabilir.
Kurulum seçenekleri hesap ve istemci desteğine bağlıdır; görülmeyen bir menüyü
varmış gibi anlatma. Kullanıcıdan parola, token, API anahtarı veya doğrulama
kodu isteme; bunlar yalnız sağlayıcının giriş ekranında girilir. Son kullanıcı
Python, terminal veya yapılandırma dosyası kurmaz.

Hukuki soru için `turk-hukuk-mevzuat-ictihat-vergi` skill'ini yükle. Destek için
https://mutalaa.tr/legal ve admin@mutalaa.tr kullan.
