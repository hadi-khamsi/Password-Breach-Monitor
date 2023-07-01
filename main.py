import requests
from bs4 import BeautifulSoup
# import pandas
# import matplotlib as pd
def fetch_stock_data(symbol):
    url = f"https://finance.yahoo.com/quote/{symbol}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Finds the current price
    price_element = soup.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
    if price_element is None:
        current_price = "N/A"
    else:
        current_price = float(price_element.text)

    # Finds the previous close
    prev_close_element = soup.find("td", class_="Ta(end) Fw(600) Lh(14px)", attrs={"data-test": "PREV_CLOSE-value"})
    if prev_close_element is None:
        prev_close = "N/A"
    else:
        prev_close = float(prev_close_element.text)

    # Determine if it's a buy call or buy put
    if isinstance(current_price, float) and isinstance(prev_close, float):
        if current_price < prev_close:
            recommendation = "Buy Calls"
        else:
            recommendation = "Buy Puts"
    else:
        recommendation = "N/A"

    return current_price, prev_close, recommendation

if __name__ == "__main__":
    symbol = input("Ticker Symbol: ")
    current_price, prev_close, recommendation = fetch_stock_data(symbol)
    print(f"Current Price: {current_price}")
    print(f"Previous Close: {prev_close}")
    print(f"Recommendation: {recommendation}")