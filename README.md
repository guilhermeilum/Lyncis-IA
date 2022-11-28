<h1 align="center"> Lyncis-IA </h1>

## Projeto elaborado para o estudo analítico (desenvolvido com _Machine Learning_) de dados anamnéticos sobre casos de malária relacionados à Amazônia Legal.

Os dados utilizados para o desenvolvimento desse projeto foram extraídos de um repositório da Synapse, [_An Integrated Dataset of Malaria Notifications in the Legal Amazon_](https://doi.org/10.7303/syn21552203). À vista disso, foi desenvolvido um mecanismo probabilístico, o qual visa mensurar a taxa de infecção por _Plasmodium sp._ quando se visita ou mora em algum dos munícipios documentados.

#### por Guilherme Gurian Dariani, Shaian José Anghinoni e Gustavo Duarte Verçosa.

### Descrição dos arquivos

<ul>
  <li>Pasta “dados”: contém todos os dados necessários para o estudo.</li>
<ul>
  <li>Arquivo ".gitignore": utilizado para designar arquivos e diretórios ignorados;</li>
  <li>Arquivo "LICENSE": usado para compartilhar <em>software</em> de código aberto;</li>
  <li>Arquivo "README.md": apresenta informações do projeto, é o que está lendo agora;</li>
  <li>Arquivo "grafico.png": feito para uma análise preliminar de todos os dados;</li>
  <li>Arquivo "importar_exportar.py": trata previamente os dados com tamanho reduzido e exporta o arquivo para o modelo <em>pickle</em>, ao invés do <em>csv</em> (a fim de ser mais rápido). Possui "Dados_utilizaveis", que contêm o código dos munícipios do Brasil e os dados de latitude e longitude respectivos, sendo então as informações utilizadas para elaborar o estudo de <em>Machine Learning</em>;</li>
  <li>Arquivo "manipulacao_dados.py":  termina de tratar os dados e <em>plota</em> a chance mínima de alguém contrair malária em cada mês (variando os anos), comparado com a somatória da população dos municípios que teve a infecção;</li>
  <li>Arquivo "matriz_covariancia.png": análise da interligação entre meses;</li>
  <li>Arquivo "requerimentos.txt": são todas as bibliotecas instaladas e, portanto, utilizadas, tais como: Numpy, Pandas, SciKit-Learn;</li>
  <li>Arquivo "treino.ipynb": desenvolvimento prático da análise probabilística; </li>
  <li>Arquivo "unsupervised.ipynb": estudo de modelos não supervisionados, algoritmos PCA e dados anômalos.</li>
    
</ul>
