# Cliente Python

### `validate_only` y `partial_failure` van en el objeto request, no como kwargs
- **Tipo**: gotcha de API
- **Por qué**: `svc.mutate_x(customer_id=..., operations=..., validate_only=True)` lanza `TypeError`. El fallo aparece en ejecución, a veces después de haber creado recursos.
- **Cómo detectarlo**: `TypeError: got an unexpected keyword argument 'validate_only'`.
- **Qué hacer**:
  ```python
  req = client.get_type("MutateCampaignsRequest")
  req.customer_id = cid
  req.operations.extend(ops)
  req.validate_only = True      # o req.partial_failure = True
  svc.mutate_campaigns(request=req)
  ```
- **Evidencia**: Visto en 4+ cuentas, ago-sep 2026, v24, librería 31.x.

### `FieldMask` no es un tipo del cliente de Google Ads
- **Tipo**: gotcha de API
- **Por qué**: `client.get_type("FieldMask")` lanza `ValueError`.
- **Cómo detectarlo**: el error al construir un update.
- **Qué hacer**: `from google.protobuf import field_mask_pb2` y `op.update_mask.CopyFrom(field_mask_pb2.FieldMask(paths=[...]))`.
- **Evidencia**: Visto en 2-3 cuentas, ago 2026, v24.

### `field_mask(None, obj)` omite los valores por defecto y el update no hace nada
- **Tipo**: gotcha de API
- **Por qué**: `protobuf_helpers.field_mask(None, updated._pb)` solo incluye campos distintos del default de proto3. `False`, `0` y `""` no entran. El mutate devuelve OK y el valor no cambia.
- **Cómo detectarlo**: releer la entidad tras el mutate. En un caso, apagar partners devolvió OK cuatro veces sin efecto.
- **Qué hacer**: escribir las rutas a mano, o usar `field_mask(original._pb, updated._pb)`, que diffea contra el estado real. Todo script que ponga un booleano a `False` relee y falla si no cambió.
- **Evidencia**: Visto en 2-3 cuentas, sep 2026, v24.

### La ruta de la máscara tiene que ser el subcampo hoja
- **Tipo**: gotcha de API
- **Por qué**: poner un mensaje entero (`maximize_conversions`, `price_asset`, `exclusion_dimension`) devuelve `FIELD_HAS_SUBFIELDS`.
- **Cómo detectarlo**: el error nombra el mensaje.
- **Qué hacer**: usar la hoja: `maximize_conversions.target_cpa_micros`, `price_asset.price_offerings`, `exclusion_dimension.exclusions`. En `maximize_conversions`, `target_cpa_micros = 0` significa sin target.
- **Evidencia**: Visto en 2-3 cuentas, may-sep 2026, v23-v24.

### En Python 3.11+, `str()` de un enum devuelve el número
- **Tipo**: gotcha de API
- **Por qué**: los enums de proto-plus son `IntEnum`. Desde 3.11, `str(row.campaign.status)` da `'2'`, no `'CampaignStatus.ENABLED'`. El patrón `str(x).split(".")[-1]` devuelve el entero.
- **Cómo detectarlo**: estados mostrados como `2`, `3` o `4`, y comparaciones con `"ENABLED"` que nunca casan.
- **Qué hacer**: usar `.name`. En estados, 2 = ENABLED, 3 = PAUSED, 4 = REMOVED. En `KeywordMatchType`, 2 = EXACT, 3 = PHRASE, 4 = BROAD.
- **Evidencia**: Visto en 4+ cuentas, jul 2026, v23-v24.

### Rarezas de proto-plus que rompen scripts a mitad de lote
- **Tipo**: gotcha de API
- **Por qué**: asignar un string a un campo repetido lo parte en caracteres (`RESOURCE_NAME_MALFORMED: 'c'`). Los tipos anidados no salen con `get_type`. `client.enums.KeywordMatchTypeEnum` ya es el enum. `err.error_code.WhichOneof` no existe.
- **Cómo detectarlo**: errores de tipo o de resource name con un solo carácter.
- **Qué hacer**: `.append()` en repetidos. `type(client.get_type("Campaign")).AssetAutomationSetting()` para anidados. `getattr(client.enums.KeywordMatchTypeEnum, "PHRASE")`. `err.error_code._pb.WhichOneof("error_code")`.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026, v24.
