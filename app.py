from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

@app.route('/trade_data', methods=['POST'])
def trade_data():
    data = request.json
    symbol = data.get('symbol', 'XAUUSD')
    risk_percent = data.get('risk_percent', 1.0)

    # Use OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Analyze the market for {symbol} with a risk percentage of {risk_percent}.",
        max_tokens=50
    )

    return jsonify(response.choices[0].text.strip())

if __name__ == '__main__':
    app.run(debug=True)
