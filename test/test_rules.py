import pytest
from domain.rules import Rules
from domain.deck import Deck

@pytest.mark.rules
def test_check_body_infected():
    body = {
        "organ1" : {"name" : "hueso", "type" : "organ", "color" : "yellow"},
        "organ2" : {"name" : "estómago", "type" : "organ", "color" : "green"},
        "organ3" : {"name" : "cerebro", "type" : "organ", "color" : "blue"},
        "organ4" : {"name": "corazón", "type" : "organ", "color" : "red"},
        "organ5" : {},

        "effect1" : {"name" : "virus de hueso", "type" : "virus", "color" : "yellow"},
        "effect2" : {"name" : "medicamento de estómago", "type" : "medicine", "color" : "green"},
        "effect3" : {"name": "virus de cerebro", "type" : "virus", "color" : "blue"},
        "effect4" : {"name" : "medicamento de corazón", "type" : "medicine", "color" : "red"},
        "effect5" : {},

        "inmune1" : False,
        "inmune2" : False,
        "inmune3" : False,
        "inmune4" : True,
        "inmune5" : False
    }

    assert False == Rules().check_body(body)

@pytest.mark.rules
def test_check_body_health():
    body = {
        "organ1" : {"name" : "hueso", "type" : "organ", "color" : "yellow"},
        "organ2" : {"name" : "estómago", "type" : "organ", "color" : "green"},
        "organ3" : {"name" : "cerebro", "type" : "organ", "color" : "blue"},
        "organ4" : {"name": "corazón", "type" : "organ", "color" : "red"},
        "organ5" : {},

        "effect1" : {},
        "effect2" : {"name" : "medicamento de estómago", "type" : "medicine", "color" : "green"},
        "effect3" : {},
        "effect4" : {"name" : "medicamento de corazón", "type" : "medicine", "color" : "red"},
        "effect5" : {},

        "inmune1" : False,
        "inmune2" : False,
        "inmune3" : False,
        "inmune4" : True,
        "inmune5" : False
    }

    assert True == Rules().check_body(body)

@pytest.mark.rules
def test_change_body():
    player_A = {
        "id" : "pa123",
        "name" : "name 1",
        "body" : {
            "organ1" : "organ 1",
            "organ2" : "organ 2",
            "organ3" : "organ 3"
        },
        "mallet" : ["virus", "medicine", "organ"]
    }
    player_B = {
        "id" : "pb123",
        "name" : "name 1",
        "body" : {
            "organ1" : "",
            "organ2" : "organ 2",
            "organ3" : ""
        },
        "mallet" : ["virus", "medicine", "organ"]
    }

    assert player_A["body"] == Rules().change_body(player_A, player_B)[1]["body"]
    assert player_B["body"] == Rules().change_body(player_A, player_B)[0]["body"]

@pytest.mark.rules
def test_change_organ():
    body_A = {
        "organs" : {
            "organ1" : "organo 1 A",
            "organ2" : "organo 2 A",
            "organ3" : "organo 3 A"
        }
    }
    body_B = {
        "organs" : {
            "organ1" : "organo 1 B",
            "organ2" : "organo 2 B",
            "organ3" : "organo 3 B"
        }
    }
    organ_A = "organo 1 A"
    organ_B = "organo 3 B"

    new_body_A = Rules().change_organ(body_A, body_B, organ_A, organ_B)[0]
    new_body_B = Rules().change_organ(body_A, body_B, organ_A, organ_B)[1]

    assert organ_A == new_body_B["organs"]["organ3"]
    assert organ_B == new_body_A["organs"]["organ1"]

@pytest.mark.rules
def test_stole_organ():
    body_A = {
        "organs" : {
            "organ1" : {
                "organ" : {},
                "effect" : {},
                "inmune" : False
            },
            "organ2" : {
                "organ" : {},
                "effect" : {},
                "inmune" : False
            },
            "organ3" : {
                "organ" : {},
                "effect" : {},
                "inmune" : False
            }
        }
    }
    organ = {
        "organ" : {"name": "corazón", "type" : "organ", "color" : "red"},
        "effect" : {"name" : "medicamento de corazón", "type" : "medicine", "color" : "red"},
        "inmune" : False
    }
    body_B = {
        "organs" : {
            "organ1" : {
                "organ" : {},
                "effect" : {},
                "inmune" : False
            },
            # Organo para robar
            "organ2" : organ,

            "organ3" : {
                "organ" : {},
                "effect" : {},
                "inmune" : False
            }
        }
    }

    new_body_A = Rules().stole_organ(body_A, body_B, organ)[0]
    new_body_B = Rules().stole_organ(body_A, body_B, organ)[1]

    assert new_body_A["organs"]["organ1"] == organ
    assert new_body_B["organs"]["organ2"] != organ

@pytest.mark.rules
def test_drop_mallets():
    players = [
        {
            "id" : "1111",
            "name" : "Player 1",
            "mallet" : ["carta_1_P1", "carta_2_P1", "carta_3_P1"],
            "body" : {},
        },
        {
            "id" : "2222",
            "name" : "Player 2",
            "mallet" : ["carta_1_P2", "carta_2_P2", "carta_3_P2"],
            "body" : {},
        },
        {
            "id" : "3333",
            "name" : "Player 3",
            "mallet" : ["carta_1_P3", "carta_2_P3", "carta_3_P3"],
            "body" : {},
        }
    ]
    test_deck = [
        "Platano",
        "Pera",
        "Naranja",
        "Manzana",
        "Aguacate",
        "Piña",
        "Pomelo",
        "Cereza",
        "Kiwi",
        "Maracuyá",
        "Mandarina",
        "Papaya"
    ]

    deck = Deck(test_deck[:])
    
    player_1 = {
        "id" : "1111",
        "name" : "Player 1",
        "mallet" : ["carta_1_P1", "carta_2_P1", "carta_3_P1"],
        "body" : {},
    }
    player_2 = {
        "id" : "2222",
        "name" : "Player 2",
        "mallet" : ["carta_1_P2", "carta_2_P2", "carta_3_P2"],
        "body" : {},
    }
    player_3 = {
        "id" : "3333",
        "name" : "Player 3",
        "mallet" : ["carta_1_P3", "carta_2_P3", "carta_3_P3"],
        "body" : {},
    }

    new_players = Rules().drop_mallets([player_1, player_2, player_3], deck.get_cards_available())
    new_players.clear()

    assert players[0] != player_1
    assert players[1] != player_2
    assert players[2] != player_3