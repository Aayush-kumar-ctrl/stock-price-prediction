from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("../models/stock_model.pkl")

@app.route('/')
def home():
    return "Welcome to Stock Price Predictor! Use /predict?open=...&high=...&low=...&volume=..."

@app.route('/predict')
def predict():
    open_p = float(request.args.get('open'))
    high_p = float(request.args.get('high'))
    low_p = float(request.args.get('low'))
    volume = float(request.args.get('volume'))

    prediction = model.predict(np.array([[open_p, high_p, low_p, volume]]))
    return f"Predicted Closing Price: ₹{prediction[0]:.2f}"

if __name__ == '__main__':
    app.run(debug=True)
