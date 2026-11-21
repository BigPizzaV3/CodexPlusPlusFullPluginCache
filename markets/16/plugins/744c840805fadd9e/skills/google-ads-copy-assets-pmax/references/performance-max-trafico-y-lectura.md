# Performance Max: tráfico y lectura

### Una PMax "multicanal" suele ser una campaña de Search
- **Tipo**: error de método
- **Por qué**: el 83-98% del gasto fue a la red de búsqueda en varias cuentas. Cuando YouTube sube de peso, el ROAS cae y el agregado no dice por qué.
- **Cómo detectarlo**: coste y conversiones por `segments.ad_network_type`, mes a mes.
- **Qué hacer**: leerla siempre por red. Al clonarla, atar el budget al techo de demanda en Search, no al de la referencia.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026.

### PMax y Search sobre la misma query no son dos subastas
- **Tipo**: error de método
- **Por qué**: una PMax "de competidores" compraba 84% genérico y el 74% de sus clics eran términos que Search también servía. El Performance Planner las suma como independientes.
- **Cómo detectarlo**: cruzar términos de `campaign_search_term_view` con los de `search_term_view` de la misma ventana.
- **Qué hacer**: descontar el solape antes de leer el marginal del Planner. Con un descuento del 37%, el plan perdía recorrido.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026.

### Tras excluir la marca propia de PMax, la caída de conversiones es reatribución
- **Tipo**: error de método
- **Por qué**: sin exclusión, PMax hace de campaña de marca y su eficiencia se infla. Al excluirla, la marca pasa a la Search de marca.
- **Cómo detectarlo**: conversiones de marca en el tramo Search de PMax antes de la fecha de exclusión.
- **Qué hacer**: no actuar sobre esa caída. Activar brand exclusions siempre y tener Search de marca aparte. La brand exclusion cubre misspells; las negativas no tienen close variants.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026.

### El idioma se targetea a nivel campaña, no de asset group
- **Tipo**: gotcha de plataforma
- **Por qué**: Google elige el asset group. Un grupo en otro idioma dentro de la campaña no se limita a esos usuarios. El criterio de idioma filtra la interfaz del usuario, no el idioma de la query.
- **Cómo detectarlo**: campañas sin criterio `LANGUAGE`. Clics por idioma de la query en los search terms.
- **Qué hacer**: campaña aparte por idioma, con idioma excluido en la otra para que no compitan. Para cortar queries de otro idioma, negativas.
- **Evidencia**: Visto en 2-3 cuentas, sep 2026.

### Una PMax de acciones locales no se juzga por `metrics.conversions`
- **Tipo**: error de método
- **Por qué**: en un negocio con ubicaciones físicas, la PMax local puja a "cómo llegar", llamadas y visitas. La conversión principal de la cuenta no es biddable en esa campaña y sale a 0 en `conversions`. Leída así, se pausa una campaña que sí la produce.
- **Cómo detectarlo**: `metrics.all_conversions` por `segments.conversion_action_name`. `cost_micros` no se puede pedir con ese segmento: dos queries y join.
- **Qué hacer**: medir aparte la conversión principal con `all_conversions`. En el caso medido, la PMax local batía a su Search hermana.
- **Evidencia**: Visto en 1 cuenta, ago 2026.
