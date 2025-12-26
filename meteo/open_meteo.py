import httpx

GEOCODE = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST = "https://api.open-meteo.com/v1/forecast"

async def get_temperature(city: str):
    timeout = httpx.Timeout(10.0, connect=5.0)
    limits = httpx.Limits(max_connections=50, max_keepalive_connections=20)

    async with httpx.AsyncClient(timeout=timeout, limits=limits) as client:
        # 1) geocoding
        result = await client.get(GEOCODE, params={"name": city, "count": 1, "language": "ru", "format": "json"})
        result.raise_for_status()
        geo = result.json()
        if not geo.get("results"):
            return {"city": city, "error": "City not found"}

        item = geo["results"][0]
        lat, lon, tz = item["latitude"], item["longitude"], item.get("timezone", "Europe/Berlin")

        # 2) weather
        w = await client.get(FORECAST, params={
            "latitude": lat,
            "longitude": lon,
            "current_weather": "true",
            "timezone": tz,
        })
        w.raise_for_status()
        data = w.json()

        return data.get("current_weather").get("temperature")
