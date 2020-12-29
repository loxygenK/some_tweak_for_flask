from flask import jsonify

from config.application import app


@app.route("/hello")
def hello_world():
    return jsonify({"response": "hello_world!"})


