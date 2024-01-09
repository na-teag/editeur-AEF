from editing.deter import rendredeterministe, est_deterministe

automatevoulu ={
    "Etats": {
        "1": {"a": ["1,3"], "b": ["2"]},
        "1,3": {"a": ["4,1,3"], "b": ["2"]},
        "2": {"b": ["1,4"]},
        "4,1,3": {"a": ["4,1,3"], "b": ["2"]},
        "1,4": {"a": ["4,1,3"], "b": ["2"]}
    },
    "Etats_initiaux": ["1"],
    "Etats_finaux": ["2"],
    "Nom" : "automate_deterministe"
}

automate ={
    "Etats": {
        "1": {"a": ["1","3"], "b": ["2"]},
        "2": {"b": ["1","4"]},
        "3": {"a": ["4"], "b": ["2"]},
        "4": {"a": ["4"], "b": ["2"]}
    },
    "Etats_initiaux": ["1"],
    "Etats_finaux": ["2"],
    "Nom" : "automate"
}

def test_verifdeter():
    if est_deterministe(automatevoulu):
        if est_deterministe(automate)==False:
            return True
    else:
        return False

def test_deter():
    nautomate = rendredeterministe(automate)
	
    if nautomate == automatevoulu:
        return True
    else:
        return False