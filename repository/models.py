from mongoengine import *


class Cards(Document):
    name = StringField(required=True)
    type = StringField(required=True)
    color = StringField(required=True)

    def to_json(self):
        return {"name": self.name, "type": self.type, "color": self.color}

class Users(Document):
    code = StringField(required=True)
    name = StringField(required=True)
    mallet = ListField(required=True)
    body = DictField(required=True)

    def to_json(self):
        return {"code" : self.code, "name": self.name, "mallet": self.mallet, "body": self.body}

'''
Definiendo estructura de cada usuario

{
    "code" : "...",
    "name" : "...",
    "mallet" : [...],
    "body" : {...}
}

Cada mallet tendra una lista de cartas en la mano


Definiendo estructura del body de cada usuario

{
    "organs" : {
        "organ1" : {
            "organ" : {...},
            "effect" : {...},
            "inmune" : False/True
        },
        "organ2" : {
            "organ" : {...},
            "effect" : {...},
            "inmune" : False/True
        },
        "organ3" : {
            "organ" : {...},
            "effect" : {...},
            "inmune" : False/True
        },
        "organ4" : {
            "organ" : {...},
            "effect" : {...},
            "inmune" : False/True
        },
        "organ5" : {
            "organ" : {...},
            "effect" : {...},
            "inmune" : False/True
        }
    }
}
'''