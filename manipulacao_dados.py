import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def importar():
    """importa os dados nescessarios e devolve dois dados, tabela da malaria e dados dos municipios
    arg: nenhum
    retunr: df =  tabela pandas base de dados e municipios = tabela pandas dos municipios e população por ano."""
    df = pd.read_pickle("dados\Dados_utilizaveis")
    # criar coluna com dados de casos confirmados como 1, outros resultados como 0
    df["detection.numerico"] = df["detection.type"].map(
        {"active": 1, "passive": 0, "CVL": 0}
    )
    municipio = pd.read_pickle("dados\municipio")
    municipio["id_municipio"] = municipio["id_municipio"] // 10
    return df, municipio


def municipios_unicos(df, year):
    """Descobre municipios relatados em cada ano, não os repetindo
    arg: base de dados e ano em questão
    return: matriz dos munipios em cada mes do ano"""
    logic = df["notification.year"] == year
    municipio_unico_cada_mes = (
        df.loc[logic].groupby("notification.month")["infection.county"].unique()
    )
    return municipio_unico_cada_mes


def descobrir_população_por_mes(
    municipio, municipio_unico_cada_mes, ano, tabela_população
):
    """Descobre a polulação total de cada mês
    Arg: tabela de dados de municipio, tabela de dados de municipio unico, ano de referencia,tabela depopulação para add dados novos
    Return: tabela, com primeira colula dos meses e segunda da população total, com referencia o ano"""
    # todas as colunas do respectivo ano
    logic1 = municipio["ano"] == ano
    mes = 0
    lista_população = []
    # for em cada linha
    for linha in municipio_unico_cada_mes:
        mes += 1
        população_total = 0
        # for id em cada lista de municipios
        for id in linha:
            logic2 = municipio["id_municipio"] == id
            população_total += int(municipio.loc[logic1 & logic2]["populacao"])
        lista_população.append(população_total)
    tabela_população[f"{ano}"] = lista_população

    return tabela_população


def descobrir_casos_por_mes(df, ano, tabela_casos):
    """Descobre a soma dos casos por mes de determinado ano usando groupby pela sua rapidez
    Arg: dados, ano em questão, tabela de casos para add dados
    Return: tabela de casos"""
    logic = df["notification.year"] == ano
    casos_cada_mes = list(
        df.loc[logic].groupby("notification.month")["detection.numerico"].sum()
    )
    tabela_casos[f"{ano}"] = casos_cada_mes
    return tabela_casos


def plot_graficos(tabela_plot):
    fig = plt.figure()  # Definindo a figura do plot

    ax1 = fig.add_subplot(251)
    tabela_plot.plot(x="mes", y="2010", legend=True, ax=ax1)
    ax1.set_ylabel("Porcentagem de casos", fontsize=12)
    ax1.set_xlabel("")
    ax1.set_xticklabels([])

    ax2 = fig.add_subplot(252)
    tabela_plot.plot(x="mes", y="2011", legend=True, ax=ax2)
    ax2.set_yticklabels([])
    ax2.set_xticklabels([])
    ax2.set_xlabel("")

    ax3 = fig.add_subplot(253)
    tabela_plot.plot(x="mes", y="2012", legend=True, ax=ax3)
    ax3.set_yticklabels([])
    ax3.set_xticklabels([])
    ax3.set_xlabel("")

    ax4 = fig.add_subplot(254)
    tabela_plot.plot(x="mes", y="2013", legend=True, ax=ax4)
    ax4.set_yticklabels([])
    ax4.set_xticklabels([])
    ax4.set_xlabel("")

    ax5 = fig.add_subplot(255)
    tabela_plot.plot(x="mes", y="2014", legend=True, ax=ax5)
    ax5.set_yticklabels([])
    ax5.set_xticklabels([])
    ax5.set_xlabel("")

    ax6 = fig.add_subplot(256)
    tabela_plot.plot(x="mes", y="2015", legend=True, ax=ax6)
    ax6.set_ylabel("Porcentagem de casos", fontsize=12)

    ax7 = fig.add_subplot(257)
    tabela_plot.plot(x="mes", y="2016", legend=True, ax=ax7)
    ax7.set_yticklabels([])

    ax8 = fig.add_subplot(258)
    tabela_plot.plot(x="mes", y="2017", legend=True, ax=ax8)
    ax8.set_yticklabels([])

    ax9 = fig.add_subplot(259)
    tabela_plot.plot(x="mes", y="2018", legend=True, ax=ax9)
    ax9.set_yticklabels([])

    ax10 = fig.add_subplot(2, 5, 10)
    tabela_plot.plot(x="mes", y="2019", legend=True, ax=ax10)
    ax10.set_yticklabels([])

    plt.subplots_adjust(wspace=0.25, hspace=0.12)  # Ajustar distância entre os gráficos
    plt.subplots_adjust(wspace=0.25, hspace=0.12)  # Ajustar distância entre os gráficos

    for ax in [
        ax1,
        ax2,
        ax3,
        ax4,
        ax5,
        ax6,
        ax7,
        ax8,
        ax9,
        ax10,
    ]:  # Ajustar o range dos eixos-y de todos os gráficos, para uniformizar
        plt.setp(ax, ylim=(0, 0.2))

    plt.savefig(
        "grafico.png", dpi=300, format="png", facecolor="white"
    )  # Salvar figura com o gráfico, fundo branco
    plt.show()  # Mostrar o gráfico


def matriz_covariancia(df):
    df["mes"] = minmax_norm(df, "mes")
    for i in range(2010, 2020):
        df[str(i)] = minmax_norm(df, str(i))
    print("\nMatriz normalizada\n")
    print(df)
    print("\nMatriz de covariancia.\n")
    matriz = df.cov()
    print(matriz)
    sns.heatmap(matriz, xticklabels=matriz.columns, yticklabels=matriz.columns)
    plt.title("Covariância")
    plt.show()


def minmax_norm(df, coluna):
    return (df[coluna] - df[coluna].min()) / (df[coluna].max() - df[coluna].min())


def descricao(df):
    print("Descrição da tablela de chance minima de contaminação.\n")
    tabela_descricao = df.describe()
    print(tabela_descricao)


def main():
    """Função padrão para organizar o codigo"""
    df, municipio = importar()
    # tabelas previamente criada para organizar dados
    tabela_população = pd.DataFrame(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], columns=["mes"]
    )
    tabela_casos = pd.DataFrame(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], columns=["mes"]
    )
    # Um ano a menos do que poderia pois não temos dados da população de todas os munucipios
    for ano in range(2010, 2020):
        municipio_unico_cada_mes = municipios_unicos(df, ano)
        tabela_população = descobrir_população_por_mes(
            municipio, municipio_unico_cada_mes, ano, tabela_população
        )
        tabela_casos = descobrir_casos_por_mes(df, ano, tabela_casos)
    tabela_chance = (
        tabela_casos / tabela_população * 100
    )  # tabela de percentagem da chance
    tabela_chance["mes"] = list(range(1, 13))  # Arrumando a coluna mês
    print("tabela de chance minima de contaminação.\n", tabela_chance)
    descricao(tabela_chance)
    plot_graficos(tabela_chance)
    matriz_covariancia(tabela_chance)


main()
