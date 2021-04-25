from services.db import data_base
from domain.rules import Rules
from domain.deck import Deck
from domain.verify import Verify

class Game:

    @staticmethod
    def user_infect_virus(db, url, user, card, target):
        target = data_base().get_user(db, url, target)
        user = data_base().get_user(db, url, user)