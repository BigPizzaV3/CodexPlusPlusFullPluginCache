# GOLD example — Teatro / Ópera en herradura ocupado

Uso recomendado: archivo de referencia para que un GPT CADSFS aprenda el **nivel de detalle esperado** en teatros históricos, óperas, salas líricas y recintos con palcos, galerías y plateas ocupadas.

Este archivo no debe exponerse al usuario final como texto ni como JSON. Debe usarse sólo como ejemplo interno de calidad.

## Archivo asociado

- `GOLD_Teatro_Colon_herradura_ocupado.csm`

## Por qué sirve como ejemplo

- Tipología: teatro/ópera en herradura.
- Nivel de detalle adecuado para sala compleja, no modelo de caja simple.
- Contiene separación de zonas de audiencia y ocupación.
- Incluye materiales y constructividad por superficie.
- Incluye assemblies de aislamiento / construcción.
- Cumple la regla `materials: []`.
- No deja `Default` como material final en `surface_group_material`.

## Métricas de referencia

- Objetos: 66
- Audience areas: 128
- Wall assemblies: 14
- Speaker systems: 0
- Valores `Default` en `surface_group_material`: 0

## Cuándo usarlo como patrón

Usar este ejemplo cuando el usuario pida:

- teatro lírico;
- ópera;
- sala en herradura;
- teatro histórico;
- teatro con palcos;
- sala con varias bandejas de audiencia;
- reconstrucción detallada de sala famosa;
- recinto ocupado con platea, palcos, galerías o paraíso.

## Qué debe imitar el GPT

- Densidad de detalle.
- Separación clara de zonas.
- Audience areas múltiples.
- Materiales diferenciados por zona y superficie.
- Uso de assemblies constructivos.
- Validación de `materials: []` y ausencia de `Default` en materiales finales.
- Entrega como archivo cerrado, sin mostrar JSON ni arquitectura interna.

## Qué NO debe imitar

- No copiar dimensiones ni geometría exacta salvo que el usuario pida explícitamente una sala tipo Teatro Colón.
- No entregar el interior del CSM en pantalla.
- No resumir el cookbook.
- No explicar el generador.
- No mostrar código.
- No usar este archivo como sustituto del pedido del usuario cuando el recinto tenga planos o fotos propias.

## Regla de calidad asociada

Para recintos teatrales complejos, una salida con una sola caja rectangular, una sola zona de audiencia o materiales genéricos debe considerarse insuficiente y debe regenerarse con mayor detalle antes de entregar. Sin embargo, detalle excesivo puede ser contraproducente. Tomemos este ejemplo como el límite máximo de detalle a menos que se solicite aún más.
