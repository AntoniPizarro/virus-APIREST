from mongoengine import *


class Cards(Document):
    name = StringField(required=True)
    type = StringField(required=True)
    color = StringField(required=True)

    def to_json(self):
        return {"name": self.name, "type": self.type, "color": self.color}

class User_list(Document):
    name = StringField(required=True)
    deck = ListField(required=True)
    body = DictField(required=True)

    def to_json(self):
        return {"name": self.name, "deck": self.deck, "body": self.body}

'''
Definiendo estructura del body de cada usuario

{
    "organ1" : {},
    "organ2" : {},
    "organ3" : {},
    "organ4" : {},
    "organ5" : {},

    "effect1" : {},
    "effect2" : {},
    "effect3" : {},
    "effect4" : {},
    "effect5" : {},

    "inmune1" : False,
    "inmune2" : False,
    "inmune3" : False,
    "inmune4" : False,
    "inmune5" : False
}
'''