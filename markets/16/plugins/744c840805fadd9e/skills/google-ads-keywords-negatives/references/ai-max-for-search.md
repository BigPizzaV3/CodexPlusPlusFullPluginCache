# AI Max for Search

### El reparto exacto keyword frente a AI Max sale de `keyword_view` con `segments.match_type`
- **Tipo**: gotcha de API
- **Por qué**: el enum de `segments.match_type` incluye `AI_MAX` y cuadra con la pestaña de Palabras clave. `segments.search_term_match_source` solo responde en vistas de search terms, sobre lo visible, y sesga contra AI Max.
- **Cómo detectarlo**: en una campaña, AI Max tenía 4,5 veces más conversiones en `keyword_view` que en search terms visibles. Coste de campaña menos `keyword_view` = tráfico keywordless de página.
- **Qué hacer**: nunca dar coste por conversión de AI Max desde search terms. Antes de afirmar que algo no sale por API, listar campos con `GoogleAdsFieldService`.
- **Evidencia**: Visto en 1 cuenta, oct-nov 2026.

### AI Max puede multiplicar clics sin mover conversiones y contaminar la cuenta
- **Tipo**: regla de decisión
- **Por qué**: la expansión keywordless compra clics muy baratos de intención lejana. Sube volumen de clics y baja el CPC medio de toda la cuenta.
- **Cómo detectarlo**: comprobar `enable_ai_max` antes de diagnosticar cualquier salto de CPC o de clics. Medir conversiones del embudo bajo, no solo del primer paso.
- **Qué hacer**: tratarlo como test lateral con negativas previas y lectura a 4+ semanas. Casos: clics ×13 con conversiones planas; CPC ×4 con 0 conversiones; CPL similar pero un 41-46% menos de etapas finales por euro.
- **Evidencia**: Visto en 2-3 cuentas, mar-oct 2026.

### Dos gotchas de API al activar AI Max
- **Tipo**: gotcha de API
- **Por qué**: el enum de expansión de URL es `FINAL_URL_EXPANSION_TEXT_ASSET_AUTOMATION`; `FINAL_URL_EXPANSION` no existe. Una brand list negativa en Search da `CANNOT_ATTACH_BRAND_LIST_TO_NON_QUALIFIED_SEARCH_CAMPAIGN` si AI Max aún no está activo.
- **Cómo detectarlo**: errores al enviar el criterio de marca y el update de campaña en peticiones separadas.
- **Qué hacer**: en la misma petición, el update de campaña va antes que el criterio. `AssetAutomationSetting` se construye como tipo anidado de `Campaign`.
- **Evidencia**: Visto en 1 cuenta, oct 2026.
