import os

import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv("venv/.env")


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._user = os.getenv("ENV_SHEETY_USERNAME", "")
        self._password = os.getenv("ENV_SHEETY_PASSWORD", "")
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.sheet_endpoint = os.getenv("SHEET_ENDPOINT", "")
        self.dest_data = {}

    def get_data(self):
        response = requests.get(url=self.sheet_endpoint, auth=self._authorization)
        data = response.json()
        self.dest_data = data['flightPrices']
        return self.dest_data

    # -- Updating the price in the spreedsheet --
    def update_lowest(self, id, novo_preco):
        new_data = {
            "price": {
                "lowestPrice": novo_preco
            }
        }

        requests.put(
            url=f"{self.sheet_endpoint}/{id}",
            json=new_data,
            auth=self._authorization
        )
