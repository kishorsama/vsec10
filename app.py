from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # This is where your model logic would go
    # For now, we return a mock prediction
    data = request.get_json()
    return jsonify({
        "status": "success",
        "prediction": "AI Model result for: " + str(data.get("input", "no data"))
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)