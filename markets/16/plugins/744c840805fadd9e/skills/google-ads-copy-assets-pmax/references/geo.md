# Geo

### Excluir una ubicación que ya es positiva da `IMMUTABLE_FIELD`
- **Tipo**: gotcha de API
- **Por qué**: hay dos mecanismos. Añadir negativa solo vale si la ubicación no está en la lista positiva.
- **Cómo detectarlo**: listar `campaign_criterion` LOCATION positivos antes de excluir.
- **Qué hacer**: si es positiva, quitarla primero. Mutaciones de geo siempre con `partial_failure = True`. Excluir de verdad es criterio negativo, no un ajuste de -100%.
- **Evidencia**: Visto en 2-3 cuentas, 2026.

### `geo_target_type_setting` se fija para positivos y negativos por separado
- **Tipo**: gotcha de API
- **Por qué**: el default `PRESENCE_OR_INTEREST` mete tráfico de fuera interesado en la zona. Campañas nuevas creadas con otro valor que la cuenta optimizan distinto.
- **Cómo detectarlo**: `campaign.geo_target_type_setting.positive_geo_target_type` y `negative_geo_target_type`.
- **Qué hacer**: para negocios atados a un territorio, `PRESENCE`. Replicar los dos campos de la campaña de referencia.
- **Evidencia**: Visto en 2-3 cuentas, 2026.

### La región de la analítica tiene que casar con la ubicación de Google Ads
- **Tipo**: error de método
- **Por qué**: regiones vecinas mostraron ratios de conversión de Ads frente a negocio de 0,12 a 1,57. La fuente de región del cliente no separa bien.
- **Cómo detectarlo**: conversiones de plataforma frente a eventos de negocio por región, y tasa por habitante.
- **Qué hacer**: agrupar en bloque las regiones que no cuadran. Preguntar al cliente qué fuente usa para la región.
- **Evidencia**: Visto en 2-3 cuentas, jun-oct 2026.
