import os

import requests
from dotenv import load_dotenv

load_dotenv()

SERPAPI_ENDPOINT = "https://serpapi.com/search"

class FlightSearch:

    def __init__(self):
        self._api_key = os.environ["SEARP_API_KEY"]

    def procurando_voos(self, cidade_origem, cidade_destino, from_time, to_time):
        query = {
            "engine": "google_flights",
            "departure_id": cidade_origem,
            "arrival_id": cidade_destino,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "type": "1",
            "adults": "1",
            "currency": "BRL",
            "api_key": self._api_key,
        }

        response = requests.get(url=SERPAPI_ENDPOINT, params=query)

        if response.status_code != 200:
            print(f"procura de voos response code: {response.status_code}")
            return None

        data = response.json()
        if "error" in data:
            print(f"API error: {data['error']}")
            return None
        return data