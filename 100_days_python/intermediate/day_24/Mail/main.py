TROCA = "[name]"

with open("./Input/Names/invited_names.txt") as nomes_arq:
    # cria uma lista de strings com os nomes
    nomes = nomes_arq.readlines()

with open("./Input/Letters/starting_letter.txt") as carta_arq:
    # read() pega toda a carta como uma string só
    conteudo_arq = carta_arq.read()

for nome in nomes:
    nomes_limpo = nome.strip()

    nova_carta = conteudo_arq.replace(TROCA, nomes_limpo)
    try:
        arq_path = f"./Output/ReadyToSend/letter_for_{nomes_limpo}.txt"
        with open(arq_path, "x") as cartas_completas:
            cartas_completas.write(nova_carta)
            print(f"Carta criada para o {nomes_limpo}")

    except FileExistsError:
        print(f"Arquivo já existe para {nomes_limpo}")

