import numpy as np
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import pickle
import pandas as pd

app = Flask(__name__)
CORS(app)
model = pickle.load(open("model.pkl", "rb"))
pokemon_data = pd.read_csv("Pokemon.csv")
labels_names = pokemon_data["Type 1"].unique()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = [float(request.form[x]) for x in labels_names]
    final_features = [np.array(features)]
    pred = model.predict(final_features)
    output = labels_names[pred[0]]
    return render_template("index.html", prediction_text="Pokemon Type: " + output)

@app.route("/api", methods=["POST"])
def results():
    data = request.get_json(force=True)
    feature_names = labels_names.tolist()
    features = [data.get(feature, 0) for feature in feature_names]
    pred = model.predict([np.array(features)])
    output = labels_names[pred[0]]
    return jsonify({"prediction": output})

if __name__ == "__main":
    app.run(debug=True)