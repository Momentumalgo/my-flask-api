import os
import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define a simple route to handle incoming POST requests
@app.route('/trade_data', methods=['POST'])
def handle_trade_data():
    # Parse the incoming JSON
    data = request.get_json()

    # Extract relevant fields
    symbol = data.get('symbol', 'XAUUSD')
    risk_percent = data.get('risk_percent', 1.0)

    # Example OpenAI prompt
    prompt = f"Based on the symbol {symbol} and risk percent {risk_percent}, suggest a trading strategy."

    try:
        # Call the OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )

        # Return the response
        return jsonify({
            "command": response['choices'][0]['text'].strip(),
            "new_risk_percent": risk_percent * 0.95  # Example adjustment
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app in production
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
