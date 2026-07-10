"""Small wrapper around the open.er-api.com exchange-rate API."""

import requests


BASE_URL = "https://open.er-api.com/v6/latest"


def convert_currency(amount: float, from_cur: str, to_cur: str) -> float | None:
    """Convert an amount between currencies, or return None for invalid codes."""
    from_cur = from_cur.upper()
    to_cur = to_cur.upper()

    try:
        response = requests.get(f"{BASE_URL}/{from_cur}", timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get("result") != "success":
            return None

        rate = data.get("rates", {}).get(to_cur)
        if rate is None:
            return None

        return amount * rate
    except (requests.RequestException, ValueError, TypeError):
        return None
