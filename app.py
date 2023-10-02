from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)

# Carregue seus dados de treinamento e teste em arquivos CSV
df_treinamento = pd.read_csv('basetreinamento1.csv', header=None)
df_teste = pd.read_csv('baseteste1.csv', header=None)

# Preencha os valores nulos com strings vazias
df_treinamento = df_treinamento.fillna('')
df_teste = df_teste.fillna('')

# Extraia as frases e emoções dos dados de treinamento e teste
X_treinamento = df_treinamento.iloc[:, 0]  # Coluna 0 contém as frases de treinamento
y_treinamento = df_treinamento.iloc[:, 1]  # Coluna 1 contém as emoções de treinamento

X_teste = df_teste.iloc[:, 0]  # Coluna 0 contém as frases de teste
y_teste = df_teste.iloc[:, 1]  # Coluna 1 contém as emoções de teste

# Crie um objeto CountVectorizer e converta o texto em vetores numéricos
vectorizer = CountVectorizer()
X_treinamento = vectorizer.fit_transform(X_treinamento)
X_teste = vectorizer.transform(X_teste)

# Crie e treine o modelo Naive Bayes
clf = MultinomialNB()
clf.fit(X_treinamento, y_treinamento)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/prever', methods=['POST'])
def prever_emocao():
    texto = request.form['texto']
    vetorizado = vectorizer.transform([texto])
    emocao_prevista = clf.predict(vetorizado)[0]

    # Calcule as probabilidades das emoções
    probabilidades = clf.predict_proba(vetorizado)[0]

    # Mapeie as emoções
    emocoes = clf.classes_


    # Resultado no formato desejado
    resultado = {
        'Alegria': probabilidades[0] * 100,
        'Raiva': probabilidades[1] * 100,
        'Tristeza': probabilidades[2] * 100,
        'Medo': probabilidades[3] * 100,
        'Surpresa': probabilidades[4] * 100,
        'Desgosto': probabilidades[5] * 100
    }

    return render_template('resultado.html', texto=texto, emocao=emocao_prevista, resultados=resultado)

if __name__ == '__main__':
    app.run(debug=True)
