from editing.complet import rendrecomplet, est_complet

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

def test_verifcomplet():
    if est_complet(automatevoulu):
        if est_complet(automate)==False:
            return True
    return False

def test_complet():
    nautomate = rendrecomplet(automate)

    if nautomate == automatevoulu:
        return True
    else:
        return False