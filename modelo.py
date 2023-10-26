import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
import pickle

# Carregando o arquivo Pokemon.csv em um DataFrame
pokemon_data = pd.read_csv('Pokemon.csv')

# Extraindo os recursos (features) e os rótulos (labels)
x = pokemon_data[['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation', 'Legendary']]
y = pokemon_data['Type 1']

# Realizando o split da base para teste
from sklearn.model_selection import train_test_split
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

# Treinando um classificador de árvore de decisão
clf = tree.DecisionTreeClassifier()
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
