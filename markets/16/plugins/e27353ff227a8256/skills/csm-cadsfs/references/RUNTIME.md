# Ejecución de la habilidad

Antes de producir archivos, localizar la raíz REAL de esta habilidad y comprobar
el acceso a sus recursos y al intérprete. No asumir rutas de otro chat ni inventar
una descarga. No pedir al cliente el cookbook, el generador ni las bibliotecas.

## Camino local comprobado

Usar `scripts/run_plan.py` con `--plan <plan_datos.json> --output <entrega.csm>`.
El plan es dato ya interpretado por el agente y revisado contra el pedido, no código
del cliente. La interfaz y los ejemplos reales están en `references/test_plans/`.
El ejecutor usa NumPy. No requiere MCP, API ni servidor. Sólo procesa el perfil
comprobado de recinto extruido simple con materiales y sistemas ya resueltos.

Para diagnosticar la instalación: `--quick-test --output <prueba.csm>`. Esto genera
únicamente el caso sintético 4×3×3 m y no sustituye una petición distinta del cliente.
La ruta de salida debe ser realmente accesible para adjuntarla al chat.

Si los recursos sólo pueden leerse como texto, no reconstruir un Python diferente
ni eludir su hash: comprobar un mecanismo de acceso a bytes de la habilidad.
Si el entorno no monta scripts/archivos o no permite ejecución, informar que no
se generó el archivo. Instalación no equivale a disponibilidad de ejecución.

## Integración y correcciones

El Python original permanece intacto. El adaptador corrige la triangulación de
perímetros cóncavos, el signo del apuntado vertical cuando hay objetivo explícito,
y metadatos de geometría. No cambia cotas ni centra un perímetro ajeno a escondidas.
Exige nombres de materiales y altavoces presentes en las bibliotecas recibidas.
Los campos sin triángulos no cuentan como superficies físicas Default.

## Escenas detalladas

El ejecutor probado no compone por sí solo balcones, muebles, aberturas o escenarios.
El generador aporta primitivas y las instrucciones técnicas describen la composición.
Para una escena compleja, usar esas funciones y el cookbook sin eliminar partes
solicitadas por un límite de la interfaz sencilla. Registrar qué validaciones se
pudieron hacer; no afirmar cobertura, RT, aislamiento ni apertura en CADSFS sin
haber ejecutado esas operaciones. No tomar los 8 CSM de referencia como salidas
nuevas ni editarlos directamente.

## Resultado al cliente

Entregar exclusivamente el .csm real (o ISM sólo si se prueba su exportación),
una vista de su geometría cuando sea pertinente y pocas frases. No incluir planes,
scripts, logs, catálogo, índice, cookbook o contenido JSON en un ZIP de cliente.
Los informes de ejecución y esta guía son recursos internos, no entregables del cliente.

No adjuntar el paquete de instalación ni sus recursos al responder un pedido de
modelado. Las instrucciones de salida no equivalen a cifrado ni a un control de
acceso sobre los archivos distribuidos.
