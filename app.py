from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("stock_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    prediction = None
    if request.method == "POST":
        ticker = request.form["ticker"].upper()

        # Since your model is trained on last price, we’ll just take a dummy input for now
        # Later we can connect Yahoo Finance to fetch the latest price automatically
        try:
            latest_price = float(request.form["price"])  # user enters price manually for now
            predicted_price = model.predict(np.array([[latest_price]]).reshape(-1, 1))
            prediction = f"Predicted Next Day Price for {ticker}: ${predicted_price[0]:.2f}"
        except:
            prediction = "⚠️ Invalid input! Please enter a valid number."

    return render_template("predict.html", prediction=prediction)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

