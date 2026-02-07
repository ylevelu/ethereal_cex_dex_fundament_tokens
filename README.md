# 🚨 Ethereal Perp Anomaly Watcher

Automated monitoring of **price anomalies between Ethereal DEX perpetual futures**
and **CEX spot prices**, with real-time alerts sent to a **Telegram channel**.

This project detects situations where a perp price on Ethereal
**deviates significantly from the broader market**
(e.g. XRP $1.00 → $1.60), which can be useful for:

- Arbitrage opportunities
- Hedging
- Liquidity / manipulation analysis
- Risk monitoring

---

## 🔍 What This Bot Does

- Loads available perpetual markets from Ethereal
- Fetches **mark / index prices** for each market
- Fetches **spot prices from CEX (CoinGecko)**
- Compares DEX vs CEX prices
- When deviation exceeds a configured threshold:
  - Automatically posts an alert to a Telegram channel
- Includes anti-spam cooldown protection
- Runs continuously (24/7)

---

## 📌 Example Telegram Alert

🚨 ANOMALY DETECTED

Pair: XRPUSD
DEX (Ethereal): $1.60
CEX (Spot): $1.00
Deviation: +60%


---

## 🧱 Project Architecture

## ethereal-watcher/
## main.py # main event loop
## config.py # configuration
## ethereal_api.py # Ethereal data fetching
## cex_api.py # CEX prices (CoinGecko)
## detector.py # anomaly detection logic
## notifier.py # Telegram notifications
## storage.py # cooldown / SQLite storage
## requirements.txt
## README.md


---

## ⚙️ Requirements

- Python **3.9+**
- Telegram Bot Token
- Telegram Channel (bot must be an admin)

---

## 🚀 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/ylevelu/ethereal_cex_dex_fundament_tokens.git
cd ethereal-watcher
2️⃣ Create a virtual environment
python -m venv venv
Linux / macOS

source venv/bin/activate
Windows

venv\Scripts\Activate.ps1
3️⃣ Install dependencies
pip install -r requirements.txt
🛠️ Configuration
Open config.py and set:

TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN"
TELEGRAM_CHANNEL = "@your_channel"
⚠️ Important:

The bot must be an admin in the channel

For private channels, use -100xxxxxxxxxx

Supported Tokens
TOKENS = {
    "BTCUSD": "bitcoin",
    "ETHUSD": "ethereum",
    "XRPUSD": "ripple",
    "SOLUSD": "solana"
}
Deviation Threshold
DEX_CEX_THRESHOLD = 0.25   # 25%
▶️ Running the Bot
python main.py
On successful startup, the bot will send:

✅ Bot started!
🧪 Quick Functionality Test
For testing purposes, temporarily lower the threshold:

DEX_CEX_THRESHOLD = 0.001
This will almost guarantee a test alert.

⚠️ Remember to restore the normal value after testing.

🧠 How It Works (Short Explanation)
Ethereal → perp mark / index price

CoinGecko → spot price

Deviation calculation:

|DEX - CEX| / CEX
If deviation exceeds threshold → Telegram alert

🔐 Anti-Spam Protection
SQLite stores last alert timestamps

One alert per symbol per cooldown interval

📦 Tech Stack
Python

requests

python-telegram-bot

SQLite

CoinGecko API

Ethereal public API

🚧 Limitations
Not a trading bot

Does not account for liquidity or funding rates (can be added)

Ethereal API endpoints may change

🔥 Future Improvements
Ethereal WebSocket (real-time monitoring)

Funding rate & OI filters

Wick / spike detection (X% in Y seconds)

Auto-hedging / auto-short

Docker support

Web dashboard

```

## ⚠️ Disclaimer
## This project is provided for research and educational purposes only.
## The author is not responsible for any trading decisions or financial losses.

