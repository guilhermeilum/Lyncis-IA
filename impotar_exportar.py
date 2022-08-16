import pandas as pd
def main(dados):
    #Primeiro iremos ler os dados do Csv, já lendo apenas as colunas já selecionadas e definindo seu tipo.
    df = pd.read_csv(dados,sep = "\t",usecols=["infection.county","infection.state","infection.hr","notification.month","notification.year","detection.type","occupation"],dtype={"infection.hr":"category","occupation":"category","detection.type":"category","infection.state":"category"})
    #Após apagamos todas as linhas que contem algum dado em branco, fazendo isso diminuímos de praticamente 22 milhões para 2 milhões de dados.
    df = df.dropna(axis=0)
    #Exportamos esses dados para pickle para ficar mais fácil de fazer o upload.
    df.to_pickle("dados\Dados_utilizaveis")

main("dados\integrated_dataset.csv")