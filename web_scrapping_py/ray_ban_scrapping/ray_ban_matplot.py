import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def main():
    # config visual
    sns.set_theme(style='whitegrid')
    plt.rcParams['font.family'] = 'sans-serif'

    # Dados
    try:
        df = pd.read_csv('rayban_todos_oculos.csv')
    except FileNotFoundError:
        print("Arquivo não encontrado. Rodar o scraper primeiro.")
        return

    # Limpando dados
    df['Preço_Num'] = df['Preço'].str.replace('R$', '', regex=False)\
                                .str.replace('.', '', regex=False)\
                                .str.replace(',', '.', regex=False)\
                                .str.strip().astype(float)
    # Criando layout
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(2, 2)

    # Gráfico 1 (Bar plot)
    ax1 = fig.add_subplot(gs[0, 0])
    ordem_categorias = df['Categoria'].value_counts().index
    sns.countplot(data=df, x='Categoria', palette='Blues_d', ax=ax1, order=ordem_categorias)

    ax1.set_title('Quantidade de Modelos Extraídos por Categoria', fontsize=14, fontweight='bold', pad=15)
    ax1.set_xlabel('')
    ax1.set_ylabel('Quantidade')

    # Rótulos numéricos
    for p in ax1.patches:
        ax1.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                     ha='center', va='baseline', fontsize=12, fontweight='bold',xytext=(0,5),
                     textcoords='offset points')

    # Gráfico 2 (Bloxplot)
    ax2 = fig.add_subplot(gs[0, 1])
    sns.boxplot(data=df, x='Categoria', y='Preço_Num', palette='Blues_d', ax=ax2, order=ordem_categorias)
    ax2.set_title('Distribuição e Dispersão de Preços (R$)', fontsize=14, fontweight='bold', pad=15)
    ax2.set_xlabel('')
    ax2.set_ylabel('Preço (R$)')

    # Gráfico 3 (Histograma)
    ax3 = fig.add_subplot(gs[1, :])
    sns.histplot(data=df, x= 'Preço_Num', hue='Categoria', multiple="stack", bins=30, 
                 palette='Blues_d', edgecolor =".3", linewidth=.5, ax=ax3)
    ax3.set_title('Histograma: Concentração de Preços no Portfólio', fontsize=14, fontweight='bold', pad=15)
    ax3.set_xlabel('Preço (R$)')
    ax3.set_ylabel('Frequência')

    # Ajustes Finais
    plt.tight_layout()
    nome_arquivo = 'dashboard_rayban.png'
    plt.savefig(nome_arquivo, dpi=300,bbox_inches= 'tight')
    print(f"Dashboard gerado com sucesso. Arquivo {nome_arquivo}")




if __name__ == "__main__":
    main()