import os
import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def index():
    return "Welcome to the AI trading Flask API!"

@app.route('/trade_data', methods=['POST'])
def trade_data():
    try:
        # Get data from the request
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid data"}), 400

        # Example prompt for OpenAI API
        prompt = f"Analyze this trading data: {data}"

        # Make a request to OpenAI's API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )

        # Send back the response
        return jsonify(response.choices[0].text.strip())

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
