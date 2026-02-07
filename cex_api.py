import requests
from config import TOKENS

COINGECKO = "https://api.coingecko.com/api/v3/simple/price"

def get_cex_prices():
    ids = ",".join(TOKENS.values())
    r = requests.get(
        COINGECKO,
        params={"ids": ids, "vs_currencies": "usd"},
    )
    r.raise_for_status()
    j = r.json()

    prices = {}
    for sym, cg_id in TOKENS.items():
        prices[sym] = j.get(cg_id, {}).get("usd", 0)
    return prices
