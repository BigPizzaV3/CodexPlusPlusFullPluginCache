# El Tiempo en Chile — plugin para ChatGPT y Codex

Conversión de la extensión de Chrome adjunta en un plugin de habilidad, sin servidor ni claves. El script incluido consulta Open-Meteo para ciudades chilenas y devuelve JSON para respuestas conversacionales. Se conservan tiempo actual, ocho horas, cinco días, humedad, viento, UV diario y AQI europeo.

## Prueba local

`python3 skills/pronostico-chile/scripts/forecast.py Santiago`

Requiere Python 3.9+ y acceso HTTPS a los tres dominios de Open-Meteo. La habilidad puede recurrir a la navegación web disponible cuando no hay ejecución Python. En un entorno sin red o sin acceso a herramientas web, debe comunicar que no puede verificar el pronóstico actual. No conserva la última ciudad ni reproduce el popup Chrome.

## Publicación

La creación privada permite probar el plugin. Para la ficha pública en el portal de envíos de OpenAI se requiere identidad de desarrollador verificada, logo e ícono, prompts de inicio, revisión de la habilidad y declaraciones de políticas; el envío pasa por revisión. Para un ZIP `Skills only`, las URL de sitio, soporte, privacidad y términos son opcionales según la referencia de errores del portal; son obligatorias para un envío remoto `With MCP`. El formulario puede solicitar escenarios de prueba: prepara cinco positivos y tres negativos. El script no configura automáticamente una herramienta MCP en ChatGPT; para una API garantizada en todos los entornos habría que desplegar un servidor MCP HTTPS y presentar `With MCP`.

### Prompts de inicio

- ¿Cómo estará el tiempo en Santiago hoy?
- ¿Lloverá mañana en Valparaíso?
- Dame temperatura, UV y calidad del aire en Concepción.
- Compara los próximos cinco días en Temuco y Puerto Montt.

### Casos para revisión

Positivos: Santiago actual; Valparaíso lluvia mañana; Concepción UV y AQI; Temuco cinco días; comparación Temuco y Puerto Montt. Negativos: ciudad ausente (pedir ciudad); ciudad fuera de Chile (rechazar coincidencia); servicio inaccesible (no inventar valores y explicitar fallo). Los resultados dependen de datos actuales y no contienen valores fijos esperados.

Datos consultados: ciudad escrita por la persona y coordenadas devueltas por Open-Meteo. No hay cuenta, cookies ni secretos en este plugin. Antes de enviarlo al directorio público, publicar documentos legales acordes al tratamiento real y completar los enlaces de la ficha.
