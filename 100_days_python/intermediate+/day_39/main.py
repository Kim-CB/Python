from datetime import datetime, timedelta
from pprint import pprint

import requests_cache
from data_manager import DataManager
from dateutil.relativedelta import relativedelta
from flight_data import voo_mais_barato
from flight_search import FlightSearch
from notification_manager import NotificationManager

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

requests_cache.install_cache(
    "flight_cache",
    urls_expire_after = {
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)
# ------------------------------------------

data_manager = DataManager()
sheet_data = data_manager.get_data()

flight_search = FlightSearch()
notification_manager = NotificationManager()

# --------------------------------------------
amanha = datetime.now() + timedelta(days=1)  # noqa: DTZ005
seis_meses = datetime.now() + relativedelta(months=6)  # noqa: DTZ005
CIDADE_ORIGEM = "GIG"

# ---------------------------------------------

for destino in sheet_data:
    pprint(f"Avaliando voos para {destino['city']}...")
    voos = flight_search.procurando_voos(
        CIDADE_ORIGEM,
        destino['iataCode'],
        from_time=amanha,
        to_time=seis_meses
    )
    voo_barato = voo_mais_barato(voos , voo_volta=seis_meses.strftime("%Y-%m-%d"))
    pprint(f"{destino['city']}: Preço = {voo_barato.preco}")

    if voo_barato.preco != "N/A" and voo_barato.preco < destino["lowestPrice"]:
        pprint(f"Voo mais barato para {destino['city']}")
        data_manager.update_lowest(destino["id"], voo_barato.preco)

        print(f"ALERTA DE PREÇO BARATO! "
            f"de {voo_barato.cidade_origem} to {voo_barato.aeroporto_destino},"
            f"de {voo_barato.voo_saida} até {voo_barato.voo_volta}")

        # notification_manager.send_wpp(
        #     message_body= f"ALERTA DE PREÇO BARATO!"
        #                 f"de {voo_barato.cidade_origem} to {voo_barato.aeroporto_destino},"
        #                 f"de {voo_barato.voo_saida} até {voo_barato.voo_volta}"
        # )

        notification_manager.send_wpp(message_body="sms_event_notifications")