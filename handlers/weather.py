"""Handler for the /weather command."""

from telegram import Update
from telegram.ext import ContextTypes

from services.weather_api import get_weather


async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Reply with weather for the supplied city or country's capital."""
    if not update.message:
        return

    if not context.args:
        await update.message.reply_text("Usage: /weather <city or country name>")
        return

    location = " ".join(context.args)
    weather_data = get_weather(location)

    if not weather_data:
        await update.message.reply_text(
            "Couldn't find that city or country — check the spelling and try again."
        )
        return

    temperature = weather_data["temperature"]
    await update.message.reply_text(
        f"🌤 Weather in {weather_data['city']}: {temperature:g}°C, "
        f"{weather_data['description']}, {weather_data['humidity']}% humidity"
    )
