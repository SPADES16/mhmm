import requests
url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
response = requests.get(url)
value = response.json()['bpi']['USD']['rate']
print("The Current BitCoin Price Is: $" + value)
