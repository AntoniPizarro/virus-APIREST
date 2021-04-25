from flask import Flask, jsonify, redirect
from flask_cors import CORS
import json

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
    '''
    'Obten todas las cartas de la partida
    '''
    return db.get_cards(DB, HOST)
    
@app.route("/users", methods=["GET"])
def get_users():
    '''
    'Obten el usuario por código
    '''
    return db.get_users(DB, HOST)

@app.route("/users/<string:code>/", methods=["GET"])
def get_user(code):
    '''
    'Obten el usuario por código
    '''
    user = db.get_user(DB, HOST, code)
    return jsonify({"users" : user})

@app.route("/users/<string:code>/body", methods=["GET"])
def get_user_body(code):
    '''
    'Obten el cuerpo del usuario por código
    '''
    user = db.get_user(DB, HOST, code)
    if user == None:
        return jsonify({"user" : user})
    else:
        return jsonify({"user_name" : user["name"], "user_code" : user["code"], "body" : user["body"]})

@app.route("/users/<string:code>/mallet", methods=["GET"])
def get_user_mallet(code):
    '''
    'Obten el mazo del usuario por código
    '''
    user = db.get_user(DB, HOST, code)
    if user == None:
        return jsonify({"user" : user})
    else:
        return jsonify({"user_name" : user["name"], "user_code" : user["code"], "mallet" : user["mallet"]})


# POST

@app.route("/register_user/<string:user>", methods=["POST"])
def register_user(user):
    '''
    'Registra un nuevo usuario
    '''
    db.register_user(DB, HOST, json.loads(user))
    return redirect("../users", code=302)

@app.route("/users/<string:code>/uses/<string:card>", methods=["POST"]) # Pendiente
def user_uses_card(code, card):
    return jsonify({"user" : user, "mallet" : card})


# TEST
@app.route("/test")
def test_route():
    return "Ruta de testeo"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5505)
    dict = {"code":"0002","name":"Pepe","mallet":["Mazo de Pepe"],"body":{"cuerpo":"de Pepe"}}