import os
from flask import Flask, request, jsonify
import openai
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load .env variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/trade_data', methods=['POST'])
def trade_data():
    data = request.get_json()
    print("Received data from EA:", data)

    # Send data to ChatGPT
    prompt = f"Based on this trading data: {data}, what trading action should I take?"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )

    chat_response = response.choices[0].text.strip()
    print("ChatGPT Response:", chat_response)

    # Adjust time to MetaTrader server time (UTC+2)
    server_time = datetime.utcnow() + timedelta(hours=2)

    # Return the ChatGPT response to the EA
    response_data = {
        "command": chat_response,
        "server_time": server_time.strftime("%Y-%m-%d %H:%M:%S")
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
