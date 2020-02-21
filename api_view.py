import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

animals = [
    {"id": 1, "owl": "hooter"},
    {"id": 2, "cat": "meowface"},
    {"id": 3, "dog": "woofle"}]

@app.route("/", methods=["GET"])
def home():
    return "<H1>I am a cat</H1>"

@app.route("/animals", methods=["GET"])
def animals_page():
    return jsonify(animals)

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