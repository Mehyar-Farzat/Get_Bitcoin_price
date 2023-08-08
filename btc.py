
# get BTC price from Binance Platform as windows notifaction

import requests
from win10toast import ToastNotifier
import time

toaster = ToastNotifier()

while True:
    url = 'https://api.binance.com/api/v3/ticker/price'
    parameters = {
      'symbol': 'BTCUSDT'
    }

    response = requests.get(url, params=parameters)
    data = response.json()
    price = float(data['price'])

    toaster.show_toast("Bitcoin Price", f"${price:,.2f}", duration=10)

    time.sleep(300) # wait 5 minutes

'''
# get multi Cryptocurrency price from Binance Platform as windows notificatin
import requests
from win10toast import ToastNotifier
import time
from binance.client import Client

toaster = ToastNotifier()
client = Client ('3Pc9cskMw0L54wrHdUSj5v1pXB5VY5sZwEcUOVV9SoDbx811lyO2nOYYGD11NdaQ' , 'I9zyRmVAHm47peOmlKdkjXvFw5KZbAgLMhCQwGyKzQ3f8mtsrHgmxKFXAEKMp9UZ ')

binance_symbols = ['BTCUSDT',  'VETUSDT']
while True:
    prices = client.get_all_tickers()
    for symbol in binance_symbols:
        price = float([p['price'] for p in prices if p['symbol'] == symbol][0])
        toaster.show_toast(f"{symbol} Price", f"${price:,.2f}", duration=10)
    time.sleep(300) # wait 5 minutes
'''




