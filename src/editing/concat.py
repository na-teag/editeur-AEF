# Create an automate from the concatenation of two automates 

import data.structure as strct
import data.file as file
from copy import deepcopy


def concat (automate1, automate2) :
	"""
	### Description : 
		This function returns a new automate being the concatenation of two automates

	### Return : 
		automate1.automate2
	"""

	# create new automate 
	automateFinal = {
		"Etats": {},
		"Etats_initiaux": [],
		"Etats_finaux": [],
		"Nom": ""
	}
  
	i=0
	#link the old state name (automate1) to the one in the new automate
	oldToNew1 = {}
	#link the old state name (automate2) to the one in the new automate
	oldToNew2= {}

	#implementing state with a unique name 
	for state in automate1["Etats"]:
			automateFinal["Etats"][f"e{i}"] = {}
			for key in automate1["Etats"][state]:
				automateFinal["Etats"][f"e{i}"][key] = list(automate1["Etats"][state][key])
			oldToNew1[state] = f"e{i}"
			i += 1
	
	for state in automate2["Etats"]:
		automateFinal["Etats"][f"e{i}"] = {}
		for key in automate2["Etats"][state]:
			automateFinal["Etats"][f"e{i}"][key] = list(automate2["Etats"][state][key])
		oldToNew2[state] = f"e{i}"
		i += 1

	#updating transtion with new name
		
	i = 0
	for state in automateFinal["Etats"]:
		for key in automateFinal["Etats"][state]:
			for sk in range(0,len(automateFinal["Etats"][state][key])):
				if i < len(automate1["Etats"]):
					automateFinal["Etats"][state][key][sk] =  oldToNew1[automateFinal["Etats"][state][key][sk]]
				else:
					automateFinal["Etats"][state][key][sk] =  oldToNew2[automateFinal["Etats"][state][key][sk]]
		i+=1
			
	#linking end of automate 1 to the start of automate 2 (copying transition of initial state of automate2 into the final state of automate 1)
	for end in automate1["Etats_finaux"]:
		toLink = automateFinal["Etats"][oldToNew1[end]]
		for start in automate2["Etats_initiaux"]:
			for key in automateFinal["Etats"][oldToNew2[start]]:
				for state in automateFinal["Etats"][oldToNew2[start]][key]:

					if key in toLink:
						if state not in toLink[key]:
							toLink[key].append(state)
					else:
						toLink[key] = [state]
	
	#adding end and start
	for state in automate1["Etats_initiaux"]:
		automateFinal["Etats_initiaux"].append(oldToNew1[state])
	
	for state in automate2["Etats_finaux"]:
		if state not in automate2["Etats_initiaux"]:
			automateFinal["Etats_finaux"].append(oldToNew2[state])
		else:
			for s in automate1["Etats_initiaux"]:
				automateFinal["Etats_finaux"].append(oldToNew1[s])
	

	#removing the inital state of automate2 and replacing them by the final state of automate 1
	nameOfDeletedState = []
	for state in automate2["Etats_initiaux"]:
		del automateFinal["Etats"][oldToNew2[state]]
		nameOfDeletedState.append(oldToNew2[state])

	for state in automateFinal["Etats"]:
		for key in automateFinal["Etats"][state]:
			for deleted in nameOfDeletedState:
				if deleted in automateFinal["Etats"][state][key]:
					automateFinal["Etats"][state][key].remove(deleted)
					for s in automate1["Etats_finaux"]:
						if s not in automateFinal["Etats"][state][key]:
							automateFinal["Etats"][state][key].append(oldToNew1[s])

	return automateFinal


def concatener(liste, num_automate): # Choose the 2nd automaton, run the concat() function, and add the result to the list
	num_automate2 = -1
	print("\n\n\n\n\n\n\n\n\n\n\n")
	print("Séléctionnez un deuxième AEF à comparer")
	liste, num_automate2 = file.loadAutomate(liste, num_automate2)
	automate = deepcopy(concat(liste[num_automate], liste[num_automate2]))
	automate["Nom"] = liste[num_automate]["Nom"] + "_" + liste[num_automate2]["Nom"]
	num_automate = len(liste)
	liste.append(automate)
	return liste, num_automate