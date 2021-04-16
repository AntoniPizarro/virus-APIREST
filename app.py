from flask import Flask, jsonify
from flask_cors import CORS

from services.db import data_base as db
from services.db_engine import init_app

DB = "virus"
HOST = "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.4uubd.mongodb.net/" + DB + "?retryWrites=true&w=majority"

app = Flask(__name__)
CORS(app)
init_app(app, DB, HOST)


# GET

@app.route("/", methods=["GET"])
def ping():
    return db.ping()

@app.route("/cards", methods=["GET"])
def get_cards():
    return db.get_cards(DB, HOST)

@app.route("/<string:user>/", methods=["GET"])
def get_user(user):
    return jsonify({"user" : user})

@app.route("/<string:user>/cards", methods=["GET"])
def get_user_cards(user):
    return jsonify({"user" : user, "cards" : "cards list"})

@app.route("/<string:user>/body", methods=["GET"])
def get_user_body(user):
    return jsonify({"user" : user, "body" : "body cards"})

@app.route("/<string:user>/deck", methods=["GET"])
def get_user_deck(user):
    return jsonify({"user" : user, "deck" : "deck cards"})


# POST

@app.route("/<string:user>/uses/<string:card>", methods=["POST"])
def use_card(user, card):
    return jsonify({"user" : user, "uses" : card})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5505)