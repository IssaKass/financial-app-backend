from flask import Flask, jsonify
import os
import random
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route("/")
def index():
    return jsonify({"number": random.random()})


@app.route("/about")
def about():
    return "About"


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))