import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Carregando o arquivo Pokemon.csv em um DataFrame
pokemon_data = pd.read_csv('Pokemon.csv')

# Selecionando as colunas relevantes
features = ['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
target = 'Legendary'  # Nome da coluna para prever se um Pokémon é lendário

# Extraindo os recursos (features) e os rótulos (labels)
x = pokemon_data[features]
y = pokemon_data[target]

# Realizando o split da base para teste
from sklearn.model_selection import train_test_split
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

# Treinando um classificador de árvore de decisão
clf = DecisionTreeClassifier()
clf = clf.fit(x_treino, y_treino)

# Realizando previsões
preditos = clf.predict(x_teste)
print("Preditos:", preditos)
print("Real    :", y_teste)

# Calculando a acurácia
from sklearn.metrics import accuracy_score
print("Acuracia:", accuracy_score(y_teste, preditos))

# Salvando o modelo treinado em um arquivo
pickle.dump(clf, open('model.pkl', 'wb'))
model = pickle.load(open('model.pkl', 'rb'))
