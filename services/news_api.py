"""Small wrapper around NewsAPI's top-headlines endpoint."""

import requests

from config import NEWSAPI_KEY


HEADLINES_URL = "https://newsapi.org/v2/top-headlines"


def get_top_headlines(country: str = "us", limit: int = 5) -> list[dict]:
    """Return the requested number of current headline summaries."""
    if not NEWSAPI_KEY:
        return []

    page_size = max(1, min(limit, 100))

    try:
        response = requests.get(
            HEADLINES_URL,
            params={
                "country": country,
                "pageSize": page_size,
                "apiKey": NEWSAPI_KEY,
            },
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()

        if data.get("status") != "ok":
            return []

        return [
            {
                "title": article.get("title", "Untitled story"),
                "source": article.get("source", {}).get("name", "Unknown source"),
                "url": article.get("url", ""),
            }
            for article in data.get("articles", [])[:page_size]
        ]
    except (requests.RequestException, ValueError):
        return []
