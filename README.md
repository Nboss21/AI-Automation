# Foundations Bot

> A friendly Telegram bot for checking the weather, reading top headlines, and converting currencies — built with Python.

Foundations Bot is a small, beginner-friendly project that demonstrates how to build a useful Telegram bot with external APIs. Type a command, get a clean response, and learn how handlers, services, environment variables, and API calls fit together.

## What can it do?

| Command | Description | Try it |
| --- | --- | --- |
| `/start` | Welcomes users and introduces the bot. | `/start` |
| `/help` | Shows all commands with examples. | `/help` |
| `/weather <city or country>` | Shows current weather for a city, or a country's capital. | `/weather Adama` |
| `/news` | Displays the latest five US top headlines. | `/news` |
| `/convert <amount> <from> <to>` | Converts currencies using three-letter codes. | `/convert 100 USD ETB` |

### Example responses

```text
🌤 Weather in Adama: 24°C, clear sky, 40% humidity

📰 Top Headlines:
1. Example headline — Example News
   https://example.com/story

💱 100 USD = 5,420.00 ETB
```

## Built with

- **Python 3.11+**
- [python-telegram-bot](https://docs.python-telegram-bot.org/) for Telegram commands
- [OpenWeatherMap](https://openweathermap.org/api) for weather data
- [NewsAPI](https://newsapi.org/) for headlines
- [ExchangeRate-API](https://open.er-api.com/) for currency conversion
- `python-dotenv` for private configuration

## Quick start

### 1. Clone the repository

```powershell
git clone <your-repository-url>
cd foundations-bot
```



### 2. Create a virtual environment

```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Create your environment file

```powershell
Copy-Item .env.example .env
```

On macOS or Linux:

```bash
cp .env.example .env
```

### 5. Add your credentials

Open `.env` and add your own values:

```ini
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
NEWSAPI_KEY=your_newsapi_key
```

> **Security:** Never commit `.env` or paste API keys into GitHub issues, screenshots, or chats. If a key is exposed, revoke or regenerate it immediately.

### 6. Start the bot

```powershell
python bot.py
```

When you see the message below, the bot is ready:

```text
Foundations Bot is running. Press Ctrl+C to stop.
```

Open your bot in Telegram and send `/start`.

## Get your keys

### Telegram bot token

1. Open [@BotFather](https://t.me/BotFather) in Telegram.
2. Send `/newbot` and follow the prompts.
3. Copy the token BotFather gives you into `TELEGRAM_BOT_TOKEN`.

### OpenWeatherMap key

1. Create a free account at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).
2. Open the **API keys** section in your account.
3. Copy a key into `OPENWEATHERMAP_API_KEY`.

### NewsAPI key

1. Register at [NewsAPI](https://newsapi.org/register).
2. Copy the key from your account dashboard.
3. Add it as `NEWSAPI_KEY`.

Currency conversion needs no key.

## Test checklist

With `python bot.py` still running, send these messages to your bot:

```text
/start
/help
/weather Adama
/weather Ethiopia
/news
/convert 100 USD ETB
```

Also try the validation messages:

```text
/weather
/convert 100 USD
/convert 100 XXX ETB
```

## Project structure

```text
foundations-bot/
├── bot.py                  # Application entry point and handler registration
├── config.py               # Loads environment variables
├── handlers/               # Telegram command handlers
│   ├── start.py             # /start and /help
│   ├── weather.py           # /weather
│   ├── news.py              # /news
│   └── currency.py          # /convert
├── services/               # Small external API clients
│   ├── weather_api.py
│   ├── news_api.py
│   └── currency_api.py
├── .env.example            # Safe configuration template
├── requirements.txt
└── README.md
```

## How it works

```text
Telegram command
      ↓
Command handler
      ↓
External API service
      ↓
Formatted reply in Telegram
```

Each command is independent and the bot stores no user data or database records.

## Troubleshooting

| Problem | What to check |
| --- | --- |
| `TELEGRAM_BOT_TOKEN is missing` | Create `.env`, add the token, and restart the bot. |
| Weather cannot be fetched | Confirm `OPENWEATHERMAP_API_KEY` is valid and active. |
| Headlines cannot be fetched | Confirm `NEWSAPI_KEY` is valid and check your NewsAPI plan limits. |
| Bot does not respond | Keep the terminal running and make sure only one polling instance uses the bot token. |
| `ModuleNotFoundError` | Activate the virtual environment and run `python -m pip install -r requirements.txt`. |

## Deployment note

This project uses Telegram polling, which is perfect for local development. The bot replies only while `python bot.py` is running. To keep it online 24/7, deploy it as a background worker or long-running service and set the same three environment variables in the host's secret settings.

## Ideas for the next version

- Choose a news country or category
- Add weather forecasts
- Add inline keyboards
- Deploy with Docker or a webhook
- Add automated tests for every handler

---

Built as a foundations project: simple, readable, and ready to grow. ✨
