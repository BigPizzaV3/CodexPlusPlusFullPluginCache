# Copy y RSAs: escribir

### Valida la longitud de cada asset con código, no a mano
- **Tipo**: gotcha de API
- **Por qué**: los límites son 30 caracteres por headline, 90 por description y 15 por path. Contar a mano falla por uno con acentos.
- **Cómo detectarlo**: `len()` sobre cada string antes de mutar. La API rechaza el anuncio entero si un asset pasa del límite.
- **Qué hacer**: validar en el script. Revalidar también al sustituir un término, porque una letra más puede llevar un headline de 29 a 31.
- **Evidencia**: Visto en 2-3 cuentas, sep 2026.

### No pinees assets en los RSA
- **Tipo**: regla de decisión
- **Por qué**: el pin recorta las combinaciones que el sistema prueba. El control del mensaje se consigue escribiendo assets válidos en cualquier posición.
- **Cómo detectarlo**: `ad_group_ad.ad.responsive_search_ad.headlines` con `pinned_field` no vacío.
- **Qué hacer**: escribir cada headline para que funcione como apertura y como cierre. Si una combinación sale mal, reescribir o quitar el asset.
- **Evidencia**: Visto en 4+ cuentas, oct 2026.

### Mutar los textos de un RSA reemplaza la lista entera y borra los pins
- **Tipo**: gotcha de API
- **Por qué**: `AdService.mutate_ads` con `update_mask` sobre `responsive_search_ad.headlines` no hace merge. Un `AdTextAsset` construido solo con `.text` pierde su `pinned_field`.
- **Cómo detectarlo**: leer el anuncio vivo antes de mutar y comparar `pinned_field` después. Una verificación que solo compara textos no lo ve.
- **Qué hacer**: reenviar las listas completas con el pin de cada asset original. Guardar el pin en el backup. Comparar también el pin en scripts que despinean.
- **Evidencia**: Visto en 1 cuenta, ago 2026.

### Edita headlines y descriptions en el mismo anuncio, no con remove y create
- **Tipo**: gotcha de API
- **Por qué**: los textos de un RSA son editables in place. Se conserva el `ad_id` y el histórico.
- **Cómo detectarlo**: n/a.
- **Qué hacer**: `AdService.mutate_ads` con `update` y máscara `responsive_search_ad.headlines` / `.descriptions`. Reservar remove y create para cambiar el set entero. Agrupar las ediciones del mismo anuncio en una sola mutación.
- **Evidencia**: Visto en 4+ cuentas, jun 2026.

### Un ad group admite 3 RSA ENABLED; el cuarto falla
- **Tipo**: gotcha de API
- **Por qué**: crear un cuarto RSA ENABLED devuelve `RESOURCE_LIMIT`. Los PAUSED no cuentan.
- **Cómo detectarlo**: contar RSA con `ad_group_ad.status = ENABLED` en el ad group antes de planificar.
- **Qué hacer**: si hay 3, planificar pausa más alta en la misma llamada, con la pausa primero. Elegir el anuncio a pausar por rendimiento L30D y L90D, no por Ad Strength.
- **Evidencia**: Visto en 4+ cuentas, abr 2026.

### La `final_url` de un RSA nuevo es la que ya usan los anuncios vivos del ad group
- **Tipo**: regla de decisión
- **Por qué**: la URL en uso lleva tracking, consentimiento y locale estandarizados. Una URL nueva arranca sin historial de landing page experience y puede romper la conversión.
- **Cómo detectarlo**: `ad_group_ad.ad.final_urls` de los RSA del ad group, ordenados por coste.
- **Qué hacer**: reutilizar la URL con más gasto o mejor CPA. Si el ad group está vacío, subir a campaña. Si hay duda, preguntar.
- **Evidencia**: Visto en 1 cuenta, may 2026.

### Escribe el headline con la palabra que se busca, no con la del producto
- **Tipo**: regla de decisión
- **Por qué**: el ad group nombra el servicio o el producto con un término interno y la query usa otro. Los assets específicos del término buscado ganan a las plantillas genéricas.
- **Cómo detectarlo**: peso de cada token en los search terms del ad group (L90D) contra los tokens de los headlines.
- **Qué hacer**: anclar los headlines nuevos a los tokens con más peso. No copiar el headline ganador de otro ad group si se aleja de la query.
- **Evidencia**: Visto en 2-3 cuentas, ago-oct 2026.

### Elige el término por demanda de búsqueda, no por corrección gramatical
- **Tipo**: regla de decisión
- **Por qué**: la palabra nativa correcta puede no ser la que se busca. Un préstamo del inglés o la variante de otro país puede tener más volumen.
- **Cómo detectarlo**: Keyword Planner geolocalizado por variante. Un verbo usado en un país puede no tener volumen en otro con la misma lengua.
- **Qué hacer**: fijar la variante como regla dura y meter la descartada, con y sin diacríticos, en la blocklist del generador de copy.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026.

### Un anuncio no afirma lo que el producto no hace, y "gratis" siempre lleva objeto
- **Tipo**: regla de decisión
- **Por qué**: "gratis" suelto se lee como todo gratis.
- **Cómo detectarlo**: contrastar cada claim con la landing. Buscar "gratis", "ilimitado", "sin registro", "verificado" en el inventario vivo.
- **Qué hacer**: escribir siempre qué es gratis. Funciones no documentadas se confirman con el cliente.
- **Evidencia**: Visto en 2-3 cuentas, ago-nov 2026.

### Una fecha de promo dentro de un RSA no caduca sola
- **Tipo**: gotcha de API
- **Por qué**: un headline a nivel campaña se pausa. Un asset de texto dentro de un RSA no: solo sale editando el anuncio.
- **Cómo detectarlo**: regex de fecha sobre los textos de RSA, asset groups y assets de cuenta, campaña y ad group, filtrando anuncios ENABLED.
- **Qué hacer**: preferir `PromotionAsset` con `start_date` y `end_date` nativos. Si la fecha va en el RSA, quitarla al cerrar la promo preservando los pins.
- **Evidencia**: Visto en 1 cuenta, ago 2026.

### Sin nombres de competidor en el copy
- **Tipo**: regla de decisión
- **Por qué**: riesgo de reclamación de marca y desaprobación. Pujar por la marca ajena es otra decisión.
- **Cómo detectarlo**: blocklist de marcas del vertical sobre headlines, descriptions y paths.
- **Qué hacer**: no usar DKI en ad groups de competidor. Aceptar que esas keywords se quedan con ad relevance BELOW por diseño.
- **Evidencia**: Visto en 4+ cuentas, 2026.

### DKI capitaliza mal los acrónimos
- **Tipo**: gotcha de plataforma
- **Por qué**: con `{KeyWord:...}` un acrónimo en mayúsculas como "ABC" sale como "Abc".
- **Cómo detectarlo**: listar las keywords del ad group y simular el render.
- **Qué hacer**: en ad groups que mezclan acrónimo y frase larga, copy estático o separar el ad group.
- **Evidencia**: Visto en 1 cuenta, 2026.

### No prometas en el anuncio lo que la landing no hace
- **Tipo**: regla de decisión
- **Por qué**: el h1 de una página puede decir una función y el contenido hacer otra. El anuncio hereda la promesa falsa.
- **Cómo detectarlo**: leer la landing completa antes de escribir. Extraer cifras, USPs y CTAs literales.
- **Qué hacer**: cada headline debe poder anclarse a algo de la página. Si la landing no sostiene el claim, no se escribe o no se crea el ad group.
- **Evidencia**: Visto en 2-3 cuentas, sep 2026.
