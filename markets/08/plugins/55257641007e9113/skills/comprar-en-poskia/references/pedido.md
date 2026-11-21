# Contrato de pedido y recuperación

Contrato público POSKIA MCP 0.5.0. Los esquemas descubiertos del servidor prevalecen sobre este resumen si cambian.

## Preparar

`consultas` recibe `domain: "cotizacion"` y `order`:

- `slug` del comercio elegido.
- `items`: `product_id`, `quantity`, `notes` opcional y `modifiers` con `option_id`/`quantity` si corresponden. Usa IDs reales, conserva las selecciones padre que abren opciones anidadas y respeta grupos obligatorios y suma de cantidades máxima.
- `customer_name`, `customer_phone` (7–15 dígitos, prefijo + opcional), `address`.
- `payment_method`: `cash` o `transfer`, solo si el comercio lo admite.
- `note` opcional. No agregues instrucciones de cocina que el usuario no pidió.

No envíes precios calculados por el modelo ni un request_id inventado: el servidor calcula precios y genera la identidad del pedido. La respuesta incluye resumen, total, `quote_token`, `requires_confirmation`, `receipt_required` y vencimiento. Mantén el token exacto, en privado. No reinterpretes subtotal como total final.

## Enviar

Solo después de la confirmación del resumen mostrado: `enviar_domicilio({quote_token, confirmed: true})`, más `receipt_base64` real cuando el método es transferencia. El comprobante admite imagen JPG/PNG/WebP de hasta 5 MB; una URL, una afirmación de pago o texto generado no reemplazan los bytes del archivo.

Valida que no haya `isError`/`error`, que exista `order_id` y un estado reconocido. Guarda en el contexto el `slug`, `order_id` y `status_token` devueltos para consultar el seguimiento. No muestres los tokens en la respuesta al cliente.

## Recuperar sin duplicar

- Fallo de transporte o timeout al enviar: el resultado es incierto. Reintenta como máximo una vez con EXACTAMENTE el mismo `quote_token`, confirmación y comprobante. Nunca prepares un token nuevo mientras no sepas si el anterior creó un pedido.
- Si tienes identificador y token de seguimiento, consulta `domain=estado`; no vuelvas a enviar para conocer el estado.
- Si el segundo intento tampoco confirma el resultado, comunica la incertidumbre y detente. No inventes número de pedido, aceptación ni una nueva orden.
- Error explícito de validación, pago o disponibilidad: explica el problema concreto y corrige solo lo necesario con el usuario. No reintentes automáticamente lo mismo.
- Cotización vencida: el servidor puede devolver un pedido ya creado al reintentar el mismo token. Si informa explícitamente que no pudo crear por vencimiento, prepara de nuevo. Si el resumen cambia, pide confirmar el nuevo; si es idéntico y la confirmación del usuario sigue vigente, no la repitas.
- No reintentes automáticamente un pedido rechazado/cancelado/expirado como si fuera nuevo. Pregunta qué alternativa desea.

## Estado no es entrega

El alta normalmente queda `pending_approval`, aunque un comercio con autoaprobación puede devolver `approved`. Ninguno de esos estados demuestra entrega ni salida del domiciliario. Usa `delivery_status` del seguimiento cuando exista y comunica solo lo que respalda. No accedas a reportes privados ni al teléfono de otro cliente para recuperar pedidos.
