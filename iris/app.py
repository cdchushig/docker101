from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            features = [float(request.form[f'feature{i}']) for i in range(1, 5)]
            prediction = model.predict([features])[0]
        except Exception as e:
            prediction = f"Error: {str(e)}"
    return render_template('index.html', prediction=prediction)
