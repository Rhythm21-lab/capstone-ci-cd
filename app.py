from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Hello from Capstone Flask API!"})

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    # Bind to 0.0.0.0 so container can expose it
    app.run(host="0.0.0.0", port=8000, debug=True)
