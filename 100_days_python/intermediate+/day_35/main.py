# Day 35 - Intermediate+ - Keys, Authentication & Environment Variables: Send SMS
import os

import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

API_KEY = os.environ.get("OWM_API_KEY")
city_id = 3451190
lat = -22.9028
lon = -43.2075

account_sid = ""
auth_token = os.environ.get("AUTH_TOKEN")
# export AUTH_TOKEN=................
# to pythonanywhere

to_number = ''
from_number = ''

# response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?id={city_id}&appid={API_KEY}")
# print(response)
# print(response.json())



weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": API_KEY,
    "cnt":4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# if weather_id < 700: bring unbrella (Challenge)

data = weather_data['list'][0]['dt_txt']
codigo = weather_data['list'][0]['weather'][0]['id']

id = [hour_id["weather"][0]["id"] for hour_id in weather_data["list"]]
data = [hour["dt_txt"] for hour in weather_data['list']]

tuple_dt_id = tuple([id_,data_] for data_ in data for id_ in id)

# print(tuple_dt_id)

# Course Unbrella Chall

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring and umbrella.",
            from_=from_number,
            to= to_number
        )
    wpp_message = client.messages \
        .create(
            from_="whatsapp:TWILIO_WHATSAPP_NUMBER",
            body="It's going to rain today. Remember to bring an umbrella.",
            to="whatsapp:YOUR_TWILIO_VERIFIED_NUMBER"
        )
    print(message.status)

# Can be put to run through schedule on pythonanywhere or any similar models
# has to change a little bit of the code to work
# import os
# if will_rain:
#     proxy_client = TwilioHttpClient()
#     proxy_client.session.proxies = {'https': os.environ['https_proxy']}

#     client = Client(account_sid, auth_token, http_client=proxy_client)
#     message = client.messages \
#             .create(
#                 body="It's going to rain today. Remember to bring and umbrella.",
#                 from_=from_number,
#                 to= to_number
#             )