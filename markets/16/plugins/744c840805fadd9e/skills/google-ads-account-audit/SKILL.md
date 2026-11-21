---
name: google-ads-account-audit
description: "Workflow de auditoría de una cuenta de Google Ads en solo lectura: universo de campañas, conversiones, targets, estructura, keywords, negativas, search terms, presupuesto, anuncios, configuración e historial de cambios. Usar al recibir una cuenta nueva o en la revisión anual de una cuenta activa."
---

# Auditoría de cuenta

Workflow de Fiera para auditar una cuenta de Google Ads. Sale de las cuentas que gestionamos a diario.

## Cómo usarlo

- Si existe `account-context.md` para la cuenta (lo crea la skill `google-ads-account-context`), léelo antes del paso 1. Si no existe, propón crearlo primero.
- **Solo lectura.** La auditoría no cambia nada en la cuenta. No lances mutaciones, ni siquiera con `validate_only`. Las acciones van al informe para que una persona las apruebe.
- Sigue los pasos de `references/auditoria-de-cuenta.md` en orden. El paso de conversiones va antes que el resto porque invalida lo demás.
- Cada paso cita las reglas que aplica. Están en las otras skills de este paquete (`google-ads-api-gotchas`, `google-ads-keywords-negatives`, `google-ads-copy-assets-pmax`, `google-ads-bidding-measurement`). Si están instaladas, léelas al llegar al paso.
- Cada hallazgo del informe lleva su cifra y su base.

## Índice

### `references/auditoria-de-cuenta.md`: Auditoría de cuenta
- Pasos, entradas, salida y reglas que aplica.
