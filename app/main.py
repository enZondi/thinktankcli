# app/main.py
from flask import Flask, render_template_string, jsonify
from ivanti_client import fetch_ivanti_incidents

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>ThinkTank CLI</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-dark text-white text-center p-5">
  <div class="container">
    <h1 class="display-4">🧠 ThinkTank CLI</h1>
    <p class="lead">{{ message }}</p>
    <hr class="bg-light">
    <p>Cloud-native container powered by ACR Tasks</p>
  </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE, message="Container is Live!")

@app.route("/api/incidents")
def get_incidents():
    data = fetch_ivanti_incidents()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
