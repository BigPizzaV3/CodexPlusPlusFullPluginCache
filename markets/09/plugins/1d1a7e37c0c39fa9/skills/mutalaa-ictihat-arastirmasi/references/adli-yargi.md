# Adli yargı kaynakları

| İstenen kaynak | Araç |
| --- | --- |
| Yargıtay hukuk veya ceza kararı | `yargitay_karari_ara` |
| Bölge adliye hukuk dairesi / hukuk istinafı | `bolge_adliye_hukuk_karari_ara` |
| Kaynaktaki ilk derece hukuk kararları | `yerel_hukuk_karari_ara` |
| Kanun yararına bozma koleksiyonu | `kanun_yararina_bozma_ara` |

Kullanıcının belirttiği mahkemeyi koru. Yargıtay ile istinafı, hukuk istinafı ile
ceza istinafını aynı kategori sayma. Yargı aşaması belirleyici ve eksikse sor.
Mevcut yerel hukuk aracı ilk derece ceza kararlarını kapsıyormuş gibi kullanılamaz.

Anonimleştirilmiş sorguya gereken daire ve tarih filtrelerini ekle. Esas/karar
numarasını yalnız kamuya açık emsalin kaynak referansıysa kullan; kullanıcının
özel dosya numarasını gönderme. Yıl ve sıra alanlarını ayır. Daire kodunu o
aracın şemasından/açıklamasından doğrula. Sonuçta mahkemeyi ve numaraları kontrol
et; ilgili belgenin tam metnini
`belge_getir` ile oku. Aramada başka mahkemeye yapılan atfı o mahkemenin kendi
kararı olarak sunma.

KYB kaydı yazılı emir/başvuru niteliğinde olabiliyorsa bu niteliği koru;
mahkeme veya karar niteliğini metne bakmadan üretme. Ceza istinafı karar araması
bu MCP'nin beta kapsamı dışındadır; hukuk istinafı aracı bu ihtiyacı karşılamaz.
