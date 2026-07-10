"""Small wrapper around the OpenWeatherMap current weather API."""

import requests

from config import OPENWEATHERMAP_API_KEY


WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
COUNTRY_CAPITAL_URL = "https://countriesnow.space/api/v0.1/countries/capital"


def _get_weather_for_city(city: str) -> dict | None:
    """Return current weather details for one city."""
    try:
        response = requests.get(
            WEATHER_URL,
            params={
                "q": city,
                "appid": OPENWEATHERMAP_API_KEY,
                "units": "metric",
            },
            timeout=10,
        )

        if response.status_code == 404:
            return None

        response.raise_for_status()
        data = response.json()

        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
        }
    except (requests.RequestException, KeyError, IndexError, ValueError):
        return None


def _get_country_capital(country: str) -> str | None:
    """Look up a country's capital without requiring another API key."""
    try:
        response = requests.post(
            COUNTRY_CAPITAL_URL,
            json={"country": country},
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()

        if data.get("error"):
            return None

        return data.get("data", {}).get("capital")
    except (requests.RequestException, AttributeError, ValueError):
        return None


def get_weather(city: str) -> dict | None:
    """Get weather for a city, or for a country's capital as a fallback."""
    if not OPENWEATHERMAP_API_KEY:
        return None

    weather = _get_weather_for_city(city)
    if weather:
        return weather

    capital = _get_country_capital(city)
    if not capital:
        return None

    weather = _get_weather_for_city(capital)
    if weather:
        weather["city"] = f"{city} (capital: {capital})"

    return weather
