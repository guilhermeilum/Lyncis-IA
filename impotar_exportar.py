import pandas as pd


def main(dados, municipio):
    dado_principal(dados)
    municipios(municipio)


def dado_principal(dados):
    # Primeiro iremos ler os dados do Csv, já lendo apenas as colunas já selecionadas e definindo seu tipo.
    df = pd.read_csv(
        dados,
        sep="\t",
        usecols=[
            "infection.county",
            "infection.state",
            "infection.hr",
            "notification.county",
            "notification.month",
            "notification.year",
            "detection.type",
            "occupation",
        ],
        dtype={
            "infection.hr": "category",
            "occupation": "category",
            "detection.type": "category",
            "infection.state": "category",
        },
    )
    # Após apagamos todas as linhas que contem algum dado em branco, fazendo isso diminuímos de praticamente 22 milhões para 2 milhões de dados.
    df = df.dropna(axis=0)
    df = df.reindex(list(range(len(df))))
    logic1=[]
    for i in range(len(df)):
        if df["infection.county"][i]==df["notification.county"][i]:
            logic1.append(True)
        else:
            logic1.append(False)
    df = df.loc[logic1]
    df = df.drop(["notification.county"],axis=1)
    # Exportamos esses dados para pickle para ficar mais fácil de fazer o upload.
    df.to_pickle("dados\Dados_utilizaveis")


def municipios(municipios_dados):
    # Para os dados dos municipios faremos os mesmos passos.
    municipio = pd.read_csv(municipios_dados, dtype={"sigla_uf": "category"})
    logic1 = municipio["ano"] >= 2009
    logic2 = municipio["ano"] <= 2019
    municipio = municipio.loc[logic1 & logic2]
    municipio = municipio.dropna(axis=0)
    municipio.to_pickle("dados\municipio")


main("dados\integrated_dataset.csv", "dados\municipio.csv")
