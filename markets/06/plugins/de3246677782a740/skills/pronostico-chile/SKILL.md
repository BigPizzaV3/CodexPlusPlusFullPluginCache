---
name: pronostico-chile
description: Consulta y explica el pronóstico actual, por horas y de cinco días para ciudades de Chile usando Open-Meteo. Úsala cuando pidan tiempo, lluvia, UV o calidad del aire en Chile.
---

# El Tiempo en Chile

Cuando la persona solicite el tiempo en una ciudad chilena:

1. Si falta la ciudad, pregunta cuál desea consultar. Nunca infieras su ubicación ni pidas geolocalización precisa.
2. Si hay ejecución de Python y acceso a Internet, ejecuta `python3 scripts/forecast.py "Nombre de la ciudad"` desde el directorio de esta habilidad. Si el entorno no incluye el archivo, utiliza las tres API de Open-Meteo indicadas en `references/api.md` mediante la herramienta web disponible. No inventes resultados si el entorno impide acceder a datos actuales.
3. Presenta lugar, fecha y hora local de los datos; condición, temperatura y sensación térmica; humedad, viento, UV máximo del día y AQI europeo con su escala. Resume próximas ocho horas y hasta cinco días solo cuando se solicite ese detalle o aporte valor. Separa pronóstico de observaciones actuales.
4. Indica la fuente Open-Meteo y el momento de consulta. Si falta calidad del aire, comunica «no disponible» y conserva el pronóstico. Si una ciudad coincide con varias ubicaciones, aclara cuál localidad resolvió el geocodificador.
5. Evita afirmar que el plugin da avisos oficiales, alertas de emergencia o mediciones de una estación local. Para decisiones críticas, recomienda consultar organismos oficiales.

La extensión original guardaba la última ciudad en Chrome. Este plugin no tiene acceso a ese almacenamiento: usa una ciudad dada en la conversación actual. No expongas ni solicites claves API; Open-Meteo permite estas consultas públicas.
