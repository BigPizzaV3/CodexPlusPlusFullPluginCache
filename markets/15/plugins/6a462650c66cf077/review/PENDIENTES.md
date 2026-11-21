# Conexión con Render — versión 1.2.50

Paquete nuevo: ia-camba-render-traductor-diccionario. El cambio de servidores MCP exige cargarlo como nuevo complemento desde el listado general. Nombre visible: IA camba. No sustituye ni elimina los complementos anteriores.

Servidor MCP: https://ia-camba-servidor.onrender.com/mcp
Autenticación: none. Sin cuenta adicional de IA camba.

Se preservó el contenido completo de traducción de 1.2.49 y el icono original. Se añadieron los acuerdos guardados de consulta directa, continuidad entre letras y búsqueda inversa con definición documental. Cinco casos positivos y tres negativos.

Verificación técnica del servidor: health versión 0.2.5, tools/list con ambas herramientas y anotaciones. Consulta directa ni bola devuelve definición y vecinos reales. Los resultados de las cinco llamadas técnicas se detallan abajo; no equivalen a validar las respuestas finales dentro de ChatGPT. Casos negativos y escaneo del portal: no ejecutados en esta versión.

Las cuatro páginas informativas y la página del vídeo se conservaron. Su acceso no pudo volver a verificarse desde esta sesión: HTTP 403. No implica que fallen en el navegador del autor. La demostración corresponde al material existente; cobertura y reproducción para esta nueva conexión pendientes de confirmar.

Pendiente: cargar como nuevo complemento, verificar dominio y configuración, comprobar enlaces y vídeo accesibles a revisores, ejecutar pruebas finales del host y escaneo del portal, revisar países e identidad, y completar las declaraciones del autor. No enviado a revisión ni publicado.

No se modificó el servidor ni su límite vigente. Los límites acordados de 80 consultas por usuario y traducciones sin cuota propia todavía requieren implementación y validación de identidad.

Resultados técnicos:
[
  {
    "tool": "preparar_traduccion",
    "query": "texto Nivel 1",
    "status": "ready",
    "entry": null,
    "match_type": null
  },
  {
    "tool": "consultar_entrada",
    "query": "murure",
    "status": "found",
    "entry": "mururé",
    "match_type": "exact"
  },
  {
    "tool": "consultar_entrada",
    "query": "sin dinero",
    "status": "found",
    "entry": null,
    "match_type": null
  },
  {
    "tool": "consultar_entrada",
    "query": "canita al ire",
    "status": "found",
    "entry": "echar una canita al aire",
    "match_type": "approximate"
  },
  {
    "tool": "consultar_entrada",
    "query": "zxqv987sinentrada",
    "status": "not_found",
    "entry": null,
    "match_type": null
  }
]


## Actualización 1.2.51
El portal mostró Render configurado, dominio verificado, ambas herramientas detectadas y escaneo MCP sin observaciones para 1.2.50. Este ZIP requiere cargar una nueva versión del MISMO complemento de Render, no crear otro ni cambiar su servidor.
Se añadieron instrucciones educativas y tres casos negativos. Se conservan cinco positivos. La nota review/CONTEXTO-REVISION.txt puede copiarse en Additional Submission Context; no es una declaración de que todas las salvaguardas ya fueron probadas.
Después de cargar 1.2.51, comprobar configuración, metadatos, nuevos escaneos y comportamiento en ChatGPT. La grabación existente puede no cubrir estos nuevos casos. Permanecen las comprobaciones de enlaces y vídeo, el alcance por edades y las declaraciones personales del autor. No marcar casillas automáticamente ni afirmar que la aprobación está garantizada.
