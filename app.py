import os
import requests
from config import config
from flask_cors import CORS
from urllib.parse import parse_qsl
from exceptions import APIException
from flask import Flask, jsonify, render_template

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return render_template("index.html")


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

    # Raise exceptions if client_id or client_secret not found.
    if not payload["client_id"]:
        raise APIException("Client Id Not found in environment", status_code=422)
    if not payload["client_secret"]:
        raise APIException("Client secret Not found in environment", status_code=422)
    return url, headers, payload


def get_access_token(url, headers, payload):
    response = requests.post(url, headers=headers, params=payload)
    qs = dict(parse_qsl(response.text))
    creds = {item: qs[item] for item in qs}
    return creds


# Global error handler
@app.errorhandler(APIException)
def handle_api_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == "__main__":
    app.run()
