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