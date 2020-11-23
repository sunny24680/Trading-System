import requests

r = requests.get('https://finnhub.io/api/v1/stock/candle?symbol=AAPL&resolution=1&from=1605543327&to=1605629727&token=busn7c748v6vuigkh920')
print(r.json())