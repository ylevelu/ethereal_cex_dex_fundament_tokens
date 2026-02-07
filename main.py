import time
from config import TOKENS, CHECK_INTERVAL
from ethereal_api import list_products, get_mark_price
from cex_api import get_cex_prices
from detector import is_anomaly
from notifier import send_alert, send_startup
from storage import can_alert, save_alert

send_startup()

while True:
    try:
        cex = get_cex_prices()
        products = list_products()

        for p in products:
            sym = p.get("ticker")
            if sym not in TOKENS:
                continue

            dex_price = get_mark_price(sym)
            cex_price = cex.get(sym, 0)

            if is_anomaly(dex_price, cex_price):
                if can_alert(sym):
                    send_alert(sym, dex_price, cex_price)
                    save_alert(sym)

    except Exception as e:
        print("Error:", str(e))

    time.sleep(CHECK_INTERVAL)
