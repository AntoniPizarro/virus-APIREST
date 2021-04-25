from flask import jsonify, g
from services.db_engine import get_db
from repository.models import Cards, Users
from mongoengine.queryset.visitor import Q


class data_base:
    @staticmethod
    def ping():
        '''
        'Respuesta de prueba
        '''
        res = {
            "game" : "Virus",
            "description" : "VIRUS! es un juego para 2 a 6 jugadores, en el que tendrás que construir un cuerpo humano mientras evitas que tus rivales infecten, destruyan o roben tus órganos.",
            "players" : "2-6",
            "time" : "20 min",
            "pegui" : "8+"
        }
        return jsonify(res)

    @staticmethod
    def get_cards(db, url):
        '''
        'Obtiene todas las cartas de la collección de la baraja
        '''
        db = get_db(db, url)
        cards_list = []
        for card in g.Cards.objects():
            cards_list.append(card.to_json())
        if len(cards_list) > 0:
            return jsonify({"cards": cards_list})
        else:
            return jsonify({"cards": ["N/A"]})
    
    @staticmethod
    def get_user(db, url, code):
        '''
        'Obtiene un usuario por código
        '''
        db = get_db(db, url)
        user = g.Users.objects(code=code).first()
        try:
            return user.to_json()
        except:
            return None
    
    @staticmethod
    def get_users(db, url):
        '''
        'Obtiene todos los usuarios de la partida
        '''
        db = get_db(db, url)
        user_list = []
        for user in g.Users.objects():
            user_list.append(user.to_json())
        if len(user_list) > 0:
            return jsonify({"items": user_list})
        else:
            return jsonify({"items": "N/A"})
    
    @staticmethod
    def register_user(db, url, user):
        '''
        'Añade un usuario a la collección de usuarios
        '''
        db = get_db(db, url)
        user_found = g.Users.objects(code=user["code"]).first()
        if not user_found:
            Users(
                code=user["code"], name=user["name"], body=user["body"], mallet=user["mallet"]
            ).save()
            res = "User added"
        else:
            res = "An user with code " + user["code"] + " already exists."
        return jsonify({"result" : res})
    
    @staticmethod
    def get_user_mallet(db, url, code):
        db = get_db(db, url)
        user = g.Users.objects(code=code).first()
        try:
            return user.to_json()["mallet"]
        except:
            return None