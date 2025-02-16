from flask import Flask, jsonify
import requests

app = Flask(__name__)

API_URL = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD"

def get_btc_data():
    response = requests.get(API_URL)
    data = response.json()
    return data

@app.route('/signal')
def get_signal():
    btc_data = get_btc_data()
    
    entry_price = btc_data["USD"]
    stop_loss = entry_price * 0.98  # 2% Stop Loss
    target_price = entry_price * 1.05  # 5% Target
    trend = "Upside" if entry_price > stop_loss else "Downside"

    return jsonify({
        "coin": "BTC",
        "price": entry_price,
        "stop_loss": stop_loss,
        "target": target_price,
        "direction": trend
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)