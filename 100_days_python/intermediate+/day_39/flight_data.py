class FlightData:

    def __init__(self, preco, cidade_origem, aeroporto_destino, voo_saida, voo_volta):
        self.preco = preco
        self.cidade_origem = cidade_origem
        self.aeroporto_destino = aeroporto_destino
        self.voo_saida = voo_saida
        self.voo_volta = voo_volta

def voo_mais_barato(dados, voo_volta):

    if dados is None or (not dados.get("best_flights") and not dados.get("other_flights")):
        print("Sem dados do voo.")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    todos_voos  = dados.get("best_flights", []) + dados.get("other_flights", [])

    primeiro_voo = todos_voos[0]
    menor_preco = primeiro_voo['price']
    origem = primeiro_voo['flights'][0]['departure_airport']['id']
    destino = primeiro_voo['flights'][-1]['arrival_airport']['id']
    voo_saida  = primeiro_voo['flights'][0]['departure_airport']['time'].split(" ")[0]

    voo_mais_barato = FlightData(menor_preco, origem, destino, voo_saida, voo_volta)

    for voo in todos_voos:

        try:
            preco = voo["preco"]
        except KeyError:
            print("--- Sem preço para o voo --")
            continue
        if preco < menor_preco:
            menor_preco = preco
            origem = voo["flights"][0]["departure_airport"]["id"]
            destino = voo["flights"][-1]["arrival_airport"]["id"]
            voo_saida = voo["flights"][0]["departure_airport"]["time"].split(" ")[0]
            voo_mais_barato = FlightData(menor_preco, origem, destino, voo_saida, voo_volta)
            print(f"Menor preço para {destino} é R${menor_preco}")
            
    return voo_mais_barato