import flask
from flask import request, jsonify
import mid_logic

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET"])
def home():
    return "<H1>I am a cat</H1>"

@app.route("/logs", methods=["GET"])
def log_range_page():
    j = mid_logic.JournalSevrice()
    a = request.args
    # j.log_range(params["low_stamp"], params["high_stamp"])
    return jsonify(j.log_range(request.args["low_stamp"], request.args["high_stamp"]))

@app.route("/animal", methods=["GET"])
def one_animal():
    if "id" in request.args:
        id = int(request.args["id"])
    else:
        return "No id field provided"
    results=[]
    for animal in animals:
        if animal["id"] == id:
            results.append(animal)

    return jsonify(results)

app.run()