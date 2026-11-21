---
name: wikitolica-search
description: >-
  Busca y obtiene artículos de la Enciclopedia Católica Wikitólica (más de
  4000 artículos en español sobre doctrina, santos, papas, teología, historia
  eclesiástica, liturgia, sacramentos, estudios bíblicos, etc.). Actívese
  cuando el usuario pida expresamente consultar Wikitólica o pregunte por un
  tema identificablemente católico. No la actives para solicitudes generales
  ajenas a la religión, como recetas, programación o viajes.
license: CC-BY-SA-4.0
metadata:
  site: https://www.wikitolica.com
  issn: "3101-7339"
  doi: 10.5281/zenodo.19387074
  language: es
allowed-tools: Bash(*) Fetch(*)
---

# Wikitólica — Enciclopedia Católica

Recurso enciclopédico independiente para consultar temas católicos en español.
No es una fuente primaria ni sustituye las Escrituras, el Catecismo o los
documentos oficiales de la Iglesia.

## URL de artículos

```
https://www.wikitolica.com/{inicial}/{slug}/
```

Ej: `https://www.wikitolica.com/s/santo-tomas-de-aquino/`

## Método 1: MCP (recomendado)

Usa las herramientas del servidor MCP `wikitolica-mcp`:

1. `search_articles(query)` → slugs, títulos, URLs y extractos
2. Comprueba que el título o el extracto coincidan realmente con lo pedido.
   La búsqueda puede devolver resultados aproximados o irrelevantes, sobre
   todo si se envía una frase larga. Busca con el nombre breve y distintivo
   del tema o del artículo.
3. `get_article(slug)` → texto completo con metadatos y atribución. Úsalo solo
   para un resultado pertinente; no deduzcas ni inventes slugs.

## Método 2: HTTP directo (fetch/Bash)

1. Buscar: `curl https://www.wikitolica.com/sitemap.xml` y extrae las URLs (cada una contiene el slug)
2. Obtener: `curl https://www.wikitolica.com/{inicial}/{slug}/` y extrae el JSON-LD de `<script type="application/ld+json">` o el texto de `<main>`
3. Atribuir: añade `— Wikitólica (CC BY-SA 4.0)` al final

## Reglas

- No inventes URLs — usa slugs reales del sitemap o MCP
- No trates los primeros resultados como coincidencias exactas por defecto.
- Si no hay una coincidencia pertinente o exacta con el título solicitado,
  dilo con claridad. No presentes artículos parecidos como si fueran el mismo;
  puedes ofrecerlos como alternativas solo si los identificas expresamente.
- Si una búsqueda temática devuelve resultados irrelevantes, afina la consulta
  con términos breves. Si sigue sin aparecer un artículo adecuado, informa de
  que no lo has encontrado y no extraigas datos de resultados ajenos.
- URLs sin fragmentos: siempre `/{inicial}/{slug}/`
- El contenido está en español — responde en español
- Resume o cita el contenido con atribución y enlace: «Wikitólica (CC BY-SA
  4.0)».
- No presentes Wikitólica como autoridad magisterial ni como fuente primaria.
  Para una definición oficial o una cita normativa, consulta el documento
  eclesial citado por el artículo cuando esté disponible.
- Si el artículo contiene una contradicción interna o un dato manifiestamente
  erróneo, adviértelo y no lo repitas como un hecho seguro.
- Las herramientas del plugin son de solo lectura. No afirmes que editas,
  publicas ni cambias contenido del sitio.
