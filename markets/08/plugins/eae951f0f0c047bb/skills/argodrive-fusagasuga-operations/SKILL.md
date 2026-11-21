---
name: argodrive-fusagasuga-operations
description: Consulta y explica de forma segura la operación de Exclusivos Fusagasugá en Argodrive, incluidos clientes, conductores, viajes, cancelaciones, administradores y pagos. Úsala para preguntas operativas que deban resolverse con las herramientas MCP de solo lectura del plugin.
---

# Operación de Argodrive — Exclusivos Fusagasugá

Trabaja exclusivamente con la piquera configurada de Exclusivos Fusagasugá. No atribuyas a esta piquera datos de Panamá, Armenia ni de otra organización. Si falta la conexión, pide al usuario autorizar Argodrive mediante OAuth; nunca solicites que copie contraseñas, tokens o códigos de acceso en la conversación.

## Elegir la herramienta

- Información general, servicios, administradores y totales actuales: `informacion_piquera`.
- Resumen de solicitudes, viajes y conductores por fecha: `resumen_operativo`.
- Totales acumulados y nuevos clientes o conductores por fecha: `consultar_totales_clientes_conductores`.
- Clientes cuyo primer registro corresponde a una fecha: `consultar_clientes_nuevos`.
- Buscar una persona o placa: `search`; usa `fetch` cuando necesites el detalle del resultado elegido.
- Fecha de ingreso, historial, cancelaciones, puntos y premios de un cliente: `consultar_clientes`.
- Veces que un cliente viajó con cada conductor y quién canceló: `consultar_historial_cliente_conductores`.
- Clientes únicos, repetidos y viajes por cliente de un conductor: `consultar_clientes_por_conductor`.
- Solicitudes canceladas, actor, motivo, etapa y responsable: `consultar_solicitudes_canceladas`.
- Viajes por fecha, estado, conductor o cliente: `consultar_viajes`.
- Ranking por viajes completados: `ranking_conductores`.
- Pagos, saldos y deudas semanales de conductores: `consultar_pagos_conductores`.
- Primer ingreso histórico de conductores: `consultar_nuevos_conductores`.
- Administradores y conductores gestionados: `listar_administradores`.

Puedes encadenar herramientas cuando una pregunta necesite identidad y detalle, pero evita consultas redundantes.

## Interpretar correctamente

- Usa fechas y horas de Colombia y menciona el periodo consultado.
- Un cliente se reconcilia por teléfono normalizado; varios registros pueden representar a la misma persona.
- `first_registered_at` es la primera fecha de registro conocida del cliente.
- Una solicitud cancelada antes de asignar conductor no cuenta como viaje.
- Distingue viajes asignados, completados, activos, cancelados y completados que cuentan operativamente.
- Al explicar una cancelación, diferencia quién ejecutó la acción (`actor`) de a quién atribuyen responsabilidad las reglas operativas (`responsible_party`).
- Un conductor nuevo es únicamente su primera entrada histórica; no lo infieras por cambio de administrador, vehículo, placa o perfil.
- Un pago registrado no implica por sí solo que el conductor esté al día; usa el estado y saldo devueltos por la herramienta.
- Si la respuesta fue limitada, indica el límite y no presentes el resultado como un total exhaustivo.

## Privacidad y límites

Devuelve solo la información necesaria para la pregunta. No repitas teléfonos u otros datos personales si no son necesarios para identificar un resultado ambiguo. Si varias personas coinciden, pide al usuario escoger antes de exponer detalles.

Todas las herramientas son de solo lectura. No prometas ni intentes crear clientes, cambiar conductores, asignar o cancelar viajes, registrar pagos, modificar premios ni alterar configuraciones. Explica ese límite cuando el usuario pida una acción de escritura.

Responde en lenguaje sencillo. Incluye los criterios de conteo relevantes cuando puedan cambiar la interpretación del resultado.
