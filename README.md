# text_mining
Mineracao das emocoes:

Projeto de Análise de Sentimentos com Flask e Naive Bayes
Este projeto implementa um classificador de análise de sentimentos usando Flask (um framework web em Python) e o algoritmo Naive Bayes. Permite aos usuários inserir um texto e prever a emoção associada a esse texto. Este guia fornece instruções detalhadas para configurar o ambiente de desenvolvimento e executar o projeto.

Pré-requisitos
Antes de começar, você precisará instalar o Python e algumas bibliotecas essenciais manualmente. Siga as etapas abaixo:

1. Instalação do Python
Se você não tiver o Python instalado, siga estas etapas:

Baixe o Python em python.org.
Execute o instalador e certifique-se de marcar a opção "Adicionar Python ao PATH" durante a instalação.
2. Configuração do Ambiente Virtual (Opcional, mas recomendado)
A configuração de um ambiente virtual Python ajuda a isolar as dependências do projeto. Abra o terminal ou prompt de comando e siga estas etapas:

Instale a ferramenta virtualenv (caso ainda não tenha) usando o seguinte comando:

bash
Copy code
pip install virtualenv
Crie um ambiente virtual na pasta do projeto:

bash
Copy code
python -m venv venv
Ative o ambiente virtual:

No Windows:

bash
Copy code
venv\Scripts\activate
No macOS e Linux:

bash
Copy code
source venv/bin/activate
Instalação das Bibliotecas Necessárias
Certifique-se de estar dentro do ambiente virtual, se você optou por usá-lo, e, em seguida, instale as bibliotecas necessárias manualmente. Siga as etapas abaixo:

1. Instalação do Flask
O Flask é um framework web para Python que será usado para criar o servidor web do projeto.

Instalação:
Abra um terminal ou prompt de comando.

Execute o seguinte comando para instalar o Flask:

bash
Copy code
pip install Flask
2. Instalação do pandas
A biblioteca pandas é usada para manipulação de dados, o que é útil para carregar e processar os dados de treinamento e teste a partir dos arquivos CSV.

Instalação:
No mesmo terminal, execute o seguinte comando para instalar o pandas:

bash
Copy code
pip install pandas
3. Instalação do scikit-learn
A biblioteca scikit-learn é usada para implementar o modelo de aprendizado de máquina Naive Bayes.

Instalação:
Execute o seguinte comando para instalar o scikit-learn:

bash
Copy code
pip install scikit-learn
Após a execução dessas etapas, todas as bibliotecas necessárias estarão instaladas em seu ambiente e você poderá prosseguir com a execução do projeto de análise de sentimentos com Flask e Naive Bayes. Certifique-se de que o ambiente virtual Python, se você estiver usando um, esteja ativado durante a instalação das bibliotecas.

Execução do Projeto
Agora que você configurou o ambiente e instalou as bibliotecas, você pode executar o projeto. Siga estas etapas:

No terminal, navegue até o diretório do projeto.

Execute o seguinte comando para iniciar o aplicativo Flask:

bash
Copy code
python app.py
O aplicativo Flask estará em execução. Abra um navegador da web e acesse http://localhost:5000 para usar o projeto de análise de sentimentos.
Estrutura do Projeto
A estrutura do projeto é a seguinte:


Copy code
projeto_sentimentos/
├── app.py
├── basetreinamento1.csv
├── baseteste1.csv
├── templates/
│   ├── index.html
│   └── resultado.html
├── venv/  (ambiente virtual - se utilizado)



app.py: O código principal do aplicativo Flask.
basetreinamento1.csv e baseteste1.csv: Os arquivos CSV contendo os dados de treinamento e teste.
templates/: O diretório que contém os modelos HTML usados para renderizar as páginas da web.
venv/: O diretório do ambiente virtual (se utilizado).

Contribuição
Sinta-se à vontade para contribuir com melhorias neste projeto. Para fazer isso, siga as etapas usuais de fork e pull request.

Licença
Este projeto é distribuído sob a licença MIT.


