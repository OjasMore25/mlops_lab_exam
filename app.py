from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Docker deployed successfully by Ojas Ganesh More - 2023BCS0043"})

@app.route("/metrics")
def metrics():
    with open("metrics.json", "r") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)