#!/usr/bin/env python3
"""Consulta pública de Open-Meteo para una ciudad de Chile; salida JSON UTF-8."""
import json
import sys
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


LABELS = {
    0: "Despejado", 1: "Mayormente despejado", 2: "Parcialmente nublado", 3: "Nublado",
    45: "Niebla", 48: "Niebla con escarcha", 51: "Llovizna ligera", 53: "Llovizna",
    55: "Llovizna intensa", 61: "Lluvia ligera", 63: "Lluvia", 65: "Lluvia intensa",
    71: "Nieve ligera", 73: "Nieve", 75: "Nieve intensa", 80: "Chubascos ligeros",
    81: "Chubascos", 82: "Chubascos intensos", 95: "Tormenta",
    96: "Tormenta con granizo", 99: "Tormenta con granizo",
}


def fetch(base, params):
    url = base + "?" + urlencode(params)
    with urlopen(Request(url, headers={"User-Agent": "ElTiempoEnChile/0.1"}), timeout=12) as response:
        return json.load(response)


def quality(aqi):
    if not isinstance(aqi, (int, float)):
        return "No disponible"
    for limit, label in [(20, "Buena"), (40, "Aceptable"), (60, "Moderada"),
                         (80, "Deficiente"), (100, "Mala")]:
        if aqi <= limit:
            return label
    return "Muy mala"


def query(city):
    locations = fetch("https://geocoding-api.open-meteo.com/v1/search", {
        "name": city, "count": 5, "language": "es", "countryCode": "CL"})
    matches = locations.get("results", [])
    if not matches:
        raise ValueError("Ciudad no encontrada en Chile.")
    place = matches[0]
    coords = {"latitude": place["latitude"], "longitude": place["longitude"]}
    weather = fetch("https://api.open-meteo.com/v1/forecast", {
        **coords, "timezone": "auto", "forecast_days": 5,
        "current": "temperature_2m,apparent_temperature,relative_humidity_2m,weather_code,wind_speed_10m",
        "hourly": "temperature_2m,weather_code,precipitation_probability",
        "daily": "weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max,uv_index_max",
    })
    try:
        air = fetch("https://air-quality-api.open-meteo.com/v1/air-quality", {
            **coords, "current": "european_aqi", "timezone": "auto"})
        aqi = air.get("current", {}).get("european_aqi")
    except (HTTPError, URLError, TimeoutError, ValueError):
        aqi = None
    current, hourly, daily = weather["current"], weather["hourly"], weather["daily"]
    now = current["time"]  # Todos los tiempos locales se entregan en la zona de la ciudad.
    hours = [{"hora_local": time, "temperatura_c": hourly["temperature_2m"][i],
              "condicion": LABELS.get(hourly["weather_code"][i], "Condiciones variables"),
              "probabilidad_lluvia_pct": hourly["precipitation_probability"][i]}
             for i, time in enumerate(hourly["time"]) if time >= now][:8]
    days = [{"fecha_local": date,
             "condicion": LABELS.get(daily["weather_code"][i], "Condiciones variables"),
             "maxima_c": daily["temperature_2m_max"][i],
             "minima_c": daily["temperature_2m_min"][i],
             "probabilidad_lluvia_max_pct": daily["precipitation_probability_max"][i],
             "uv_max": daily["uv_index_max"][i]}
            for i, date in enumerate(daily["time"])]
    return {"fuente": "Open-Meteo", "consultado_utc": datetime.now(timezone.utc).isoformat(),
            "lugar": {"nombre": place["name"], "region": place.get("admin1"),
                      "pais": "Chile", "latitud": place["latitude"], "longitud": place["longitude"]},
            "zona_horaria": weather["timezone"], "hora_local": now,
            "actual": {"temperatura_c": current["temperature_2m"],
                       "sensacion_c": current["apparent_temperature"],
                       "condicion": LABELS.get(current["weather_code"], "Condiciones variables"),
                       "humedad_pct": current["relative_humidity_2m"],
                       "viento_kmh": current["wind_speed_10m"]},
            "uv_max_hoy": days[0]["uv_max"],
            "aire": {"escala": "AQI europeo", "valor": aqi, "categoria": quality(aqi)},
            "proximas_horas": hours, "cinco_dias": days,
            "otras_coincidencias": [p["name"] + ", " + p.get("admin1", "Chile") for p in matches[1:]]}


if __name__ == "__main__":
    city = " ".join(sys.argv[1:]).strip()
    if not city:
        print(json.dumps({"error": "Indica una ciudad chilena."}, ensure_ascii=False))
        sys.exit(2)
    try:
        print(json.dumps(query(city), ensure_ascii=False))
    except (HTTPError, URLError, TimeoutError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))
        sys.exit(1)
