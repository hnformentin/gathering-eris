import requests
from flask import Flask, jsonify

app = Flask("name-gathering")

dummy_result = {
    "locations": [
        {
            "location": "Vassbotnen",
            "air_temperature": 7.4,
            "precipitation_rate": 0.0,
            "wind_speed": 3.6,
            "clothing": "rainwear",
            "time_until_rain": 90,
            "next_1_hours": {
                "symbol_code": "cloudy",
                "precipitation_amount": 0.0
            },
        },
        {
            "location": "Rotvoll",
            "air_temperature": 7.4,
            "precipitation_rate": 0.0,
            "wind_speed": 3.6,
            "clothing": "rainwear",
            "time_until_rain": 90,
            "next_1_hours": {
                "symbol_code": "cloudy",
                "precipitation_amount": 0.0
            }
        }
    ]
}

trondheim = 'https://api.met.no/weatherapi/nowcast/2.0/complete?lat=63.4308&lon=10.4034'


def nowcast():
    return requests.get(trondheim).content


@app.route("/nowcast")
def root():
    weather = nowcast()
    weather = jsonify(dummy_result)

    return weather


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
