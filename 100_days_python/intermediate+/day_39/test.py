from datetime import datetime, timedelta

import requests
from dateutil.relativedelta import relativedelta

SERPAPI_ENDPOINT = "https://serpapi.com/search"
SEARP_API_KEY = "ca96db8b174a4c0a93daa97c32d5f11016e78232cac75e0c8613dc43d2452266"

response = requests.get(url="https://api.sheety.co/85cbe337263d8c0d4af57660c582d669/flightDeals/flightPrices", auth=("kim","bnVsbDpudWxs"))
data = response.json()
dest_data = data['flightPrices']
print(dest_data)

# amanha = datetime.now() + timedelta(days=1)  # noqa: DTZ005
# seis_meses = datetime.now() + relativedelta(months=6)  # noqa: DTZ005


# query = {
#     "engine": "google_flights",
#     "departure_id": "GIG",
#     "arrival_id": "VVI",
#     "outbound_date": amanha.strftime("%Y-%m-%d"),
#     "return_date": seis_meses.strftime("%Y-%m-%d"),
#     "type": "1",
#     "adults": "1",
#     "currency": "BRL",
#     "api_key": SEARP_API_KEY,
# }

# response = requests.get(url=SERPAPI_ENDPOINT, params=query)

# data = response.json()
# print(data)