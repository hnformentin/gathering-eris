import os
import json
from flask import Flask, render_template

app = Flask("name-gathering")


@app.route("/")
def root():
    return json.dumps(["Hello world!"])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
