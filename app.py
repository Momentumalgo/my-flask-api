from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/trade_data', methods=['POST'])
def trade_data():
    data = request.get_json()
    print("Received data from EA:", data)
    return jsonify({"message": "Success!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)