from config import DEX_CEX_THRESHOLD

def is_anomaly(dex_price, cex_price):
    if cex_price == 0:
        return False

    diff = abs(dex_price - cex_price) / cex_price
    return diff >= DEX_CEX_THRESHOLD
