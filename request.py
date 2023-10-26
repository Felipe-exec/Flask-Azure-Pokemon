import requests

url = 'http://localhost:5000/api'
# Os nomes das características do Pokémon devem corresponder ao que você tem no modelo treinado
data = {
    "Total": 318, 
    "HP": 45, 
    "Attack": 49, 
    "Defense": 49, 
    "Sp. Atk": 65, 
    "Sp. Def": 65, 
    "Speed": 45, 
    "Generation": 1, 
    "Legendary": False
}

r = requests.post(url, json=data)

print(r.json())
