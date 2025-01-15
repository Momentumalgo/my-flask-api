from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

# Route to handle trade data from EA
@app.route('/trade_data', methods=['POST'])
def trade_data():
    data = request.get_json()
    print("Received data from EA:", data)

    # Adjust time to MetaTrader server time (assumed UTC+2)
    server_time = datetime.utcnow() + timedelta(hours=2)
    print("Server Time (UTC+2):", server_time)

    # Example response to the EA
    response = {
        "command": "AdjustRisk",
        "new_risk_percent": 0.5,
        "server_time": server_time.strftime("%Y-%m-%d %H:%M:%S")
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
