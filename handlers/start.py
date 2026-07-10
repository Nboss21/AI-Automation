"""Handlers for /start and /help."""

from telegram import Update
from telegram.ext import ContextTypes


WELCOME_MESSAGE = """Welcome to Foundations Bot! 👋

I can look up weather, news, and currency conversions. Send /help to see examples."""


HELP_MESSAGE = """Foundations Bot commands:

/weather <city or country name>
Example: /weather Adama
Country example: /weather Ethiopia

/news
Example: /news

/convert <amount> <from> <to>
Example: /convert 100 USD ETB

/help
Show this guide again."""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Welcome a new user and show the available commands."""
    if update.message:
        await update.message.reply_text(WELCOME_MESSAGE)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show every command with an example."""
    if update.message:
        await update.message.reply_text(HELP_MESSAGE)
