import os
import openai
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Load the OpenAI API key from environment variable
openai.api_key = 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

# Route to handle trade data from EA
@app.route('/trade_data', methods=['POST'])
def trade_data():
    data = request.get_json()
    print("Received data from EA:", data)

    # Call OpenAI API for processing
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Process this trading data: {data}",
            max_tokens=50
        )

        return jsonify({"response": response['choices'][0]['text'].strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
