# DólarUY — paquete para revisión pública

Servidor público: https://dolaruy.matiasca89.chatgpt.site/api/mcp
Transporte: Streamable HTTP, sin autenticación ni claves.
Sitio del plugin: https://dolaruy.matiasca89.chatgpt.site
Información ampliada solicitada por el usuario: https://dolaruy.fyi/
La conexión personal creada por Sites sigue usando /mcp y su OAuth administrado por la plataforma.

## Revisión

El paquete declara exactamente un servidor, cinco casos positivos y tres negativos. La demostración técnica enlazada muestra solicitudes MCP y respuestas reales de la API; no se presenta como una conversación grabada de ChatGPT. Los resultados incluidos son una instantánea con fecha, no cotizaciones actuales para reutilizar.

El editor de OpenAI debe seleccionar la identidad verificada del publicador, completar el desafío de dominio que entregue el portal, conectar el MCP sin autenticación, revisar el escaneo y realizar las declaraciones exigidas por el formulario. La identidad visible del directorio se establece a partir de la identidad verificada elegida en el portal.

Consulta únicamente https://dolaruy.fyi/api/quotes. Compra/venta son del banco: comprar USD divide por venta; vender USD multiplica por compra. No ejecuta operaciones financieras ni recomienda inversiones. No almacena usuarios, conversaciones ni un historial individual. Para la presentación mantiene un resultado temporal cifrado, que puede incluir el banco y monto de una conversión: vence a los cinco minutos y se elimina en la siguiente operación de consulta o presentación. La infraestructura puede mantener registros técnicos de acuerdo con sus propias políticas.

## Archivos

plugin.json: manifiesto y ficha pública, políticas, soporte y casos de revisión.
mcp.json: servidor remoto público sin credenciales.
assets/logo.png: logo original de DólarUY, sin modificaciones.
review/live-results.json: evidencia de pruebas con marca temporal.

## Envío

Guía oficial: https://developers.openai.com/plugins/deploy/submission
Se requiere aprobación de OpenAI para aparecer en el directorio. Tener un ZIP válido o un sitio público no equivale a haber enviado o publicado el plugin en el directorio.

La versión 1.0.9 define un flujo de dos pasos: consultar_dolaruy obtiene datos y una referencia de 39 caracteres sin HTML; mostrar_resultado recibe solo presentacion_token y recupera el resultado original cifrado sin otra consulta HTTP. Este argumento conserva el contrato de la conexión instalada. Solo mostrar_resultado enlaza UI. Las consultas intermedias no montan tarjetas. Las cotizaciones no incluyen formulario ni acción de conversión. El editor aparece solo en un resultado de conversión solicitado. Actualizar y el editor de conversión actualizan la tarjeta existente mediante auxiliares app-only/private sin tokens ni instrucciones de presentación.

Los metadatos de visibilidad MCP Apps y ChatGPT están alineados. Las dos herramientas del chat son públicas para el modelo; los cuatro auxiliares conservan sus nombres para widgets anteriores y son privados para el modelo. Los recursos v1–v12 siguen disponibles.

Las pruebas del catálogo y del componente cubren dos consultas repetidas, una presentación final y las acciones locales. No fuerzan una única tarjeta para ocultar montajes extra. No acreditan por sí solas las decisiones del modelo o el comportamiento de ChatGPT Android. El envío al directorio sigue pausado hasta confirmar la prueba del plugin personal. Las instrucciones y los casos del paquete señalan explícitamente que el paso de presentación es necesario para completar una respuesta con tarjeta.

Si falla la presentación, las instrucciones piden responder en texto con los datos consultados y finalizar sin más herramientas. La tarjeta acepta las notificaciones estándar y la salida de compatibilidad de ChatGPT; si no recibe resultado, deja de esperar y muestra el fallo sin volver a consultar.
