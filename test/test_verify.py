import pytest

from domain.verify import Verify

@pytest.mark.verify
def test_ver_virus_color_true():
    organs = {
        "organ1" : {
            "organ" : {"name": "corazón", "type" : "organ", "color" : "red"},
            "effect" : {"name" : "virus de corazón", "type" : "virus", "color" : "red"},
            "inmune" : False
        },
        "organ2" : {
            "organ" : {"name" : "hueso", "type" : "organ", "color" : "yellow"},
            "effect" : {"name" : "virus comodín", "type" : "virus", "color" : "multicolor"},
            "inmune" : False
        },
        "organ3" : {
            "organ" : {"name" : "estómago", "type" : "organ", "color" : "green"},
            "effect" : {},
            "inmune" : False
        },
        "organ4" : {
            "organ" : {"name" : "cerebro", "type" : "organ", "color" : "blue"},
            "effect" : {"name" : "medicamento de cerebro", "type" : "medicine", "color" : "blue"},
            "inmune" : False
        },
        "organ5" : {
            "organ" : {"name" : "comodín", "type" : "organ", "color" : "multicolor"},
            "effect" : {"name" : "medicamento comodín", "type" : "medicine", "color" : "multicolor"},
            "inmune" : False
        }
    }
    assert True == Verify().ver_virus_color(organs)

@pytest.mark.verify
def test_ver_virus_color_false():
    organs = {
        "organ1" : {
            "organ" : {"name": "corazón", "type" : "organ", "color" : "red"},
            "effect" : {"name" : "virus de corazón", "type" : "virus", "color" : "red"},
            "inmune" : False
        },
        "organ2" : {
            "organ" : {"name" : "hueso", "type" : "organ", "color" : "yellow"},
            "effect" : {"name" : "virus comodín", "type" : "virus", "color" : "multicolor"},
            "inmune" : False
        },
        "organ3" : {
            "organ" : {"name" : "estómago", "type" : "organ", "color" : "green"},
            "effect" : {},
            "inmune" : False
        },
        "organ4" : {
            "organ" : {"name" : "cerebro", "type" : "organ", "color" : "blue"},
            "effect" : {"name" : "medicamento de cerebro", "type" : "medicine", "color" : "green"},
            "inmune" : False
        },
        "organ5" : {
            "organ" : {"name" : "comodín", "type" : "organ", "color" : "multicolor"},
            "effect" : {"name" : "medicamento comodín", "type" : "medicine", "color" : "multicolor"},
            "inmune" : False
        }
    }
    assert False == Verify().ver_virus_color(organs)

@pytest.mark.verify
def test_can_be_inmune():
    organ = {
        "organ" : {},
        "effect" : {},
        "inmune" : False
    }
    assert False == Verify().can_be_inmune(organ)
    
    organ = {
        "organ" : {"name": "corazón", "type" : "organ", "color" : "red"},
        "effect" : {},
        "inmune" : False
    }
    assert False == Verify().can_be_inmune(organ)
    
    organ = {
        "organ" : {},
        "effect" : {"name" : "virus de corazón", "type" : "virus", "color" : "red"},
        "inmune" : False
    }
    assert False == Verify().can_be_inmune(organ)
    
    organ = {
        "organ" : {"name": "corazón", "type" : "organ", "color" : "red"},
        "effect" : {},
        "inmune" : False
    }
    assert False == Verify().can_be_inmune(organ)
    
    organ = {
        "organ" : {"name": "corazón", "type" : "organ", "color" : "red"},
        "effect" : {"name" : "virus de corazón", "type" : "virus", "color" : "red"},
        "inmune" : False
    }
    assert False == Verify().can_be_inmune(organ)
    
    organ = {
        "organ" : {"name": "corazón", "type" : "organ", "color" : "red"},
        "effect" : {"name" : "virus comodín", "type" : "virus", "color" : "multicolor"},
        "inmune" : False
    }
    assert False == Verify().can_be_inmune(organ)
    
    organ = {
        "organ" : {"name": "corazón", "type" : "organ", "color" : "red"},
        "effect" : {"name" : "medicamento de corazón", "type" : "medicine", "color" : "red"},
        "inmune" : False
    }
    assert True == Verify().can_be_inmune(organ)
    
    organ = {
        "organ" : {"name": "corazón", "type" : "organ", "color" : "red"},
        "effect" : {"name" : "medicamento comodín", "type" : "medicine", "color" : "multicolor"},
        "inmune" : False
    }
    assert True == Verify().can_be_inmune(organ)
    
    organ = {
        "organ" : {"name" : "comodín", "type" : "organ", "color" : "multicolor"},
        "effect" : {"name" : "medicamento de corazón", "type" : "medicine", "color" : "red"},
        "inmune" : False
    }
    assert True == Verify().can_be_inmune(organ)
    
    organ = {
        "organ" : {"name" : "comodín", "type" : "organ", "color" : "multicolor"},
        "effect" : {"name" : "medicamento comodín", "type" : "medicine", "color" : "multicolor"},
        "inmune" : False
    }
    assert True == Verify().can_be_inmune(organ)