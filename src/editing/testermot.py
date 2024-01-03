from data.structure import alphabet

'''
automate ={
    "Etats": {
        "q0": {"a": ["q1","q0"]},
        "q1": {"c": ["q0","q2"], "d": ["q1"]},
        "q2": {"a": ["q0"], "b": ["q1"]}
    },
    "Etats_initiaux": ["q0"],
    "Etats_finaux": ["q2"]
}
'''





def tester(automate):
	test = 1
	mot = []
	alphabet2 = alphabet(automate)
	while test:
		letter = input("Entrez la prochaine lettre de votre mot : ")
		if(letter != ""):
			if(letter in alphabet2):
				mot.append(letter)
			else:
				print("\n\nCette lettre n'est pas présente dans l'automate, aucun mot ne peut la contenir")
		else:
			if(len(mot) == 0): # cancel and get to the previous menu
				return False
			else: # word complete, now test it
				test = 0

	for etat in automate["Etats_initiaux"]:
		if(mot[0] in automate["Etats"][etat].keys()):
			test += tester_mot(automate, mot, 0, etat)
			if(test):
				print("\033[2J")
				print("\n\nLe mot", mot, "a été trouvé dans l'automate")
				print("\n\n\n\n\n\n\n\n\n\n\n")
				return True
	print("\033[2J")
	print("\n\nLe mot", mot, "n'a pas été trouvé dans l'automate")
	print("\n\n\n\n\n\n\n\n\n\n\n")
	return False
		
	


def tester_mot(automate, mot, indice, etat_actuel):
		if(mot[indice] in automate["Etats"][etat_actuel].keys()): # if the next letter is accessible from here
			if(len(automate["Etats"][etat_actuel][mot[indice]]) == 1): # if there is only one possibility to select the right letter
				if(len(mot) <= indice+1): # if the next letter is the last one
					if(automate["Etats"][etat_actuel][mot[indice]][0] in automate["Etats_finaux"]): # if the state we go using the next letter is a final state
						#print("0")
						return 1
					else:
						#print("1")
						return 0
				else:
					#print("2")
					return tester_mot(automate, mot, indice+1, automate["Etats"][etat_actuel][mot[indice]][0])
			else: # if there is several possiblilty to select the right letter
				if(len(mot) <= indice+1): # if the next letter is the last one
					for etat_suivant in automate["Etats"][etat_actuel][mot[indice]]:
						if(etat_suivant in automate["Etats_finaux"]): # if the state we go using the next letter is a final state
							#print("3")
							return 1
					#print("4")
					return 0
						
				else:
					for etat_suivant in automate["Etats"][etat_actuel][mot[indice]]:
						#print("4.5")
						if(tester_mot(automate, mot, indice+1, etat_suivant)): # testing all the possibility 
							#print("5")
							return 1 # if a path has been found
					#print("6")
					return 0 # if no path found
		else:
			#print("7")
			return 0 # if the next letter isn't reachable from here
		
			