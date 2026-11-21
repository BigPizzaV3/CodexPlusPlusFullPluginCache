# Fina — paquete público para revisión de OpenAI

Archivo: `fina-chatgpt-1.0.7.zip`. Nombre interno y visible: **Fina**.

Esta versión incorpora el enlace de grabación proporcionado por Steve:
https://youtu.be/5sr3Yst9W_0

Está guardado en `extensions.com.openai.review.demo_recording_url` dentro de
`plugin.json`, como exige el aviso del portal. Conserva las ocho skills, el
servidor MCP remoto, los cinco casos positivos, los tres negativos, el icono,
la licencia, las traducciones y la disponibilidad de la versión pública 1.0.6.
No incluye la vinculación personal del paquete privado Fina Web.

## Carga en el borrador existente

1. Abre Fina en OpenAI Platform → Plugins, en la organización correspondiente.
2. Usa **Upload new version / Reupload draft** y selecciona este ZIP completo.
3. Comprueba que la versión guardada sea 1.0.7 y que **Supporting review content**
   muestre el enlace. El aviso de URL ausente debería desaparecer al importar
   correctamente el manifiesto; no es un resultado ya observado en el portal.
4. Revisa las credenciales privadas de la cuenta de prueba, el estado de la
   conexión MCP, los escaneos y las declaraciones que solicite el portal.
   El reemplazo del borrador puede requerir aceptar nuevamente declaraciones.
5. Envía a revisión tú cuando el portal no muestre requisitos pendientes.
   La carga del ZIP y el envío no equivalen a aprobación ni publicación.

## Grabación y resultados

El requisito documentado es una URL accesible al revisor; no especifica un
proveedor único. Para YouTube, deja el video **No listado** o público y comprueba
que se pueda abrir sin tu sesión ni permisos especiales. Un video privado al
que el revisor no tenga acceso no cumple ese requisito.

Por solicitud expresa de Steve, el agente no revisó el contenido del video ni
certificó su reproducción o permisos. La URL fue aportada por el propietario.
El informe de funcionamiento de la prueba privada no se convierte en resultados
individuales aprobados: las hojas conservan el estado de verificación pendiente.
Las pruebas web tampoco certifican otras superficies.

Las credenciales e instrucciones de acceso se entregan únicamente en los campos
privados del portal, nunca en el ZIP. Este paquete no configura el acceso del
revisor ni certifica el cumplimiento de las declaraciones del publicador.

Referencias oficiales:
- https://developers.openai.com/plugins/deploy/submission#complete-review-information
- https://developers.openai.com/plugins/deploy/submission#configure-onboarding-review-and-publication

El agente preparó y validó el archivo local. No lo subió ni lo envió a revisión.
