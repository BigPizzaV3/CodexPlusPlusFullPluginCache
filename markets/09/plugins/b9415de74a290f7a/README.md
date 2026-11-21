# Habyt para ChatGPT — producción

Este paquete conecta ChatGPT con el MCP remoto de Habyt en producción. No contiene secretos ni reemplaza la autorización OAuth individual de cada persona.

## Identidad de la app

- Nombre: **Habyt**
- Descripción corta: **Gestiona tu lealtad digital**
- Categoría: **Productivity**
- Logotipo: `assets/habyt-logo.png`
- Color de marca: `#5AFF01`

## Qué puede hacer

- Consultar plan, tarjetas, clientes, pases, sucursales, gerentes y estadísticas.
- Crear y actualizar tarjetas desde plantillas, incluyendo imágenes adjuntas.
- Registrar sellos, puntos, recargas, canjes y ventas directas.
- Preparar y enviar notificaciones, administrar reglas automatizadas y geo-push.
- Crear o actualizar sucursales y editar configuraciones disponibles.

Las acciones que modifican datos usan el flujo de confirmación de Habyt: el chat prepara un resumen y solo ejecuta después de una confirmación explícita.

## Alta en ChatGPT

1. Crea una app MCP personalizada en el workspace de ChatGPT que tendrá acceso a Habyt.
2. Carga este paquete y selecciona el servidor MCP remoto incluido en `mcp.json`.
3. Configura OAuth y registra exactamente la URL de retorno que entregue ChatGPT en las URLs permitidas del proveedor de autenticación de Habyt.
4. Ejecuta **Scan Tools**, autentícate con una cuenta owner de Habyt y habilita las acciones que el equipo aprobará.
5. Prueba primero en borrador. En un chat nuevo, pide: `Usa Habyt para decirme qué plan tengo y cuáles son mis tarjetas activas.`
6. Publica solo después de confirmar las herramientas de lectura y una acción de escritura con confirmación.

El catálogo de herramientas lo publica el servidor MCP en el momento de **Scan Tools**. Si el servidor cambia, actualiza las acciones desde ChatGPT antes de usar las nuevas capacidades.
