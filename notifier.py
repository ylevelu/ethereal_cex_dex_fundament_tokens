import asyncio
from telegram import Bot
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL

bot = Bot(TELEGRAM_BOT_TOKEN)

async def _send(text):
    await bot.send_message(chat_id=TELEGRAM_CHANNEL, text=text, parse_mode="Markdown")

def send_message(text):
    asyncio.run(_send(text))

def send_alert(symbol, dex_price, cex_price):
    text = (
        f"🚨 *ANOMALY DETECTED*\n"
        f"*Pair:* {symbol}\n"
        f"*DEX:* ${dex_price:.4f}\n"
        f"*CEX:* ${cex_price:.4f}"
    )
    send_message(text)

def send_startup():
    send_message("✅ Bot started!")
