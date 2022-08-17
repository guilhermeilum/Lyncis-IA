import pandas as pd
def main(dados):
    dado_principal(dados)
    municipios()

def dado_principal(dados):
    #Primeiro iremos ler os dados do Csv, já lendo apenas as colunas já selecionadas e definindo seu tipo.
    df = pd.read_csv(dados,sep = "\t",usecols=["infection.county","infection.state","infection.hr","notification.month","notification.year","detection.type","occupation"],dtype={"infection.hr":"category","occupation":"category","detection.type":"category","infection.state":"category"})
    #Após apagamos todas as linhas que contem algum dado em branco, fazendo isso diminuímos de praticamente 22 milhões para 2 milhões de dados.
    df = df.dropna(axis=0)
    #Exportamos esses dados para pickle para ficar mais fácil de fazer o upload.
    df.to_pickle("dados\Dados_utilizaveis")

def municipios():
    #Para os dados dos municipios faremos os mesmos passos.
    municipio = pd.read_csv("dados\municipio.csv", dtype={"sigla_uf":"category"})
    logic1 = municipio["ano"] >= 2009
    logic2 = municipio["ano"] <=2019
    municipio = municipio.loc[logic1 & logic2]
    municipio.to_pickle("dados\municipio")

main("dados\integrated_dataset.csv")