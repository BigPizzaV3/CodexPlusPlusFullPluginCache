# Comuscopio para ChatGPT y Claude

Paquete de distribución: 1.2.8. No es la versión del motor ni de las extensiones.

## Servicio

- MCP público: https://comuscopio.com/api/mcp
- Transporte: Streamable HTTP, respuestas JSON, sin estado de sesión ni SSE persistente.
- Autenticación pública: ninguna. Datos públicos y límites de uso; las acciones de atención y avisos requieren interacción explícita.
- Idiomas: es, ca, gl, eu.
- Herramientas: search_organizations y get_organization. Sólo interfaz: organization_chat y report_search.
- Interfaz: MCP Apps, con la misma experiencia de búsqueda que la webapp.
- No se usa otra base de datos ni otro algoritmo de búsqueda.

## ChatGPT

El paquete contiene plugin.json, mcp.json, icono y casos de revisión.
Subirlo al portal de publicación de OpenAI mediante la opción para MCP remoto.
Verificar la identidad de publicación y el dominio siguiendo el desafío que muestre
el portal; no inventar un token de verificación ni sustituir desafíos existentes.
Antes de enviar, ejecutar los cinco casos positivos y los tres negativos en ChatGPT
y aportar una grabación de ese recorrido. Ya existe una demo real del panel,
pero no sustituye los casos de aceptación pendientes ni acredita su primera carga.
La publicación del Site no equivale a la aprobación en el directorio público.

Para probar la conexión manual, usa el endpoint público indicado arriba y elige
sin autenticación. No hace falta instalar el complemento privado que Sites ofrece
al propietario. No necesitas una cuenta de Comuscopio ni una clave de API.

## Claude

Para pruebas, añadir el servidor remoto en Configuración > Conectores con la URL
https://comuscopio.com/api/mcp, si la cuenta permite conectores personalizados.
No pegar el JSON de configuración en el chat ni solicitar una clave de OpenAI.
Para distribución sin configuración técnica, presentar el conector al directorio
de Anthropic. Ejecutar la búsqueda, lectura, preferencias, cuatro idiomas y errores
en Claude antes del envío. La disponibilidad depende del cliente y sus políticas.
El ZIP de OpenAI no es un instalador de Claude: ambos usan el mismo servidor MCP.

## Seguridad, privacidad y costes

Las fichas se proyectan con una lista de campos permitidos. No se devuelven CIF,
facturación, empleados, claves, historial de revisión, uso de tokens o diagnósticos.
El HTML decorativo se entrega sólo a la interfaz, fuera del contexto del modelo.
Se reconstruye con elementos permitidos y CSS filtrado dentro de un Shadow DOM
aislado. No se ejecutan scripts ni formularios. Los textos del catálogo no son instrucciones.
URLs de entrada reutilizan las validaciones y protección SSRF del buscador.
Los enlaces sólo se abren por acción de la persona. Las herramientas de búsqueda
y lectura no escriben fichas. Las herramientas exclusivas de la interfaz pueden
guardar avisos de resultados, enviar mensajes de atención y, con consentimiento,
enviar copias por correo. No recopilan el historial de conversación con el asistente.
La interfaz no envía eventos a GA4. El servidor registra
contadores técnicos agregados y límites de uso; la búsqueda usa la caché existente.
El proveedor del asistente aplica su propia política de tratamiento de conversación.

Límites: 20 herramientas/minuto y 120/hora por IP; 2.000 herramientas/día globales.
Las búsquedas nuevas con IA tienen límite adicional de 20/hora por IP y 100/día
para esta integración, además del presupuesto diario compartido del buscador.
Abrir fichas no llama al modelo. Las búsquedas en caché no generan una
nueva llamada al modelo. No cambiar estos límites para eludir restricciones del proveedor.
MCP_PUBLIC_ENABLED=false deshabilita el endpoint público sin tocar el buscador web.

## Estado de validación

Las pruebas automatizadas y la vista previa usan el protocolo real. No acreditan
por sí solas aprobación o funcionamiento observado dentro de ChatGPT y Claude.
Consultar la preparación de directorios en administración para distinguir pruebas
realizadas y pendientes. El propietario confirmó la primera carga correcta en
conversaciones nuevas de ChatGPT y Claude y aportó sus enlaces compartidos.
La prueba de ChatGPT incluye cinco capturas de móvil con el panel interactivo.
Las pruebas bajo control automatizado siguen mostrando un fallo anterior al
inicio de la interfaz; no demuestran por sí solas un defecto del servicio ni
su causa exacta. No se han desactivado protecciones ni reducido funciones para
ocultar ese resultado. Las demás pruebas de aceptación siguen pendientes.
También se puede usar directamente la webapp:
https://comuscopio.com/app.

La demo grabada muestra búsquedas y preferencias en un panel ya abierto:
idioma, ubicación de prueba, orden por distancia y restablecimiento. No es una
prueba de primera carga ni de los tres casos negativos. Las declaraciones
legales y el envío a revisión siguen pendientes del desarrollador autorizado.

Demo real, reproducible sin iniciar sesión:
https://comuscopio.com/downloads/comuscopio-chatgpt-demo-20261024.mp4
Duración: 99,72 segundos. H.264, sin audio. Sólo se recortó la espera inicial;
se conserva la captura íntegra en la evidencia local de preparación.

## Uso y soporte

Ejemplos:
- Busca con Comuscopio alternativas a https://movistar.es.
- Busco un menú vegano para una escuela en Barcelona.
- Busca cooperativas de alimentación y abre la primera ficha.

Sin resultados: describe el producto o servicio de otra forma. Si una web bloquea
la lectura, usa la extensión desde esa página o describe su actividad. Ante un
límite temporal, espera antes de repetir: no hagas reintentos ilimitados.
Las preferencias permiten cambiar idioma, ubicación opcional y orden. Se aplican
a la sesión. La similitud indica encaje, no certifica disponibilidad ni capacidad.
Soporte y seguridad: info@comuscopio.com. Indica cliente, hora y error; no envíes
claves ni conversaciones privadas. Desarrollador: https://eutopia.cat/.

## Fuentes oficiales

- https://developers.openai.com/plugins/build/chatgpt-ui
- https://developers.openai.com/plugins/deploy/submission
- https://claude.com/docs/connectors/building/submission
- https://modelcontextprotocol.io/specification/2025-11-25/basic/transports

Soporte: info@comuscopio.com. Política: https://comuscopio.com/legal.

La interfaz reutiliza panel-demo.html y panel-demo.js, sin comparación separada. Los asistentes heredan el idioma de la conversación; una elección explícita en preferencias tiene prioridad. El chat y las copias requieren interacción y consentimiento según el formulario. No se activa GA4 dentro de esta integración.

