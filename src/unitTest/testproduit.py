from editing.produit import product

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
print("using product...")
calculated = {
    'Etats': {
        'e0': {'a': ['e1'], 'b': ['e2']}, 
        'e1': {'a': ['e3'], 'b': ['e4']}, 
        'e2': {'b': ['e2']}, 
        'e3': {'a': ['e1'], 'b': ['e2']}, 
        'e4': {'a': ['e5'], 'b': ['e4']}, 
        'e5': {'a': ['e6']}, 
        'e6': {'a': ['e5'], 'b': ['e6']}
        }, 
    'Etats_initiaux': ['e0'], 
    'Etats_finaux': ['e1', 'e2', 'e4', 'e6'], 
    'Nom': 'test1xtest2'
}
r = product(automate1, automate2)
if r == calculated:
    print("test successfull")
else:
    print("test failed")

