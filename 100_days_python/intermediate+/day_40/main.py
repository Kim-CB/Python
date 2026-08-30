from datetime import datetime, timedelta
from pprint import pprint

import requests_cache
from data_manager import DataManager
from flight_data import find_cheapest_flight
from flight_search import FlightSearch
from notification_manager import NotificationManager

# ==================== Conserve requests and preserve your free plan ====================
requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)
# ==================== Setup ====================
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# pprint(sheet_data)
flight_search = FlightSearch()
# Create an instance of the NotificationManager
notification_manager = NotificationManager()

# ---------------------

customer_data = data_manager.get_customer_emails()

customer_email_list = [row['whatIsYourEmail?'] for row in customer_data]

# ==================== Set the Dates and Origin Airport ====================
tomorrow = datetime.now() + timedelta(days=1)  # noqa: DTZ005
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))  # noqa: DTZ005
ORIGIN_CITY_IATA = "GIG"  # Galeão - Rio de Janeiro

# ==================== Achando voos baratos ====================

for destination in sheet_data:
    pprint(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights, return_date=six_month_from_today.strftime("%Y-%m-%d"))
    pprint(f"{destination['city']}: BRL {cheapest_flight.price}")

    # ---------------- Voos indiretos se N/A ----------------------

    if cheapest_flight.price != "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct=False
        )
        cheapest_flight = find_cheapest_flight(stopover_flights, return_date=six_month_from_today.strftime("%Y-%m-%d"))
        print(f"Cheapest indirect flight price is: BRL {cheapest_flight.price}")

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        data_manager.update_lowest_price(destination["id"], cheapest_flight.price)
        # Mensagens variadas dependendo do numero de paradas
        if cheapest_flight.stops == 0:
            message = f"Preço baixo alerta! Valor: {cheapest_flight.price} para voar para"\
                      f"para {cheapest_flight.origin_airport} para {cheapest_flight.destination_airport}, "\
                      f"no dia {cheapest_flight.out_date} até {cheapest_flight.return_date}."
        else:
            message = f"Alerta de preço baixo! Só {cheapest_flight.price} para voar"\
                      f"de {cheapest_flight.origin_airport} para {cheapest_flight.destination_airport}, "\
                      f"com {cheapest_flight.stops} parada(s)"\
                      f"saindo no dia {cheapest_flight.out_date} e voltando no {cheapest_flight.return_date}"

        print(f"Olhe seu email. Voo mais barato achado para {destination["city"]}!")

        # Mandando email com as respostas
        notification_manager.send_emails(email_list=customer_email_list, email_body=message)

        notification_manager.send_sms(message_body="sms_event_notifications")
