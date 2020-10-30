import json

import requests
from flask import Flask, jsonify
from flask_cors import CORS

from location import Location

from location import Location

app = Flask("name-gathering")
CORS(app)

locations = [Location(location='Rotvoll', lat=63.4308, lon=10.4034),
             Location(location='Vassbotnen', lat=58.89, lon=5.72),
             Location(location='Sandsli', lat=60.2939, lon=5.2824)
             ]


@app.route("/nowcast")
def root():
    location_info_list = []
    for loc in locations:
        location_info_list.append(loc.nowcast())
    weather = jsonify({"locations": location_info_list})

    return weather


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
