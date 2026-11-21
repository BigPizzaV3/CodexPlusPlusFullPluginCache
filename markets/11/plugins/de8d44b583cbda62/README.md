# TuPartidoCorrupto — paquete público 0.2.0

Este paquete prepara la publicación de TuPartidoCorrupto en el directorio de ChatGPT. Contiene el manifiesto Agent Plugins, una conexión MCP y los iconos de la marca. El editor indicado es Fabrizio.

Servidor remoto: **https://tupartidocorrupto.com/mcp**, transporte Streamable HTTP, **sin autenticación**. No se necesitan cuenta de TuPartidoCorrupto, suscripción, clave de API ni OAuth. El MCP ofrece consultas públicas de solo lectura, con límites técnicos de uso; la API REST comercial del sitio es un servicio separado.

Las seis herramientas permiten buscar casos documentados, abrir sus fichas y cronologías, resumir el catálogo, consultar candidaturas, comparar propuestas y consultar indicadores económicos. Los resultados incluyen fuentes, fechas y límites de cobertura. No se modifica el catálogo, no se presentan denuncias y no se realizan recomendaciones personalizadas de voto.

La interfaz de tarjetas, comparativas y gráficos se sirve como recurso MCP Apps desde el Worker; no se duplica en este ZIP. La conversación de ChatGPT sigue las políticas y opciones del cliente, por lo que no se promete que carezca de historial.

El manifiesto incluye cinco casos positivos, tres negativos, notas de versión, ausencia de comercio y disponibilidad en todos los países admitidos por la plataforma. Los textos base están en inglés y se incluye localización es-ES.

La preparación del paquete no implica envío, aprobación ni publicación. El estado de las comprobaciones y del vídeo se mantiene en `docs/mcp-review.md` del repositorio; la arquitectura y el proceso están en `docs/mcp-chatgpt.md`. No contiene credenciales, bindings privados de apps ni hooks.
