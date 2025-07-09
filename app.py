from flask import Flask, jsonify
import json

app = Flask(__name__)


with open("wac-artists.json", "r") as f:
    data = json.load(f)
    artists = {item["data"]["id"]: item["data"] for item in data}


@app.route("/artwork/<string:id>")
def show_post(id):
    if id in artists:
        return jsonify(artists[id])
    else:
        return jsonify({"error": "Artwork not found"}), 404
