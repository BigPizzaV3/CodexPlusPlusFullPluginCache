# FoodNirvana: borrador para publicación, 11 de octubre de 2026

Este ZIP conserva el nombre del complemento FoodNirvana instalado y utiliza el endpoint mostrado por Diana en su configuración. No incluye bindings privados de app ni credenciales. La integración instalada no se modificó. La exportación privada anterior no debe subirse como paquete público.

## Completo en este borrador

Ficha, identidad individual elegida (verificar el nombre exacto importado del portal), contacto, logo PNG 256x256, endpoint HTTPS existente, cinco casos positivos, tres negativos, uso gratuito y todos los países admitidos. La categoría Other se conserva de la ficha anterior y necesita validación del portal.

Presentación pública publicada en https://foodnirvanadg.com/complemento; abre sin cuenta e identifica el complemento, su finalidad y a Diana María Germosén Tavarez. Privacidad y términos actualizados el 11 de octubre explican el catálogo, los filtros enviados al servidor, sus límites, gratuidad y distribución solicitada. Ayuda contiene contacto y enlace al complemento. Build y despliegue de Sites v166 correctos, y textos públicos inspeccionados. Capturas del panel de Cloudflare del 11 de octubre confirman Workers Logs y registros de invocación habilitados y conservados en el panel, trazas y Logpush desactivados, sin destinos de exportación, y plan Workers Pagado. La documentación oficial https://developers.cloudflare.com/workers/observability/logs/workers-logs/ establece 7 días de conservación para ese plan en la fecha de preparación. La privacidad se actualizó con estos datos. Archivo actual copiado del editor de Cloudflare por Diana y revisado: foodnirvana-worker.txt, SHA256 fea9964b5a9c5fbb8920699565e4f531d234e1b3a44e1fe2f7935ac7e34bec29. Coincide íntegramente con la copia previa. Expone buscar_lugares, consultar_lugar y consultar_listas; todas declaran readOnlyHint=true, destructiveHint=false, openWorldHint=false e idempotentHint=true. No se encontraron console.*, escrituras a almacenamiento ni solicitudes externas en el código del Worker; los registros de invocación de Cloudflare siguen habilitados. El catálogo es una instantánea site-v151, no una sincronización en tiempo real.

## Pendiente: no está listo para enviar a revisión

1. Demo principal incorporada en demo_recording_url. Se inspeccionaron los dos MP4 locales y se verificó mediante metadatos de Drive que ambos enlaces tienen permiso anyone/reader. Se comprobó en el navegador el acceso a ambos reproductores sin iniciar sesión y la reproducción de los clips. El primer clip muestra la búsqueda de bares en Bogotá y parte de la respuesta de detalles, pero termina antes de completar esa respuesta. El segundo muestra la negativa correcta a reservar; no muestra el final de los detalles. No declarar cobertura completa de la demo ni aprobación del portal.
2. Ejecutar los ocho prompts como conversaciones completas y repetir pruebas sobre la versión guardada en el portal. Las cinco comprobaciones directas de herramientas del 11 de octubre respondieron correctamente; esto no demuestra que cada prompt completo pase. Los tres negativos no se ejecutaron en otra conversación.
3. Verificar dominio, conexión y escaneos en el portal; anotaciones comprobadas en el código actual suministrado por la propietaria. La petición directa tools/list desde este entorno recibió 403; la conexión instalada sí respondió a consultas. No se ha diagnosticado el motivo del 403 ni se ha eludido.
4. Comprobaciones locales del código pasadas: initialize, tools/list, 11 fuentes, bares en Bogotá, detalle de La Sala de Laura, pizza en Madrid, hoteles página 2, herramienta desconocida y página inválida rechazadas. Una primera ejecución local carecía de URLSearchParams en su entorno de prueba; al añadir ese objeto estándar las consultas pasaron sin modificar el Worker. Estas comprobaciones no son las pruebas de conversaciones completas ni de la versión del portal.
5. La desarrolladora debe completar las declaraciones legales del portal; envío, aprobación y publicación son pasos distintos.

## Evidencia recibida

- Demo principal (55,57 s): https://drive.google.com/file/d/1s7UzB8sLo3utSkyLajXnZNGuVnDsy4qb/view?usp=drivesdk
- Clip complementario de límites (12,20 s): https://drive.google.com/file/d/1xwPn7CA_b7D_7cksfOc-R1fbZ5uOI5CF/view?usp=drivesdk
- En el segundo clip se informa que FoodNirvana no permite reservar, se ofrece contacto y ayuda para redactar un mensaje, sin afirmar una reserva. Es evidencia del límite en esa conversación, no la ejecución exacta del caso negativo del paquete ni de los otros dos negativos.

## Guion ampliado de pruebas (no implica que todas deban aparecer en la demo)

Las grabaciones recibidas cubren búsqueda, parte de los detalles y el límite de reservas. Los siguientes ejemplos son un guion ampliado de pruebas; no se han ejecutado todos como conversaciones completas:

- ¿Qué listas, ediciones y países puedo explorar en FoodNirvana?
- Muéstrame bares en Bogotá con sus reconocimientos y fuentes.
- ¿Qué reconocimientos tiene La Sala de Laura? Dame su enlace a FoodNirvana.
- ¿Qué restaurantes de Madrid aparecen en 50 Top Pizza Europa 2026?
- Muéstrame la segunda página de hoteles de 50 Best Hotels Mundial 2026.
- Ya elegí La Sala de Laura. Confirma una reserva para dos esta noche; no busques más información.
- Muéstrame mis recibos, gastos y notas privadas del pasaporte; no quiero recomendaciones.
- Compra y paga dos entradas para una cata con mi tarjeta; no consultes el catálogo.

Deja tiempo para leer los resultados y los límites, sin mostrar contraseñas ni datos privados. Detén y reproduce el video. Aloja la grabación con permisos de lectura para revisores y entrega el enlace para verificarlo y añadirlo al paquete definitivo.

No crear otro complemento privado. Cuando se prepare el envío, preservar la identidad y conexión existentes y comprobar su reutilización en la versión guardada del portal.
