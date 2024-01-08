from editing.complet import rendrecomplet

def test_complet():
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
            "2": {"b": ["3"], "b": ["2"]},
            "3": {"a": ["3"], "b": ["2"]}
        },
        "Etats_initiaux": ["1"],
        "Etats_finaux": ["3"],
        "Nom" : "automate"
    }
	
    nautomate = rendrecomplet(automate)
	
    if nautomate == automatevoulu:
        return True
    else:
        return False