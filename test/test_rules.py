import pytest
from domain.rules import Rules

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