# PrecioReal 0.1.2

Plugin MCP de consulta con una interfaz interactiva: búsqueda, presupuesto, variantes, tiendas, vendedores, estado e historial de una oferta.

El endpoint público es https://precioreal.com/mcp. No requiere autenticación ni contiene operaciones de compra, alertas o acceso a cuentas personales.

Para generar el paquete de producción:

```sh
npm run chatgpt:package
```

El ZIP se crea en plugins/precioreal/dist/. Para desarrollo puede usarse CHATGPT_MCP_URL=http://localhost:8787/mcp; el servidor independiente se inicia con npm run chatgpt y la configuración habitual del catálogo.

El endpoint está desplegado. La distribución en el directorio de ChatGPT depende de la revisión y aprobación de OpenAI. El vídeo muestra la UI conectada al MCP público desde un banco de prueba local, sin simular una sesión de ChatGPT.

Consulta docs/chatgpt-app.md en el repositorio para configuración, estado de publicación y pruebas. El paquete no contiene credenciales ni datos del catálogo.

El titular es DIGITAL LINK MARKETING S.L., según https://precioreal.com/aviso-legal. El nombre del desarrollador del paquete debe coincidir con la identidad empresarial verificada en OpenAI. Esta versión corrige los metadatos; no acredita por sí sola la verificación ni la aprobación del directorio.
