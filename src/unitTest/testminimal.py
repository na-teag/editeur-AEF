from editing.minimal import toMinimal


autommate = {
	"Etats": {
		"q0": {"a": ["q2"], "b": ["q1"]},
		"q1": {"a": ["q2"], "b": ["q1"]},
		"q2": {"a": ["q3"], "b": ["q2"]},
		"q3": {"a": ["q5"], "b": ["q4"]},
        "q4": {"a": ["q5"], "b": ["q4"]},
		"q5": {"a": ["q6"], "b": ["q5"]},
		"q6": {"a": ["q5"], "b": ["q7"]},
		"q7": {"a": ["q5"], "b": ["q7"]}
	},
	"Etats_initiaux": ["q0"],
	"Etats_finaux": ["q0","q3", "q4", "q6", "q7"],
	"Nom" : "test"
}

print(f"automate: {autommate}")
print("using toMinimal...")
calculated = {
    'Etats': {
        'q0': {'a': 'q2', 'b': 'q1'}, 
        'q1': {'a': 'q2', 'b': 'q1'}, 
        'q2': {'a': 'q3', 'b': 'q2'}, 
        'q3': {'a': 'q2', 'b': 'q3'}
        },
    'Etats_initiaux': ['q0'], 
    'Etats_finaux': ['q0', 'q3'], 
    'Nom': 'test_minimal'
}
r = toMinimal(autommate)
if r == calculated:
    print("test successfull")
else:
    print("test failed")
