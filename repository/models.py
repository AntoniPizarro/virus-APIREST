from mongoengine import *


class Cards(Document):
    name = StringField(required=True)
    type = StringField(required=True)
    color = StringField(required=True)

    def to_json(self):
        return {"name": self.name, "type": self.type, "color": self.color}

class User_list(Document):
    id = StringField(required=True)
    name = StringField(required=True)
    mallet = ListField(required=True)
    body = DictField(required=True)

    def to_json(self):
        return {"id" : self.id, "name": self.name, "mallet": self.mallet, "body": self.body}

'''
Definiendo estructura del body de cada usuario

{
    "organs" : {
        "organ1" : {
            "organ" : {},
            "effect" : {},
            "inmune" : False/True
        },
        "organ2" : {
            "organ" : {},
            "effect" : {},
            "inmune" : False/True
        },
        "organ3" : {
            "organ" : {},
            "effect" : {},
            "inmune" : False/True
        },
        "organ4" : {
            "organ" : {},
            "effect" : {},
            "inmune" : False/True
        },
        "organ5" : {
            "organ" : {},
            "effect" : {},
            "inmune" : False/True
        }
    }
}
'''