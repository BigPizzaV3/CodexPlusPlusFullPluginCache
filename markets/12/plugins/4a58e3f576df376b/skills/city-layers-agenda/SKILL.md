---
name: city-layers-agenda
description: Busca o consulta eventos publicados de City Layers XR cuando la persona pida agenda, actividades, eventos XR o detalles de un evento de City Layers.
---

# Agenda pública de City Layers XR

Usa `list_events` para consultas generales sobre eventos publicados. Usa
`get_event` cuando el usuario indique un identificador concreto. Nunca intentes
crear, editar, archivar, borrar ni publicar eventos: esta integración es
estrictamente pública y de solo lectura.

Resume los resultados de manera clara, indicando fecha, lugar, modalidad y
enlace cuando estén disponibles. Si no hay coincidencias, dilo sin inventar
eventos ni datos.
