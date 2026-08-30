import os
from datetime import datetime

import requests

APP_ID = os.environ["ENV_NIX_APP_ID"]
API_KEY = os.environ["ENV_NIX_API_KEY"]

exercise_url = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

question = input("Tell me which exercises you did: ")

# Supported activities:
# Running/Jogging - "ran for 30 minutes", "jogged 2 miles"
# Swimming - "swam for 1 hour", "swimming laps"
# Walking - "walked 3 miles", "brisk walk 45 min"
# Cycling - "biked for 1 hour", "rode bike 10 miles"
# Weightlifting - "lifted weights 45 min", "weight training"

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

data = {
    "query": question,
    "weight_kg": 75,
    "height_cm": 171,
    "age":25,
    "gender": "male"
}

response = requests.post(url=exercise_url, headers=headers, json=data)
response_data = response.json()
print(response_data["exercises"][0])

hoje = datetime.now().strftime("%d/%m/%Y")  # noqa: DTZ005
hora = datetime.now().strftime("%X")  # noqa: DTZ005

sheet_endpoint = os.environ["ENV_SHEETY_ENDPOINT"]
GOOGLE_SHEET_NAME = "workout"

for exercise in response_data["exercises"]:
    inputs = {
        GOOGLE_SHEET_NAME: {
            "date":hoje,
            "time": hora,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }



    sheet_response = requests.post(
        sheet_endpoint,
        json=inputs,
        auth=(
            os.environ["ENV_SHEETY_USERNAME"],
            os.environ["ENV_SHEETY_PASSWORD"]
        )
    )


    print(f"Sheety Response: \n{sheet_response.text}")