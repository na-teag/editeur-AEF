# This file contains all functions to edit an automate
import display.display as dis
import data.file as file
import re

def verif(val):
    return bool(re.match(r'^[\w-]+$', val)) # letters, numbers, underscore or -


def editStates(list_automate, automate_selected): # add or delete transition or states

	if(list_automate[automate_selected]["Nom"] == ""):
		list_automate[automate_selected]["Nom"] = input("Veuillez donner un nom à l'automate : ")
	if(list_automate[automate_selected]["Nom"] == ""):
		return file.loadAutomate(list_automate, automate_selected)
	test = 1
	while test:
		print("\n\n\n\n\n\n\n\n\n")
		dis.displayAEF(list_automate[automate_selected])
		print("\nEntrez les états et transitions sous la forme : état, transition, état_suivant.\nUne transition déjà existante sera supprimée, ou ajoutée si elle n'existe pas")
		print("\nCaractères autorisés : lettres chiffres underscores et tirets")
		transition_input = input("Entrez la nouvelle partie de votre AEF ou appuyez sur Entrer pour terminer : ").split(',') # state name : no special characters
		# print(transition_input)
		if(len(transition_input) == 3 and verif(transition_input[0].strip()) and verif(transition_input[1].strip()) and verif(transition_input[2].strip())):
			etat = transition_input[0].strip() # delete space
			transition = transition_input[1].strip()
			etat_suivant = transition_input[2].strip()
			if(etat_suivant not in list_automate[automate_selected]["Etats"]):# Add state if not already existing
				list_automate[automate_selected]["Etats"][etat_suivant] = {}
			if(etat not in list_automate[automate_selected]["Etats"]): # if not existing, it's added with the transition    
				list_automate[automate_selected]["Etats"][etat] = {}
				list_automate[automate_selected]["Etats"][etat][transition] = []
				list_automate[automate_selected]["Etats"][etat][transition].append(etat_suivant)
			elif(transition not in list_automate[automate_selected]["Etats"][etat]): # if the state exist but without this transition, create it
				list_automate[automate_selected]["Etats"][etat][transition] = []
				list_automate[automate_selected]["Etats"][etat][transition].append(etat_suivant)
			elif(etat_suivant in list_automate[automate_selected]["Etats"][etat][transition]): # if the state already exist with this transition, it's deleted
				list_automate[automate_selected]["Etats"][etat][transition].remove(etat_suivant)
				if(len(list_automate[automate_selected]["Etats"][etat][transition]) == 0):
					del list_automate[automate_selected]["Etats"][etat][transition]

			else: # the state exist with this transition but leading to another state, so we add the next state to the list
				list_automate[automate_selected]["Etats"][etat][transition].append(etat_suivant)

			liste = [] # list for state that must be deleted (cannot delete state while in a loop of the list of state)
			for etat in list_automate[automate_selected]["Etats"]:
				if(state_isolated(list_automate[automate_selected], etat) and len(list_automate[automate_selected]["Etats"].keys())-len(liste) > 1): # if the state has no transition other than itself beginning or leading to it
					liste.append(etat) # add the state to the list of state to be deleted
			if(len(liste) != 0):
				for etat in liste:
					del list_automate[automate_selected]["Etats"][etat]
				if(list_automate[automate_selected]["Etats"] == {}): # if all the states have been deleted, ask to enter a new FA
					print("\033[2J") # clear the screen
					print("\n\n\n\n\n\n\n\n\n\n\nVous ne pouvez pas manipuler un AEF vide ou contenant des états n'ayant aucune liaison directe ou indirecte entre eux\n\nmerci d'en réenregistrer un :")
					list_automate[automate_selected]["Etats_initiaux"] = []
					list_automate[automate_selected]["Etats_finaux"] = []
					return editStates(list_automate, automate_selected)
				print("\033[2J") # clear the screen
				print("\n\n\n\n\n\n\n\n\n\n\n")
				print("Des états non reliés entre eux, que ce soit de manière directe ou indirecte ont été détectés.")
				print("\nCe programme n'étant pas capable de gérer un AEF avec deux parties distinctes, les etats concernés ont été supprimés")
			else:
				print("\033[2J") # clear the screen


		elif(transition_input == ['']): # if the answer is empty
			if(len(list_automate[automate_selected]["Etats"].keys()) >= 1): # if there is enough states
				print("\033[2J") # clear the screen
				list_automate, automate_selected = changeStatesInitFinal(list_automate, automate_selected, 0)
				print("\033[2J") # clear the screen
				list_automate, automate_selected = changeStatesInitFinal(list_automate, automate_selected, 1)
				test = 0
				print("\033[2J") # clear the screen
			else:
				print("\033[2J") # clear the screen
				print("\n\n\n\n\n\n\n\n\n\n\n")
				print("Veuillez entrer au moins une transition entre deux états")

		else: # the answer is incorrect
			print("\033[2J") # clear the screen
			print("\n\n\n\n\n\n\n\n\n\n\n")
			print("votre entrée n'est pas correcte")
	return list_automate, automate_selected


def testTransition(automate, etat2): # testing if a state has transition leading to it
	test = 0
	for etat in automate["Etats"]:
		for transition in automate["Etats"][etat].keys():
			for liste_etats_suivants in automate["Etats"][etat][transition]:
				if(etat2 in liste_etats_suivants):
					if(etat != etat2):
						return 1 # the state have another state leading to it
					else:
						test = 1 # the state is leading to itself
	if(test == 0):
		return 0 # the state hasn't any state leadnig to it
	else:
		return 2 # the state has only one transition leading ot it, from itself


def state_isolated(automate, etat): # testing if the state has transition other than itself leading or beginning from it
	no_transition = 1
	for transition in automate["Etats"][etat].keys():
		for etat_suivant in automate["Etats"][etat][transition]:
			if(etat_suivant != etat): # testing if the state has transition beginning from it that are not leading to itself
				no_transition = 0
				break
		if(no_transition == 0):
			break
	if(no_transition): # if the state doesn't have any transition beginning from it
		if(testTransition(automate, etat) != 1): # if the state has no transition leading to it
			return 1
		else:
			return 0
	else:
		return 0
			


def deleteStates(list_automate, automate_selected): # delete all apparition of a state
	print("\n\n\n\n\n\n\n\n")
	dis.displayAEF(list_automate[automate_selected])
	print("\n\n\n\n")
	choix = input("Entrez l'état à supprimer ou appuyez sur entrer pour revenir en arrière : ").strip()
	if(choix in list_automate[automate_selected]["Etats"]):
		choix2 = input(f"Etes-vous sûr de vouloir supprimer l'état {choix} ? Cette action est irréversible\n1 : oui\n2 : non\n\n\n").strip()
		if(choix2 == "1"):
			dico = {}
			del list_automate[automate_selected]["Etats"][choix] # delete the state from the list of state of the FA
			for etat, transition in list_automate[automate_selected]["Etats"].items():
				for etat_suivant in transition.values():
					if(choix in etat_suivant): # if other states have transition leading to the deleted state, remove these transitions
						etat_suivant.remove(choix)
				
				for trans in transition.keys():
					if(list_automate[automate_selected]["Etats"][etat][trans] == []): # after deleting the state, if there is transition starting from it, they are added to a list to be deleted (cannot do it when the loop is on these same transitions)
						dico[etat] = trans
			for etat in dico:
				del list_automate[automate_selected]["Etats"][etat][dico[etat]]
			if(choix in list_automate[automate_selected]["Etats_initiaux"]): # if the state is in the finals or initials state liste, it's deleted too
				list_automate[automate_selected]["Etats_initiaux"].remove(choix)
			if(choix in list_automate[automate_selected]["Etats_finaux"]):
				list_automate[automate_selected]["Etats_finaux"].remove(choix)

			liste = []
			for etat in list_automate[automate_selected]["Etats"]:
				if(state_isolated(list_automate[automate_selected], etat)): # if the state has no transition other than itself beginning or leading to it
						liste.append(etat)
			if(len(liste) != 0):
				#print(liste)
				for etat in liste: # if the liste of state isn't empty, the states in the list are deleted
					del list_automate[automate_selected]["Etats"][etat] 
					if(etat in list_automate[automate_selected]["Etats_initiaux"]): # if the deleted states are in the initals or finals state list, they are deleted from there too
						list_automate[automate_selected]["Etats_initiaux"].remove(etat)
					if(etat in list_automate[automate_selected]["Etats_finaux"]):
						list_automate[automate_selected]["Etats_finaux"].remove(etat)
				
			if(len(list_automate[automate_selected]["Etats"]) <= 1): # if all the states have been removed, enter a new FA
				print("\033[2J") # clear the screen
				print("Vous ne pouvez pas manipuler un AEF vide, veuillez en entrer un nouveau :")
				print("\n\n\n\n\n\n\n\n")
				return editStates(list_automate, automate_selected)
			if(len(list_automate[automate_selected]["Etats_initiaux"]) == 0): # if there is 0 initial state, ask another one
				print("\033[2J") # clear the screen
				print("Vous avez supprimé le seul état initial, veuillez en entrer un nouveau")
				print("\n\n\n\n\n\n\n\n")
				list_automate, automate_selected = changeStatesInitFinal(list_automate, automate_selected, 0)
			if(len(list_automate[automate_selected]["Etats_finaux"]) == 0): # if there is 0 final state, ask another one
				print("\033[2J") # clear the screen
				print("Vous avez supprimé le seul état final, veuillez en entrer un nouveau")
				print("\n\n\n\n\n\n\n\n")
				list_automate, automate_selected = changeStatesInitFinal(list_automate, automate_selected, 1)
		else:
			print("\033[2J") # clear the screen
			print("action annulée")
			print("\n\n\n\n\n\n\n\n")
	elif(choix == ""):
		print("\033[2J") # clear the screen
		return list_automate, automate_selected
	else:
		print("\033[2J") # clear the screen
		print("Veuillez entrer une des options proposées")
		print("\n\n\n\n\n\n\n\n")
	return list_automate, automate_selected


def renameStates(list_automate, automate_selected): # rename all apparitions of a state (can be used to fuse two states)
	dis.displayAEF(list_automate[automate_selected])
	print("\n\n\n\n")
	choix = input("Entrez l'état à renommer ou appuyez sur entrer pour revenir en arrière : ").strip()
	ancien = choix
	if(choix in list_automate[automate_selected]["Etats"]):
		nouveau = input(f"Entrez le nouveau nom à donner à l'état {ancien} ou appuyez sur entrer pour revenir en arrière : ").strip()
		if(nouveau in list_automate[automate_selected]["Etats"]):
			choix = input(f"L'état {nouveau} existe déjà dans l'AEF, êtes vous sûr de vouloir fusionner les états {ancien} et {nouveau} ?\n1 : oui\n2 : non\n\n").strip()
			if(choix != "1"):
				print("\033[2J") # clear the screen
				return list_automate, automate_selected
			else:
				if(len(list_automate[automate_selected]["Etats"]) < 3):
					test = 0
					for transition in list_automate[automate_selected]["Etats"][ancien].keys():
						if(nouveau in list_automate[automate_selected]["Etats"][ancien][transition]):
							test = 1
					for transition in list_automate[automate_selected]["Etats"][nouveau].keys():
						if(ancien in list_automate[automate_selected]["Etats"][nouveau][transition]):
							test = 1
					if(not(len(list_automate[automate_selected]["Etats"]) == 2 and test)): # if the result is a state with a transition on itself, it's ok
						print("\033[2J") # clear the screen
						print("impossible de fusionner les deux états, car il s'agit des deux seuls états de l'AEF")
						print("\n\n\n\n\n\n\n\n")
						return list_automate, automate_selected
		elif(nouveau == ""):
			print("\033[2J") # clear the screen
			return list_automate, automate_selected
		else:
			list_automate[automate_selected]["Etats"][nouveau] = {} # if the new state doesn't exist, create it


		for transition, liste_etats_suivants in list_automate[automate_selected]["Etats"][ancien].items(): # duplicate all the transition to the new state
			if(transition not in list_automate[automate_selected]["Etats"][nouveau].keys()):
				list_automate[automate_selected]["Etats"][nouveau][transition] = []
			for transition2 in liste_etats_suivants:
				list_automate[automate_selected]["Etats"][nouveau][transition].append(transition2)
			list(set(list_automate[automate_selected]["Etats"][nouveau][transition]))
		for etat in list_automate[automate_selected]["Etats"]:
			if(etat != ancien):
				for transition, liste_etats_suivants in list_automate[automate_selected]["Etats"][etat].items(): # change all the transition leading to this state
					if(ancien in list_automate[automate_selected]["Etats"][etat][transition]):
						list_automate[automate_selected]["Etats"][etat][transition].remove(ancien)
						if(nouveau not in list_automate[automate_selected]["Etats"][etat][transition]):
							list_automate[automate_selected]["Etats"][etat][transition].append(nouveau)
		del list_automate[automate_selected]["Etats"][ancien] # after all the transitions have been removed, the state is deleted

		if(ancien in list_automate[automate_selected]["Etats_initiaux"]): # if the former state is in the list of initials or finales states, rename them too
			list_automate[automate_selected]["Etats_initiaux"].remove(ancien)
			if(nouveau not in list_automate[automate_selected]["Etats_initiaux"]):
				list_automate[automate_selected]["Etats_initiaux"].append(nouveau)
		if(ancien in list_automate[automate_selected]["Etats_finaux"]):
			list_automate[automate_selected]["Etats_finaux"].remove(ancien)
			if(nouveau not in list_automate[automate_selected]["Etats_finaux"]):
				list_automate[automate_selected]["Etats_finaux"].append(nouveau)

	elif(choix == ""):
		print("\033[2J") # clear the screen
		return list_automate, automate_selected
	else:
		print("\033[2J") # clear the screen
		print("Erreur : l'état", ancien, "n'existe pas dans l'AEF")
		print("\n\n\n\n\n\n\n\n")

	return list_automate, automate_selected



def changeStatesInitFinal(list_automate, automate_selected, nbr): # add or delete initials or finals states
	test = 1
	if(nbr == 0):
		etat = "Etats_initiaux" # same function for both final and initial modification, so the name are saved to print the correct one
		nom = "initial"
	elif(nbr == 1):
		etat = "Etats_finaux"
		nom = "final"
	else:
		print("erreur, le 3e parametre de changer_etats_ini_fin() ne peut être que 0 ou 1")
		exit(1)
	while test:
		print("\n\n\n\n\n\n\n\n\n\n\n")
		dis.displayAEF(list_automate[automate_selected])
		print("\n\n\nEntrez un état", nom, "déjà présent pour l'effacer, appuyez sur entrer pour sortir")
		choix = input(f"Entrez l'état {nom} que vous voulez ajouter : ").strip()
		if choix in list_automate[automate_selected][etat]:
			list_automate[automate_selected][etat].remove(choix) # if the choice is already here, delete it
			print("\033[2J") # clear the screen
		elif(choix in list_automate[automate_selected]["Etats"]): # if the choice isn't already here and exist in the FA
			if(nbr == 0 and len(list_automate[automate_selected]["Etats_initiaux"]) >= 1): # if there is already an initial state (one initial state max is imposed by the project)
				print("\033[2J") # clear the screen
				print("Vous ne pouvez rentrer qu'un état initial")
			else:
				if(nbr == 0):
					if(len(list_automate[automate_selected]["Etats"][choix].keys()) != 0 or choix in list_automate[automate_selected]["Etats_finaux"]): # check if initial state lead to another state or is a final state
						list_automate[automate_selected][etat].append(choix)
						print("\033[2J") # clear the screen
					else:
						print("\033[2J") # clear the screen
						print("Erreur, l'état", choix, "ne peux pas être défini comme état initial car il ne contient aucune transition et n'est pas final")
				else:
					if(testTransition(list_automate[automate_selected], choix) != 0 or choix in list_automate[automate_selected]["Etats_initiaux"]):
						list_automate[automate_selected][etat].append(choix)
						print("\033[2J") # clear the screen
					else:
						print("\033[2J") # clear the screen
						print("Erreur, l'état", choix, "ne peux pas être défini comme état final car aucune transition n'y conduit")
		elif(choix == ""):
			if(0<len(list_automate[automate_selected][etat])): # if there is enough initial or final state
				test = 0
			else: # if there isn't enough
				print("\033[2J") # clear the screen
				print("Erreur, votre AEF doit contenir au moins un état", nom)
		else:
			print("\033[2J") # clear the screen
			print("Erreur, l'état", choix, "n'existe pas dans cet automate")
	print("\033[2J") # clear the screen
	return list_automate, automate_selected



def demandDelete(liste_automate, automate_selected): # ask confirmation before deleting the FA
	print("\033[2J") # clear the screen
	dis.displayAEF(liste_automate[automate_selected])
	choix = input("\n\n\nEtes-vous sûr de vouloir supprimer cet AEF ?\n1 : oui\n2 : non\n\n").strip()
	if(choix == "1"):
		print("\033[2J") # clear the screen
		return deleteAutomate(liste_automate, automate_selected)
	else:
		print("\033[2J") # clear the screen
		return liste_automate, automate_selected


def deleteAutomate(liste_automate, automate_selected): # delete the FA
	liste_automate.pop(automate_selected)
	automate_selected = -1
	return file.loadAutomate(liste_automate, automate_selected)


