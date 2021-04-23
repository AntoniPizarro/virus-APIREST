import pytest

@pytest.mark.verify
def test_ver_virus_color():
    organs = {
        "organ1" : {
            "organ" : {"name": "corazón", "type" : "organ", "color" : "red"},
            "effect" : {...},
            "inmune" : False
        },
        "organ2" : {
            "organ" : {...},
            "effect" : {...},
            "inmune" : False
        },
        "organ3" : {
            "organ" : {...},
            "effect" : {...},
            "inmune" : False
        },
        "organ4" : {
            "organ" : {...},
            "effect" : {...},
            "inmune" : False
        },
        "organ5" : {
            "organ" : {...},
            "effect" : {...},
            "inmune" : False
        }
    }