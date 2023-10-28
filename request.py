import requests

url = 'http://localhost:5000/api'
data = {
    "Total": 318, 
    "HP": 45, 
    "Attack": 49, 
    "Defense": 49, 
    "Sp. Atk": 65, 
    "Sp. Def": 65, 
    "Speed": 45
}

r = requests.post(url, json=data)

result = r.json()
if "is_legendary" in result:
    if result["is_legendary"]:
        print("Este Pokémon é lendário!")
    else:
        print("Este Pokémon não é lendário!")
else:
    print("Erro na resposta da API.")
