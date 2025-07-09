from flask import Flask, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)
CORS(app, resources=r"/artist/*")

with open("wac-artists.json", "r") as f:
    data = json.load(f)
    artists = {item["data"]["id"]: item["data"] for item in data}


@app.route("/artist/<string:id>")
def show_post(id):
    if id in artists:
        return jsonify(artists[id])
    else:
        return jsonify({"error": "Artist not found"}), 404
