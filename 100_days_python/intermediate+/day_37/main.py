from datetime import datetime

import requests

USERNAME = "kim-cb"
TOKEN = "j32i4h234h5t43b5234j5"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Horas",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime.now()  # noqa: DTZ001, DTZ005, RUF100
today_str = today.strftime("%Y%m%d")

post_pixel = {
    "date": today_str,
    "quantity": float(input("Quantas horas de código hoje?"))
}

response = requests.post(url=post_endpoint, json=post_pixel, headers=headers)
print(response.text)

put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_str}"

put_pixel = {
    "quantity": "4.5"
}

response = requests.put(url=put_endpoint, json=put_pixel, headers=headers)
print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_str}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response)