# Performance Max: assets y asset groups

### Imágenes: 20 por asset group sumando todos los ratios
- **Tipo**: gotcha de API
- **Por qué**: el tope es la suma de MARKETING, SQUARE, PORTRAIT y TALL_PORTRAIT. Al llegar falla con `RESOURCE_LIMIT`.
- **Cómo detectarlo**: contar imágenes del anunciante por asset group.
- **Qué hacer**: para borrar un enlace, usar el `resource_name` que devuelve la query; construirlo a mano da `BAD_RESOURCE_ID`.
- **Evidencia**: Visto en 1 cuenta, ago 2026.

### Un texto idéntico es el mismo asset en toda la cuenta
- **Tipo**: gotcha de API
- **Por qué**: crear el mismo texto otra vez en otro asset group da `CONCURRENT_MODIFICATION`. Un search theme también saca su id del texto.
- **Cómo detectarlo**: buscar en `asset` por `text_asset.text` antes de crear.
- **Qué hacer**: enlazar el asset existente. No quitar y volver a poner el mismo search theme en una petición (`ID_EXISTS_IN_MULTIPLE_MUTATES`).
- **Evidencia**: Visto en 2-3 cuentas, oct 2026.

### Los vídeos auto-creados no cuentan para Ad Strength
- **Tipo**: gotcha de plataforma
- **Por qué**: la UI enseña 5 vídeos y el grupo sigue en GOOD. En una cuenta, todos los vídeos eran `AUTOMATICALLY_CREATED`. Las variantes auto-generadas tampoco valen como input de un anuncio nuevo.
- **Cómo detectarlo**: `asset.source` en el inventario de vídeo.
- **Qué hacer**: si el cliente pregunta por qué no llega a Excellent, la respuesta es que no tiene vídeo propio. Hace falta un fichero.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026.
