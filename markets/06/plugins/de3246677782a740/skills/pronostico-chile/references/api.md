# Fuente y campos

- Geocodificación: `https://geocoding-api.open-meteo.com/v1/search?name=<ciudad>&count=5&language=es&countryCode=CL`.
- Pronóstico: `https://api.open-meteo.com/v1/forecast` con `latitude`, `longitude`, `timezone=auto`, `forecast_days=5`, `current=temperature_2m,apparent_temperature,relative_humidity_2m,weather_code,wind_speed_10m`, `hourly=temperature_2m,weather_code,precipitation_probability`, `daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max,uv_index_max`.
- Calidad del aire: `https://air-quality-api.open-meteo.com/v1/air-quality` con `latitude`, `longitude`, `current=european_aqi`, `timezone=auto`.

La escala de AQI europeo utilizada por la extensión: 0–20 buena, 21–40 aceptable, 41–60 moderada, 61–80 deficiente, 81–100 mala, >100 muy mala. Identificar explícitamente la escala europea para no confundirla con AQI US.

El clima es un pronóstico estimado. No presentar el valor UV diario como índice UV instantáneo.
