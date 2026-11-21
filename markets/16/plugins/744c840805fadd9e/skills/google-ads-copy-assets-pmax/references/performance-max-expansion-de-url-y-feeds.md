# Performance Max: expansión de URL y feeds

### Cuando una PMax se va de intención, mira el destino antes que las queries
- **Tipo**: error de método
- **Por qué**: la expansión de URL final crea landings que el asset group no declaró. Los search terms siguen a la landing.
- **Cómo detectarlo**: `landing_page_view` con `metrics.clicks > 0`, agrupado por prefijo de path. `final_url_expansion_asset_view` lista las URLs activadas.
- **Qué hacer**: excluir por URL o acotar con page feed. En un caso, el 94% de los clics iba a páginas pensadas para otro tipo de usuario.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026.

### Page feed y filtro de asset group: reglas de formato
- **Tipo**: gotcha de API
- **Por qué**: el feed solo acepta dos columnas, `Page URL` y `Custom label`, con 5 etiquetas máximo por fila. El filtro de asset group no admite EQUALS.
- **Cómo detectarlo**: n/a.
- **Qué hacer**: una fila por URL con la unión de etiquetas, no la primera. Filtrar con `url_contains` y la URL completa, o con `custom_label`.
- **Evidencia**: Visto en 1 cuenta, sep 2026.

### Un feed con URLs que redirigen con 200 falla en silencio
- **Tipo**: gotcha de plataforma
- **Por qué**: en un feed cuyos ids cambian, las URLs viejas pasan a redirigir a una página genérica. Un 200 no dispara `DESTINATION_NOT_WORKING`.
- **Cómo detectarlo**: muestrear URLs del feed con `curl -sIL` y comparar el destino final con la URL pedida.
- **Qué hacer**: refrescar el feed antes de enlazarlo. Comprobar también que el asset set está enlazado: `campaign_asset_set` puede no devolver filas.
- **Evidencia**: Visto en 1 cuenta, ago-sep 2026.
