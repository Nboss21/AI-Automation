"""Handler for the /convert command."""

import math

from telegram import Update
from telegram.ext import ContextTypes

from services.currency_api import convert_currency


USAGE_MESSAGE = "Usage: /convert <amount> <from> <to>  e.g. /convert 100 USD ETB"
UNKNOWN_CURRENCY_MESSAGE = "Unknown currency code — use 3-letter codes like USD, EUR, ETB."


async def convert(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Convert the supplied amount between two three-letter currency codes."""
    if not update.message:
        return

    if len(context.args) != 3:
        await update.message.reply_text(USAGE_MESSAGE)
        return

    amount_text, from_currency, to_currency = context.args

    try:
        amount = float(amount_text)
    except ValueError:
        await update.message.reply_text(USAGE_MESSAGE)
        return

    if not math.isfinite(amount) or amount <= 0:
        await update.message.reply_text(USAGE_MESSAGE)
        return

    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    if not all(code.isalpha() and len(code) == 3 for code in (from_currency, to_currency)):
        await update.message.reply_text(UNKNOWN_CURRENCY_MESSAGE)
        return

    converted_amount = convert_currency(amount, from_currency, to_currency)
    if converted_amount is None:
        await update.message.reply_text(UNKNOWN_CURRENCY_MESSAGE)
        return

    await update.message.reply_text(
        f"💱 {amount:g} {from_currency} = {converted_amount:,.2f} {to_currency}"
    )
