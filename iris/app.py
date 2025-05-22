from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Cargar el modelo entrenado
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            features = [
                float(request.form["sepal_length"]),
                float(request.form["sepal_width"]),
                float(request.form["petal_length"]),
                float(request.form["petal_width"])
            ]
            pred = model.predict([features])[0]
            clases = ["Setosa", "Versicolor", "Virginica"]
            return f"<h2>Predicción: {clases[pred]}</h2><a href='/'>Volver</a>"
        except:
            return "<h2>Error en los datos. Asegúrate de que los valores sean numéricos.</h2><a href='/'>Volver</a>"
    return render_template("form.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
