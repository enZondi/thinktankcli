from flask import Flask, send_from_directory, jsonify
from app.ivanti import fetch_incidents
import os

app = Flask(__name__)

@app.route("/")
def root_index():
    return send_from_directory(".", "index.html")

@app.route("/api/incidents")
def get_incidents():
    data = fetch_incidents()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
