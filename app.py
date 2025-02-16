from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    api_url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.get(api_url)
    data = response.json()
    return render_template('index.html', price=data)

if __name__ == "__main__":
    app.run(debug=True)
