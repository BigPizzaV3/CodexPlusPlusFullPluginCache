# Extensiones y assets

### Los niveles de extensión se suman; el más específico no apaga al general
- **Tipo**: gotcha de plataforma
- **Por qué**: con sitelinks propios en todos los ad groups, el set de campaña siguió sirviendo en el 91% de las campañas en un solo día. Los de cuenta también entran.
- **Cómo detectarlo**: impresiones por nivel en un solo día, para evitar el sesgo de enlaces creados a mitad de ventana.
- **Qué hacer**: para que un sitelink deje de salir en una intención, desenlazarlo también del nivel superior. Solo si todos los ad groups ENABLED quedan con set propio.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026.

### Un enlace de extensión PAUSED no es cobertura
- **Tipo**: error de método
- **Por qué**: `campaign_asset`, `ad_group_asset` y `customer_asset` tienen estado propio. `!= 'REMOVED'` deja pasar los PAUSED y fabrica cobertura y desajustes falsos.
- **Cómo detectarlo**: `WHERE campaign_asset.status = 'ENABLED'`. Por defecto la consulta también devuelve REMOVED.
- **Qué hacer**: filtrar por estado del enlace en toda query de `*_asset`. Un enlace activo con 0 impresiones es otro problema: no entra en subasta.
- **Evidencia**: Visto en 2-3 cuentas, jul-sep 2026.

### Mira en qué nivel sirven las extensiones antes de leer hallazgos de encaje
- **Tipo**: error de método
- **Por qué**: en cuentas que corren a nivel cuenta, casi todo lo enlazado en campaña tiene 0 impresiones. Un desajuste ahí es inventario muerto, no exposición.
- **Cómo detectarlo**: impresiones por nivel. En un caso, el 88% de los enlaces de campaña y ad group tenía 0 impresiones en 90 días.
- **Qué hacer**: priorizar por impresiones servidas. Revisar si sitelinks temáticos útiles están enlazados solo a campañas ENDED.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026.

### Los assets de extensión del anunciante se editan in place, y el cambio es global
- **Tipo**: gotcha de API
- **Por qué**: el asset es de cuenta. Editarlo cambia cada `campaign_asset` y `ad_group_asset` que lo referencia. Los `AUTOMATICALLY_CREATED` no se editan.
- **Cómo detectarlo**: alcance por `asset.id` sobre `campaign_asset` y `ad_group_asset` antes de editar.
- **Qué hacer**: errata o URL rota en todos lados: editar con `AssetService` y `update_mask`. Cambio en un solo sitio: crear gemelo y reenlazar. `AssetOperation` no tiene remove: un asset solo se desenlaza.
- **Evidencia**: Visto en 2-3 cuentas, ago 2026.

### Lee el contenido de sitelinks, callouts y snippets con `MessageToDict`
- **Tipo**: gotcha de API
- **Por qué**: el acceso proto-plus directo a estos tipos devuelve cadena vacía.
- **Cómo detectarlo**: un audit que da todos los textos vacíos.
- **Qué hacer**: `MessageToDict(row.asset._pb)`.
- **Evidencia**: Visto en 4+ cuentas, 2026.

### Dos sitelinks al mismo destino en el mismo set: uno pierde siempre
- **Tipo**: regla de decisión
- **Por qué**: compiten por la misma página. En todos los conjuntos revisados, el duplicado perdió contra su hermano.
- **Cómo detectarlo**: agrupar sitelinks enlazados por destino dentro de cada ad group.
- **Qué hacer**: quitar el duplicado. Al crear, deduplicar por `(link_text, description1, description2, final_url)`.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026.

### El idioma de la landing no se puede inferir si el sitio no lleva locale en la ruta
- **Tipo**: error de método
- **Por qué**: una URL sin prefijo de idioma no da señal. Un script que asume inglés por defecto marca toda la cuenta como desajustada.
- **Cómo detectarlo**: comprobar si el sitio usa `/xx-XX/` en la ruta.
- **Qué hacer**: si no lo usa, declarar la dimensión de idioma no aplicable.
- **Evidencia**: Visto en 2-3 cuentas, sep 2026.

### Al duplicar ad groups, las extensiones temáticas viajan con el texto viejo
- **Tipo**: error de método
- **Por qué**: snippets y sitelinks específicos de un producto acaban en campañas de otro. Baja la relevancia y manda al usuario al producto equivocado.
- **Cómo detectarlo**: cruzar el producto que menciona cada asset contra el producto de la campaña anfitriona.
- **Qué hacer**: auditoría periódica de encaje. El eje es el producto, no el subproducto: el cross-sell dentro de un producto es legítimo.
- **Evidencia**: Visto en 2-3 cuentas, 2026.
