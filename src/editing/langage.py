import data.file as file

def generer_langage(automate): # Generate the language recognized by the given automaton.
	langage = set()
	etats_initiaux = automate["Etats_initiaux"]

	def dfs(etat_actuel, mot_actuel):
		nonlocal langage
		transitions = automate["Etats"][etat_actuel]
		
		if mot_actuel == "":
			if etat_actuel in automate["Etats_finaux"]:
				langage.add("")
		
		for transition, etats_suivants in transitions.items():
			for etat_suivant in etats_suivants:
				dfs(etat_suivant, mot_actuel + transition)
	
	for etat_initial in etats_initiaux:
		dfs(etat_initial, "")
	
	return langage

def automates_equivalents(automate1, automate2): # Check if two automata are equivalent, i.e., recognize the same language.
	langage1 = generer_langage(automate1)
	langage2 = generer_langage(automate2)

	return langage1 == langage2


def test_automates_equivalents(liste, num_automate): # Choose the 2nd automaton and run the automates_equivalents() function
	num_automate2 = -1
	print("\n\n\n\n\n\n\n\n\n\n\n")
	print("Séléctionnez un deuxième AEF à comparer")
	liste, num_automate2 = file.loadAutomate(liste, num_automate2)
	if(automates_equivalents(liste[num_automate], liste[num_automate2])):
		print("les automates sont équivalents")
	else:
		print("les automates ne sont pas équivalents")
	return liste, num_automate