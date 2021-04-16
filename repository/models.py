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
        return {"name": self.name, "type": self.type, "color": self.color}