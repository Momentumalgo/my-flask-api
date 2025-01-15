from flask import Flask, request, jsonify
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# Route to handle trading data
@app.route('/trade_data', methods=['POST'])
def trade_data():
    try:
        # Get data from the request
        data = request.get_json()
        
        # Extract values from the request
        symbol = data.get('symbol')
        risk_percent = data.get('risk_percent')
        
        # Process the data (example logic)
        new_risk_percent = risk_percent * 0.5  # Example calculation
        
        # Create the response
        response = {
            "new_risk_percent": new_risk_percent,
            "server_time": "2025-01-15T14:43:24Z"
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
