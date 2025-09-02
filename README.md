📈 Stock Price Predictor

A simple web application built with Flask, scikit-learn, and yFinance that predicts the future price of a stock based on its recent market data.

🚀 Features

🌐 Web interface built with Flask.

📊 Enter any stock ticker symbol (e.g., AAPL, TSLA, MSFT).

🔎 Fetches real-time stock data using Yahoo Finance
.

🤖 Predicts future stock price using a pre-trained ML model (stock_model.pkl).

🎨 Clean UI with green theme styling.

📂 Project Structure
stock-predictor/
│── app.py                # Flask app entry point
│── stock_model.pkl       # Pre-trained ML model
│── requirements.txt      # Python dependencies
│── templates/
│    ├── index.html       # Home page
│    ├── predict.html     # Prediction page
│── static/
│    └── styles.css       # CSS styling
│── README.md             # Project documentation



🛠️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/stock-predictor.git
cd stock-predictor

2️⃣ Create Virtual Environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the App Locally
python app.py


Now open your browser at 👉 http://127.0.0.1:5000/

📸 Screenshots
Home Page:
<img width="1911" height="912" alt="image" src="https://github.com/user-attachments/assets/ff115200-0245-4927-a919-e06265bd2905" />
Prediction Page:
<img width="1910" height="908" alt="image" src="https://github.com/user-attachments/assets/a22cdc57-d30f-4b80-a0da-f0d2e82973d3" />

🧑‍💻 Tech Stack

Backend: Flask

ML Model: scikit-learn

Data Source: yFinance

Frontend: HTML, CSS

⚡ Future Improvements

Add support for more advanced ML/DL models (LSTMs, Prophet, etc.)

Show stock history graph before prediction.

Deploy on AWS/GCP/Heroku for scalability.

📜 License

This project is licensed under the MIT License.

✨ Built with love & code 💻

