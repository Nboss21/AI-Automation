"""Entry point for Foundations Bot."""

import logging

from telegram.ext import Application, CommandHandler
from telegram.ext import ContextTypes

from config import TELEGRAM_BOT_TOKEN
from handlers.currency import convert
from handlers.news import news
from handlers.start import help_command, start
from handlers.weather import weather


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
LOGGER = logging.getLogger(__name__)


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log unexpected errors and give the user a safe, friendly response."""
    LOGGER.error("Unhandled exception while processing an update", exc_info=context.error)

    message = getattr(update, "effective_message", None)
    if message:
        await message.reply_text("Something went wrong, please try again")


def main() -> None:
    """Create the Telegram application and start polling for messages."""
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("weather", weather))
    app.add_handler(CommandHandler("news", news))
    app.add_handler(CommandHandler("convert", convert))
    app.add_error_handler(error_handler)

    print("Foundations Bot is running. Press Ctrl+C to stop.")
    app.run_polling()


if __name__ == "__main__":
    main()
