"""Handler for the /news command."""

from telegram import Update
from telegram.ext import ContextTypes

from services.news_api import get_top_headlines


async def news(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Reply with the five latest US top headlines."""
    if not update.message:
        return

    headlines = get_top_headlines(limit=5)

    if not headlines:
        await update.message.reply_text(
            "Couldn't fetch headlines right now. Please try again later."
        )
        return

    lines = ["📰 Top Headlines:"]
    for number, headline in enumerate(headlines, start=1):
        lines.append(f"{number}. {headline['title']} — {headline['source']}")
        lines.append(f"   {headline['url']}")

    await update.message.reply_text("\n".join(lines))
