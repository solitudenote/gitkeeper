from flask import Flask, jsonify, render_template
import requests
from config import config
import os
from urllib.parse import parse_qsl
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/authenticate/<code>", methods=["GET"])
def authenticate(code):
    creds = get_access_token(*build_config(code))
    return jsonify(creds)


def build_config(code):
    url = config["oauth_url"]
    headers = {"Content-Type": "application/json"}
    payload = {
        "client_id": os.environ.get(config["oauth_client_id"]),
        "client_secret": os.environ.get(config["oauth_client_secret"]),
        "code": code,
    }
    return url, headers, payload


def get_access_token(url, headers, payload):
    response = requests.post(url, headers=headers, params=payload)
    qs = dict(parse_qsl(response.text))
    creds = {item: qs[item] for item in qs}
    return creds


if __name__ == "__main__":
    app.run()
