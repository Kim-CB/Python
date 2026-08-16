# Day 33 - Intermediate+ API Endpoints & API Parameters - ISS Overhead Notifier

# Application Programming Interfaces - API"s
# Project is a ISS tracker
# International Space Station (ISS) is operated by five partner space agencies: NASA (United States), Roscosmos (Russia), ESA (Europe), JAXA (Japan) and CSA (Canada).
# The ISS is the political product of the development of international cooperation in space throughout the space age.

# request documentation: https://docs.python-requests.org/en/latest/
from datetime import datetime

import requests

MY_LAT = -22.906847
MY_LONG = -43.172897

# url = "http://api.open-notify.org/iss-now.json"

# response = requests.get(url=url)

# print(response)
# print(response.status_code)

# all status codes: https://www.webfx.com/web-development/glossary/

# if response.status_code == 404:
#     raise Exception("That resource does not exist.")
# elif response.status_code == 401:
#     raise Exception("You are not authorised to access this data.")

# data = response.json()
# data = response.json()["iss_position"]
# longitude = response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]

# iss_position = (longitude, latitude)
# print(iss_position)

# if want to see where this positions is: https://www.latlong.net/Show-Latitude-Longitude.html

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(" https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()  # noqa: DTZ005

print(time_now.hour)