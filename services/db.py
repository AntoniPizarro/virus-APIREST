from flask import jsonify, g
from services.db_engine import get_db
from repository.models import Cards
from mongoengine.queryset.visitor import Q


class data_base:
    @staticmethod
    def ping():
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
        db = get_bd(db, url)
        cards_list = []
        for card in g.Cards.objects():
            cards_list.append(card.to_json())
        if len(cards_list) > 0:
            return jsonify({"items": cards_list})
        else:
            return jsonify({"items": ["N/A"]})

    @staticmethod
    def get_item(name, db, url):
        db = get_bd(db, url)
        items_list = []
        items_list_name = []
        for item in g.Cards.objects():
            items_list.append(item.to_json())
        for item in items_list:
            if item["name"].lower() == name.lower():
                items_list_name.append(item)
        if len(items_list_name) > 0:
            return jsonify({"items": items_list_name})
        else:
            return jsonify({"items": "N/A"})

    @staticmethod
    def add_item(args, db, url):
        db = get_bd(db, url)
        item = {
            "name": args["name"],
            "sell_in": args["sell_in"],
            "quality": args["quality"],
        }
        Cards(
            name=item["name"], sell_in=item["sell_in"], quality=item["quality"]
        ).save()
        print("item added")

    @staticmethod
    def delete_item(item, db, url):
        db = get_bd(db, url)
        item = g.Cards.objects(
            Q(name=item["name"])
            & Q(quality=item["quality"])
            & Q(sell_in=item["sell_in"])
        ).first()
        if not item:
            return "The specified item does not exist"
        else:
            item.delete()
            return "Item deleted: " + str(item)

    @staticmethod
    def update_quality(db, url):
        db = get_bd(db, url)
        for item in g.Cards.objects():
            item_object = create_item_object(item.to_json())
            item_object.update_quality()
            item.sell_in = item_object.sell_in
            item.quality = item_object.quality
            item.save()

    @staticmethod
    def get_item_by_sell_in(sell_in, db, url):
        db = get_bd(db, url)
        items_list = []
        for item in g.Cards.objects(sell_in=sell_in):
            items_list.append(item.to_json())
        if len(items_list) > 0:
            return jsonify({"items": items_list})
        else:
            return jsonify({"items": "N/A"})

    @staticmethod
    def get_item_by_quality(quality, db, url):
        db = get_bd(db, url)
        items_list = []
        for item in g.Cards.objects(quality=quality):
            items_list.append(item.to_json())
        if len(items_list) > 0:
            return jsonify({"items": items_list})
        else:
            return jsonify({"items": "N/A"})
