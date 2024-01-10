from editing.complet import rendrecomplet, est_complet

def get_automate():
    automate ={
        "Etats": {
            "1": {"a": ["2"], "b": ["2"]},
            "2": {"b": ["3"]},
            "3": {"b": ["2"]}
        },
        "Etats_initiaux": ["1"],
        "Etats_finaux": ["3"],
        "Nom" : "automate"
    }
    return automate

def get_automate_voulu():
    automatevoulu ={
        "Etats": {
            "1": {"a": ["2"], "b": ["2"]},
            "2": {"b": ["3"], "a": ["2"]},
            "3": {"b": ["2"], "a": ["3"]}
        },
        "Etats_initiaux": ["1"],
        "Etats_finaux": ["3"],
        "Nom" : "automate"
    }
    return automatevoulu

def test_verifcomplet():
    if est_complet(get_automate_voulu()):
        if est_complet(get_automate()):
            return False
        else :
            return True
    else:
        return False

def test_complet():
    nautomate = rendrecomplet(get_automate())

    if nautomate == get_automate_voulu():
        return True
    else:
        return False

