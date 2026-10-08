---
name: publicar-carrusel
description: Úsala cuando el usuario quiera publicar o programar una imagen o un carrusel en redes sociales (Instagram, Facebook, LinkedIn, TikTok) para una de sus marcas. Sube el contenido y crea la publicación en Abency.
---

Sigue este flujo para publicar una imagen única o un carrusel. El servidor es organization-scoped, así que SIEMPRE necesitas resolver la marca primero y pasar `brand_id` en las llamadas.

1. Llama a `list_brands` y confirma con el usuario sobre qué marca publica (si no lo ha dicho ya).
2. Llama a `get_connections` con ese `brand_id` y localiza el `connection_id` de la plataforma destino (p. ej. Instagram).
3. Pide o confirma: el texto (caption), las imágenes y, si es programada, la fecha/hora (`scheduled_at` en ISO 8601 con zona horaria).
4. Llama a `get_media_upload_url` pasando el ARRAY con TODOS los nombres de archivo de una sola vez (una llamada → una URL por archivo). Sube cada archivo por HTTP directo a su URL firmada y guarda cada `media_path` devuelto.
5. Llama a `create_post` con `connection_ids`, el caption, `scheduled_at` si aplica y el media:
   - 1 imagen → `media_path` = la ruta.
   - Carrusel → `media_type = "carousel"` y `media_path` = array JSON de rutas en orden `["uploads/a.jpg", "uploads/b.jpg", ...]`.
6. Llama a `get_post_status` para confirmar el resultado y comunícalo al usuario.

Reglas importantes:
- NUNCA pases imágenes como base64 dentro de una llamada: se corrompen. Súbelas siempre con `get_media_upload_url` + HTTP. Si no puedes subir archivos, dile al usuario que suba las imágenes al compositor de Abency.
- Haz las llamadas MCP de una en una, no en paralelo.
- Publicar es una acción de cara al público: confirma el texto, las imágenes y la fecha con el usuario ANTES de llamar a `create_post`.
