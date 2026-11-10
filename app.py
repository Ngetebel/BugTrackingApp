from flask import Flask, jsonify

app = Flask(__name__)

bugs = [
    {
        "id": 1,
        "title": "Login Error",
        "status": "Open"
    }
]

@app.route("/")
def home():
    return jsonify({
        "message": "Bug Tracking API"
    })

@app.route("/bugs")
def get_bugs():
    return jsonify(bugs)

if __name__ == "__main__":
    app.run(debug=True)