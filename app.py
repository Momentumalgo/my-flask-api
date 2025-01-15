import openai
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define a route to process trading signals
@app.route('/trade_data', methods=['POST'])
def trade_data():
    data = request.get_json()
    print("Received data from EA:", data)

    # Example OpenAI API request
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Analyze the following trading data: {data}",
            max_tokens=100
        )
        result = response['choices'][0]['text'].strip()
    except Exception as e:
        return jsonify({"error": str(e)})

    # Respond to the EA with the result
    return jsonify({"command": "AdjustRisk", "new_risk_percent": 0.5, "analysis": result})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
