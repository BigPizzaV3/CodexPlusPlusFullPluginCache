---
name: licitaia-public
description: Buscar y consultar fichas públicas de licitaciones españolas con MCP anónimo.
---

Usa el servidor MCP público de LicitaIA para localizar licitaciones españolas y consultar una ficha básica.

El servidor ofrece solo estas herramientas:

- `buscar_licitaciones`: filtros opcionales `query`, `provincia`, `organismo` y `cpv`; `page` solo puede ser 1 y `limit` puede ser de 1 a 5.
- `ficha_licitacion`: recibe `licitacionId` como UUID.

Al presentar resultados, conserva el título, organismo, expediente, CPV, lugar, tipo, procedimiento, estado, presupuesto o valor estimado, fechas, fuente y los enlaces `oficial` y `licitaia` que devuelva la herramienta. Indica el origen y la fecha de publicación cuando estén disponibles.

El buscador cubre publicaciones de los últimos 30 días, devuelve como máximo 5 resultados en la primera página y puede indicar truncamiento. La ficha básica por UUID no promete que la licitación esté dentro de esa ventana. Comprueba siempre el plazo y las rectificaciones en el enlace oficial.

El acceso es anónimo, de solo lectura y no incluye documentos, análisis de IA, recomendaciones, veredictos ni datos de perfil. Las credenciales no amplían este servidor. Respeta los errores de límite y reintenta más tarde cuando el servidor lo indique.
