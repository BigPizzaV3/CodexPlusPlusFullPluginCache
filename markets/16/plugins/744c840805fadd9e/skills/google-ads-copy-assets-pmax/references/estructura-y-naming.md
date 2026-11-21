# Estructura y naming

### No inventes nombres: replica el patrón de la cuenta
- **Tipo**: regla de decisión
- **Por qué**: separadores, orden de tokens, idioma y casing sostienen filtros, informes y scripts del cliente.
- **Cómo detectarlo**: listar entidades del mismo tipo y línea de producto.
- **Qué hacer**: copiar el patrón exacto. Si es inconsistente, preguntar.
- **Evidencia**: Visto en 4+ cuentas, 2026.

### Renombrar una campaña no actualiza su custom parameter de tracking
- **Tipo**: gotcha de API
- **Por qué**: si el UTM se construye con `{_campaignname}`, el parámetro conserva el nombre viejo. La campaña sale con ceros en todo cruce por `utm_campaign`.
- **Cómo detectarlo**: `SELECT campaign.id, campaign.name, campaign.url_custom_parameters FROM campaign` y comparar.
- **Qué hacer**: actualizar el parámetro tras cada rename. La máscara reemplaza la lista entera: reenviar todos los parámetros.
- **Evidencia**: Visto en 1 cuenta, sep 2026.
