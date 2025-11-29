from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask App is running!"

@app.route("/api")
def api():
    data = {
        "message": "Welcome to the API endpoint",
        "status": "success"
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

