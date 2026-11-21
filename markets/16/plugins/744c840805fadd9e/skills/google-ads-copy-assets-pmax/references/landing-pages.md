# Landing pages

### Una redirección que pierde la querystring borra el `gclid`
- **Tipo**: gotcha de plataforma
- **Por qué**: un 307 sin querystring carga la página igual y la conversión no se atribuye. CVR 10 veces menor que la misma página por otra ruta.
- **Cómo detectarlo**: `curl -sIL "https://dominio/ruta?gclid=TEST123" | grep -iE "^(HTTP/|location:)"`.
- **Qué hacer**: buscar también en `ad_group_criterion.final_urls`: el override de keyword gana al del anuncio. Confirmar con el mismo término en otras campañas.
- **Evidencia**: Visto en 1 cuenta, ago 2026.
