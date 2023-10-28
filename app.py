import numpy as np
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

# Carregar o modelo treinado
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Coletar dados do formulário HTML
        features = [float(request.form['Total']), float(request.form['HP']),
                    float(request.form['Attack']), float(request.form['Defense']),
                    float(request.form['Sp. Atk']), float(request.form['Sp. Def']),
                    float(request.form['Speed'])]

        # Realizar a previsão
        pred = model.predict([features])
        predicted_legendary = pred[0]

        if predicted_legendary == 1:
            prediction_text = "Este Pokémon é lendário!"
        else:
            prediction_text = "Este Pokémon não é lendário."

        return render_template("index.html", prediction_text=prediction_text)

    except Exception as e:
        return render_template("index.html", prediction_text="Erro: Certifique-se de preencher todos os campos corretamente.")

@app.route("/api", methods=["POST"])
def api_predict():
    try:
        data = request.get_json()

        # Coletar dados do JSON
        total = float(data['Total'])
        hp = float(data['HP'])
        attack = float(data['Attack'])
        defense = float(data['Defense'])
        sp_atk = float(data['Sp. Atk'])
        sp_def = float(data['Sp. Def'])
        speed = float(data['Speed'])

        # Realizar a previsão
        features = [total, hp, attack, defense, sp_atk, sp_def, speed]
        pred = model.predict([features])
        predicted_legendary = pred[0]

        return jsonify({"is_legendary": bool(predicted_legendary)})

    except Exception as e:
        return jsonify({"error": "Erro: Certifique-se de enviar os dados corretamente."})

if __name__ == "__main":
    app.run(debug=True)
