from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.get(url)
    data = response.json()
    return f"<h1>BTC Price</h1><p>USD: {data['USD']}$</p><p>JPY: {data['JPY']}¥</p><p>EUR: {data['EUR']}€</p>"

if __name__ == '__main__':
    app.run(debug=True)
