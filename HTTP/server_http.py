from flask import Flask, request, jsonify

app = Flask(__name__)

temperature_value = 25  # default

@app.route('/temperature', methods=['GET'])
def get_temperature():
    return jsonify({"temperature": temperature_value})

@app.route('/temperature', methods=['POST'])
def update_temperature():
    global temperature_value
    data = request.get_json()
    if 'temperature' in data:
        temperature_value = data['temperature']
        return jsonify({"message": "Temperature updated"}), 200
    else:
        return jsonify({"error": "No temperature provided"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

