# Tracking y gclid

### Desde el 15-jun-2026, los imports offline y Enhanced Conversions for Leads nuevos van por Data Manager API
- **Tipo**: gotcha de API
- **Por qué**: Google bloqueó esas subidas en la Google Ads API para los usuarios nuevos de la API. Quien ya importaba puede seguir mientras migra (blog de Google Ads Developers, 15-may-2026). Desde abr-2026 acepta datos de usuario de tag, Data Manager y API a la vez. Server-side tagging no exime del consent.
- **Cómo detectarlo**: buscar código que use `ConversionUploadService` o `upload_click_conversions`.
- **Qué hacer**: migrar a Data Manager API. Revisar uploaders anteriores a mediados de 2025.
- **Evidencia**: Cambio documentado por Google, may 2026.
