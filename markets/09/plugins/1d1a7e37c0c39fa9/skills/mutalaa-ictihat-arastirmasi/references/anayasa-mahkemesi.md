# Anayasa Mahkemesi kaynakları

`aym_karari_ara` aracında norm denetimi için `tur=norm_denetimi`, bireysel
başvuru için `tur=bireysel_basvuru` seç. Talep veya eldeki numara bu ayrımı
belirlemiyorsa kullanıcıya sor; bir koleksiyonun boş olmasından diğerini
araştırmış sonucu çıkarma.

Anonimleştirilmiş dar sorguyla adayları bul; kullanıcının özel başvuru/dosya
numarasını sorguya taşıma. Norm denetiminde esas/karar; bireysel başvuruda
başvuru numarası ve karar tarihini sonuçtaki bilgilerle doğrula. Kaynak kimliğini
yeniden üretmeden `belge_getir` aracına aktar. Başvuru konusu, inceleme kapsamı,
gerekçe ve sonuçtan soruya etkisi olan kısımları oku; gereken devam sayfalarını
tamamla. Arama özeti veya hak adı tek başına ihlal/iptal sonucu göstermez.

Yalnız okunan karara dayanan bulguyu aktar; sonucu kullanıcı olayı için otomatik
kesinlik diye sunma. Yürürlük, olay tarihi veya ilgili norm bağlantısı için
kanıt eksikse mevzuat akışına dön ya da kullanıcıya belirleyici soruyu sor.
