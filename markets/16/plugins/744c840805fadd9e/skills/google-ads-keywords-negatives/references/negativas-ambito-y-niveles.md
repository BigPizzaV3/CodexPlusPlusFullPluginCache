# Negativas: ámbito y niveles

### Una negativa solo bloquea en su ámbito; resolverlo antes de medir
- **Tipo**: error de método
- **Por qué**: una lista solo bloquea las campañas que la enlazan. Una negativa de ad group solo bloquea ese ad group. Cruzar contra todas las negativas de la cuenta infla el problema.
- **Cómo detectarlo**: casos medidos: las keywords "bloqueadas" bajaban a menos del 15% al resolver el ámbito en un caso y a menos del 3% en otro; "5,5% de clics bloqueados" era 3,1%.
- **Qué hacer**: conjunto aplicable = negativas del ad group destino + negativas de campaña + `shared_criterion` de cada `campaign_shared_set` de esa campaña con `status = ENABLED`. En el cruce negativa a search terms, llevar el ámbito en la clave: `(ad_group_id | campaign, término)`.
  ```sql
  SELECT campaign.id, shared_set.id, shared_set.name, shared_set.status
  FROM campaign_shared_set
  WHERE campaign_shared_set.status = 'ENABLED'
  ```
- **Evidencia**: Visto en 4+ cuentas, may-sep 2026.

### El nombre de una lista de negativas no describe su contenido
- **Tipo**: error de método
- **Por qué**: tras un año recibiendo altas, una lista llamada "productos" puede llevar competidores, y una llamada "informacional" ser sobre todo productos.
- **Cómo detectarlo**: clasificar cada miembro con el clasificador de intención y mirar el reparto. El bloqueo incremental de enlazar la lista L a la campaña C es el cruce de sus miembros con los search terms actuales de C.
- **Qué hacer**: una lista no se enlaza a la campaña cuya intención contiene. Un bloqueo alto donde la lista no está enlazada es prueba de exclusión deliberada, no hueco. Podar miembros que no tocan ninguna query servida en 180 días (Search y PMax).
- **Evidencia**: Visto en 2-3 cuentas, sep-oct 2026.

### Ninguna query puede quedarse sin campaña que la sirva
- **Tipo**: regla de decisión
- **Por qué**: al cruzar negativas entre campañas para enrutar, una query con dos atributos (por ejemplo, producto y ubicación) puede quedar rechazada por las dos. Cada negativa pasa su puerta por separado.
- **Cómo detectarlo**: para cada término afectado, comprobar que existe una campaña viva con keyword que lo alcance y sin bloqueo en su ámbito.
- **Qué hacer**: negativizar la intención X en A solo si hay una campaña B viva que la compra. Decidir qué eje gana las combinaciones. Al negativizar para enrutar, crear la keyword en destino en el mismo movimiento.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026.

### Si una lista cancela una positiva en su ámbito, lo normal es que sobre la keyword
- **Tipo**: regla de decisión
- **Por qué**: las listas se enlazan a propósito. Una keyword de competidor en una campaña genérica con lista de competidores está mal colocada; la lista hace su trabajo.
- **Cómo detectarlo**: medir el gasto de la positiva cancelada por `(ad_group_id, criterion_id)`. Por texto, el gasto de otra copia no bloqueada se cuela.
- **Qué hacer**: corregir la keyword por defecto. Excepción: una negativa mal colocada que bloquea una keyword ENABLED en campaña activa se quita, aunque sea EXACT. Revisar siempre PHRASE y BROAD de una o dos palabras a nivel lista o campaña.
- **Evidencia**: Visto en 2-3 cuentas, jun-nov 2026.

### En cuentas con sculpting masivo, la señal limpia es "cancela una positiva activa en el mismo ámbito"
- **Tipo**: error de método
- **Por qué**: el cruce "negativa bloquea término que convirtió" da miles de falsos positivos: enrutado deliberado entre ad groups, separación por producto o idioma, y términos que convirtieron antes de negativizarse.
- **Cómo detectarlo**: ante el aviso, comprobar si un ad group hermano de la misma campaña recoge la query. Mirar si las keywords equivalentes del avisado están pausadas y si la query ya sirve desde el otro lado.
- **Qué hacer**: filtrar primero por cancelación de positiva activa en el mismo ámbito. Revisar después erratas de marca propia negativizadas.
- **Evidencia**: Visto en 2-3 cuentas, jun-sep 2026.

### El script oficial de conflictos de negativas no ve la mayoría de bloqueos
- **Tipo**: gotcha de plataforma
- **Por qué**: carga las positivas con `segments.date DURING YESTERDAY`, así que una positiva totalmente bloqueada (0 impresiones) nunca entra. Además no cuenta EXACT sobre PHRASE/BROAD, no mira search terms y tiene un tope de negativas.
- **Cómo detectarlo**: comparar su salida con una auditoría propia sin filtro de fecha.
- **Qué hacer**: auditar los tres niveles (cuenta, listas enlazadas, campaña y ad group) contra todas las positivas ENABLED y contra search terms con conversión.
- **Evidencia**: Visto en 1 cuenta, jun 2026.

### Negativas genéricas de una o dos palabras son el fallo más repetido
- **Tipo**: regla de decisión
- **Por qué**: verbos y sustantivos sueltos en BROAD o PHRASE ("comprar", "gratis", "precio", "opiniones") apagan positivas legítimas. Lo que cortan no se ve en search terms.
- **Cómo detectarlo**: listar negativas PHRASE/BROAD de 1-2 tokens en listas y campañas y cruzarlas contra positivas ENABLED del ámbito.
- **Qué hacer**: quitarlas o bajarlas a EXACT sobre la query concreta. No defenderlas porque lo visible sea basura.
- **Evidencia**: Visto en 2-3 cuentas, jun-nov 2026.

### Listas de topónimos en PHRASE o BROAD bloquean queries legítimas
- **Tipo**: regla de decisión
- **Por qué**: nombres de ciudad aparecen en queries con intención válida. Una lista compartida de ubicaciones arrastra el bloqueo a todas las campañas enlazadas.
- **Cómo detectarlo**: cruzar la lista contra search terms con conversión de cada campaña enlazada. En un caso, una lista geo bloqueaba todas las campañas enlazadas sin que nadie lo supiera.
- **Qué hacer**: poner las negativas de ciudad a nivel campaña cuando solo una campaña las necesita. Excluir nombres cortos que son palabras comunes.
- **Evidencia**: Visto en 2-3 cuentas, may-jul 2026.

### En cuentas maduras el recorrido de negativas suele estar agotado
- **Tipo**: regla de decisión
- **Por qué**: tras años de negativización, lo que queda sin convertir es la intención para la que existen las campañas o ruido de pocos clics. El tráfico bloqueado convertía al CPL de la cuenta.
- **Cómo detectarlo**: cruzar n-grams sin conversión contra las negativas que alcanzan a cada campaña. Medir el irrelevante puro en % del coste revelado.
- **Qué hacer**: pedir evidencia por conversión final antes de una tanda masiva. Medido entre 0,1% y 3,3% del coste en cuatro cuentas.
- **Evidencia**: Visto en 4+ cuentas, ago-oct 2026.
