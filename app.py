import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to handle trade data from EA
@app.route('/trade_data', methods=['POST'])
def trade_data():
    data = request.get_json()
    print("Received data from EA:", data)

    # Example response to the EA
    response = {
        "command": "AdjustRisk",
        "new_risk_percent": 0.5
    }
    return jsonify(response)

# Route to handle the root URL
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Run the app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
