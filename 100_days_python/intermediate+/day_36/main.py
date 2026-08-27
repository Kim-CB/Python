from datetime import datetime, timedelta

import requests
from twilio.rest import Client

account_sid = ""
auth_token = ""
from_number = ""
to_number = ""

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

api_key_alphavintage = ""
api_key_newsapi = ""

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"



stock_parametros = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": api_key_alphavintage

}

ontem = datetime.now() - timedelta(days=1)  # noqa: DTZ005
ontem_str = ontem.strftime("%Y-%m-%d")

response_stock = requests.get(STOCK_ENDPOINT, params= stock_parametros)
response_stock.raise_for_status()
stock_data = response_stock.json()


data_list = [value for (key,value) in stock_data["Time Series (Daily)"].items()]
stock_data_daily_close_ontem = float(data_list[0]['4. close'])
stock_data_daily_close_anteontem = float(data_list[1]['4. close'])

diferenca_stock = stock_data_daily_close_ontem - stock_data_daily_close_anteontem

up_down = "🔺" if diferenca_stock > 0 else "🔻"

diferenca_percentual = round((abs(diferenca_stock)/ stock_data_daily_close_anteontem) * 100)

if diferenca_percentual > 5:

    noticias_parametros = {
        "apikey": api_key_newsapi,
        "language": "en",
        "q": COMPANY_NAME,
        "page": 2
    }

    response_news = requests.get(NEWS_ENDPOINT, params=noticias_parametros)
    response_news.raise_for_status()
    response_news_data = response_news.json()

    tres_artigos = response_news_data["articles"][:3]

    artigos_formatados = [
        {
            "fonte": article["source"]["name"],
            "titulo": article["title"],
            "descricao": article["description"],
            "url": article["url"]
        }
        for article in tres_artigos
    ]

    client = Client(account_sid, auth_token)

    for article in artigos_formatados:
        mensagem_formatada = f"{STOCK_NAME}: {up_down}{diferenca_percentual}%\nHeadline: {article['titulo']}\nBrief: {article['descricao']}"

        message = client.messages.create(
            body=mensagem_formatada,
            from_=from_number,
            to=to_number
        )




