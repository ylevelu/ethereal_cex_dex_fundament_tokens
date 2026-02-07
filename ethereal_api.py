import requests

BASE = "https://api.ethereal.trade"

def list_products():
    # возвращает список инструментов
    url = f"{BASE}/v1/product"
    r = requests.get(url)
    r.raise_for_status()
    return r.json().get("data", [])


def get_mark_price(ticker):
    # API Ethereal подразумевает endpoint типа:
    # /v1/market/{ticker}/price или отдельный price API
    url = f"{BASE}/v1/market/{ticker}/index"
    r = requests.get(url)
    r.raise_for_status()

    data = r.json()
    return float(data.get("price", 0))
