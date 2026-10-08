# Producción e interoperabilidad

Cuando el brief esté confirmado, exista capacidad y el usuario solicite archivo final, producir PPTX editable exclusivamente con Presentations y `@oai/artifact-tool`; respetar tamaño, conteo, plantilla, idioma, notas, anexos, fuentes y branding.

Presentations es el único motor autorizado para crear slides o PPTX. No usar Gamma, Presenton ni otro generador externo como sustituto, aunque esté disponible. La disponibilidad de otro motor no modifica esta regla.

## Prioridad de objetos

1. texto nativo;
2. tablas, gráficos y diagramas nativos;
3. SVG compatible;
4. raster de calidad para fotografía o ilustración.

No rasterizar texto ni evidencia editable de forma evitable.

## Ciclo técnico

Construir → exportar → renderizar → revisar mosaico y slides críticas → validar estructura, texto, notas y objetos → corregir → rerenderizar lo afectado → liberar.

Detectar overflow, cortes, superposiciones, deformación, caracteres faltantes, bajo contraste, desalineación, inconsistencias, fuentes ausentes y objetos corruptos.

Antes de liberar, inspeccionar notas, comentarios, texto oculto, propiedades personales, rutas locales, hipervínculos, objetos incrustados y relaciones externas. Eliminar metadatos y contenido residual no necesarios, sin destruir trazabilidad requerida. Registrar el resultado; si la herramienta no permite inspeccionarlo, declarar la sanitización pendiente y bloquear entregables confidenciales o restringidos.

## Fallbacks

- Sin Presentations o `@oai/artifact-tool`: entregar storyboard/especificación de producción utilizable y declarar que el archivo no pudo generarse; no derivar a otro generador.
- Sin render: validar estructura y marcar inspección visual pendiente.
- Sin fuente: usar sustituto compatible y declarar impacto material.
- Sin activo: usar placeholder explícito; no inventar procedencia.

Verificar cada formato derivado; no asumir equivalencia entre PPTX, PDF y Google Slides.
