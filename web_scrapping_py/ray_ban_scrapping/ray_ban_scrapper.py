import time

import pandas as pd
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    TimeoutException,
)

# Selenium Importações
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def extrair_dados_rayban():
    paginas = [
        {
            "url": "https://www.ray-ban.com/brazil/oculos-de-grau/ver-todos",
            "categoria": "Óculos de Grau"
        },
        {
            "url": "https://www.ray-ban.com/brazil/oculos-de-sol/ver-todos",
            "categoria": "Óculos de Sol"
        }
    ]

    print("Iniciando Chromedriver...")
    options = uc.ChromeOptions()
    options.add_argument("--windows-size=1920,1080")
    driver = uc.Chrome(options=options)

    # Lista geral dos produtos que serão armazenados
    produtos_extraidos = []

    # Loop para Scroll e escolhendo página e categoria
    for pagina in paginas:
        url_atual = pagina["url"]
        categoria_atual = pagina["categoria"]

        print(f"\n Acessando categoria: {categoria_atual}")
        driver.get(url_atual)

        print("Carregando página...")
        time.sleep(5)

        print("Buscando por mais produtos...")

        while True:
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)

                wait = WebDriverWait(driver, 10)
                botao_carregar_mais = wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="load-more-button"]'))
                )

                driver.execute_script("arguments[0].click();", botao_carregar_mais)
                print("Botão 'CARREGAR MAIS PRODUTOS'. Aguardando itens...")
                time.sleep(3)
    
            except TimeoutException:
                print(f"Fim da página de {categoria_atual}. Itens carregados.")
                break
            except ElementClickInterceptedException as e:
                print(f"Ocorreu um erro inesperado na paginação ({categoria_atual}): {e}")
                break

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        print(f"Pegando dados do HTML para {categoria_atual}...")
        lista_produtos = soup.find_all('a', class_='rb-product-tile__wrapper')

        for produto in lista_produtos:
            try:
                # Nome
                nome_tag = produto.find('h2', class_= 'rb-product-tile__name')
                nome = nome_tag.text.strip() if nome_tag else "Sem nome"
                # Preço    
                preco_desconto_tag = produto.find('span', class_='rb-product-tile__price--discounted')
                if preco_desconto_tag:
                    preco = preco_desconto_tag.text.strip()
                else:
                    preco_original_tag = produto.find('span', class_= 'rb-product-tile__price--original')
                    preco = preco_original_tag.text.strip() if preco_original_tag else "Sem preço"

                href = produto.get('href')
                if href:
                    link = href if href.startswith('http') else "https://www.ray-ban.com" + href
                    link = link.replace(" ", "%20")
                else:
                    link = "Sem link"

                produtos_extraidos.append({
                    'Categoria': categoria_atual,
                    'Nome do Modelo': nome,
                    'Preço': preco,
                    'Link': link
                })

            except ElementClickInterceptedException as e:
                print(f"Erro ao processar um dos itens: {e}")
                continue

    # Fechando o navegador
    try:
        driver.__class__.__del__ = lambda x: None
        driver.quit()
    except OSError:
        pass

    # Exportando 
    print(f"\nForam encontrados {len(produtos_extraidos)} produtos no total (Sol e Grau).")

    if produtos_extraidos:
        df = pd.DataFrame(produtos_extraidos)
        # Reorganizando
        df = df[['Categoria', 'Nome do Modelo', 'Preço', 'Link']]
        # Salvando em CSV
        df.to_csv('rayban_todos_oculos.csv', index=False, encoding='utf-8')
        print("Dados exportados com sucesso para CSV 'rayban_todos_oculos.csv'!")
    else:
        print("Nenhum dado encontrado. Verifique as classes HTML no BeatifulSoup.")

if __name__ == "__main__":
    extrair_dados_rayban()