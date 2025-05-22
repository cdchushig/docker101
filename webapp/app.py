from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    nombre = None
    edad = None
    if request.method == "POST":
        nombre = request.form.get("nombre")
        edad = request.form.get("edad")
    return render_template("index.html", nombre=nombre, edad=edad)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
