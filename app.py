from flask import Flask, request, jsonify

app = Flask(__name__)

# Root route
@app.route('/')
def home():
    return "Welcome to the Flask API!"

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

if __name__ == '__main__':
    app.run(debug=True)
