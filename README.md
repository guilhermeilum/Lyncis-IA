<h1 align="center"> Lyncis-IA </h1>

## Projeto criado para análise de dados da malária na Amazônia Legal através de Machine Learning

Os dados utilizados para esse projeto foram extraídos de do domínio <https://doi.org/10.7303/syn21552203>, de um estudo realizado na Amazônia Legal sobre malária. A partir disso, pensamos em desenvolver um mecanismo probabilistíco por Machine Learning sobre possível taxa de infecção quando se está/visita algum munícipio dos considerados.

### Descrição dos arquivos

<ul>
  <li>Pasta “dados”: contém todos os dados necessários para utilizar no arquivo “manipulacao_dados.py”, já o arquivo “importar_expotar.py” é utilizado unicamente para tratar previamente os dados com tamanho reduzido e exportando o arquivo para o modelo pickle, ao invés do csv, para melhor rapidez. Dentro existem os "Dados_utilizaveis", que são os dados que estamos utilizando no nosso <em>Machine Learning</em>, uma lista com o código dos munícipios do Brasil e os dados de latitude e longitude respectivos.</li>
  <li>O arquivo “manipulacao_dados.py” termina de tratar os dados, extraídos pelo comando do arquivo "impotar_exportar.py", e <em>plota</em>, por enquanto, o mínimo da chance de alguém contrair malária em cada mês e variando os anos, comparado com a somatória da população dos municípios que teve a infecção.</li>
  <li>O "grafico.png" foi feito para uma análise preliminar de todos os dados.</li>
  <li>O "manuscrito.md" é uma espécie de diário de bordo sobre as atividades do grupo, atualizado por cada líder durante seu "mandato". Vale a ressalva que o manuscrito foi posta em prática a partir do Bloco 2.
  <li>O "requerimentos.txt" é um arquivo onde estão contidas as bibliotecas instalas e utilizadas no nosso <em>Machine Learning</em>, tais como: Numpy, Pandas, SciKit-Learn.
  <li>E, finalmente, no arquivo "treino.ipynb" é onde a mágica acontece! Estão contidas todas as informações a respeito do nosso projeto que podem ser visualizadas rodando o programa.
  <li>O arquivo "unsupervised.ipynb" é onde foi trabalhado os dados criando PCA, modelos não supervisionados e também foi localizado dados anômalos.
    
</ul>

<h4 align="center">
    :construction:  Projeto em construção  :construction:
</h4>
