from editing.concat import concat

automate1 = {
	"Etats": {
		"q0": {"a": ["q0"], "b": ["q1"]},
		"q1": {"b": ["q1"]}
	},
	"Etats_initiaux": ["q0"],
	"Etats_finaux": ["q1"],
	"Nom" : "test1"
}

automate2 = {
	"Etats": {
		"q0": {"a": ["q2"]},
		"q1": {"a": ["q2"]},
        "q2": {"a":["q0"], "b": ["q2"]}
	},
	"Etats_initiaux": ["q0", "q1"],
	"Etats_finaux": ["q2"],
	"Nom" : "test2"
}

print(f"automate 1: {automate1}")
print(f"automate 2: {automate2}")
print("using concat...")
calculated = {
    'Etats': {
        'e0': {'a': ['e0'], 'b': ['e1']}, 
        'e1': {'b': ['e1'], 'a': ['e4']}, 
        'e4': {'a': ['e1'], 'b': ['e4']}}, 
    'Etats_initiaux': ['e0'], 
    'Etats_finaux': ['e4'], 
    'Nom': ''
}
r = concat(automate1, automate2)
if r == calculated:
    print("test successfull")
else:
    print("test failed")
