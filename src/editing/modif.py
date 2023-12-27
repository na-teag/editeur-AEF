# This file contains all functions to edit an automate
import display.display as dis
import data.file as file

def editStates(list_automate, automate_selected): # add or delete transition or states
	while(list_automate[automate_selected]["Nom"] == ""):
		list_automate[automate_selected]["Nom"] = input("Veuillez donner un nom à l'automate : ")
	test = 1
	while test:
		print("\n\n\n\n\n\n\n\n\n\n\n")
		dis.displayAEF(list_automate[automate_selected])
		print("\nEntrez les états et transitions sous la forme : état, transition, état_suivant.\nUne transition déjà existante sera supprimée, ou ajoutée si elle n'existe pas")
		print("\nCaractères interdits : espace virgule epsilon union étoile plus guillemets")
		transition_input = input("Entrez la nouvelle partie de votre AEF ou appuyez sur Entrer pour terminer : ").split(',') # nom d'état : pas d'espace, de virgule, de plus ou d'étoile, d'union, d'epsilon
		# print(transition_input)
		if(len(transition_input) == 3 and transition_input[0].strip() != "" and transition_input[1].strip() != "" and transition_input[2].strip() != "" and "+" not in transition_input[1].strip() and "*" not in transition_input[1].strip() and "ɛ" not in transition_input[1].strip() and "∪" not in transition_input[1].strip() and " " not in transition_input[1].strip() and " " not in transition_input[0].strip() and " " not in transition_input[2].strip() and "'" not in transition_input[1].strip() and "'" not in transition_input[0].strip() and "'" not in transition_input[2].strip() and '"' not in transition_input[1].strip() and '"' not in transition_input[0].strip() and '"' not in transition_input[2].strip()):
			etat = transition_input[0].strip() # delete space
			transition = transition_input[1].strip()
			etat_suivant = transition_input[2].strip()
			if(etat_suivant not in list_automate[automate_selected]["Etats"]):# Add state if not already existing
				list_automate[automate_selected]["Etats"][etat_suivant] = {}
			if(etat not in list_automate[automate_selected]["Etats"]): # if not existing, it' added with the transition    
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

			liste = []
			for etat in list_automate[automate_selected]["Etats"]:
				if(list_automate[automate_selected]["Etats"][etat] == {}): # if the state doesn't have any transition leading or beginning from it, it's deleted because it's not related tho the FA anymore
					if(testTransition(list_automate, automate_selected, etat) == 0): # testing if the state has transition leading to it
						liste.append(etat)
			if(len(liste) != 0):
				for etat in liste:
					del list_automate[automate_selected]["Etats"][etat]
				if(list_automate[automate_selected]["Etats"] == {}): # if all the states have been deleted, ask to enter a new FA
					print("\n\n\n\n\n\n\n\n\n\n\n\n\nVous ne pouvez pas manipuler un AEF vide, merci d'en réenregistrer un :")
					list_automate[automate_selected]["Etats_initiaux"] = []
					list_automate[automate_selected]["Etats_finaux"] = []
					return editStates(list_automate, automate_selected)
				if(set(list_automate[automate_selected]["Etats_initiaux"]) <= set(liste)): # if all the initials state have been deleted, ask for new one
					print("\n\n\n\n\n Il n'y a aucun état initial, veuillez en entrez un ")
					list_automate[automate_selected]["Etats_initiaux"] = []
					list_automate, automate_selected = changeStatesInitFinal(list_automate, automate_selected, 0)
				if(set(list_automate[automate_selected]["Etats_finaux"]) <= set(liste)): # same for fianl states
					print("\n\n\n\n\n Il n'y a aucun état final, veuillez en entrez un nouveau")
					list_automate[automate_selected]["Etats_finaux"] = []
					list_automate, automate_selected = changeStatesInitFinal(list_automate, automate_selected, 1)


		elif(transition_input == ['']): # if the answer is empty
			if(len(list_automate[automate_selected]["Etats"].keys()) >= 1):
				if(len(list_automate[automate_selected]["Etats_initiaux"]) < 1):
					list_automate, automate_selected = changeStatesInitFinal(list_automate, automate_selected, 0)
				if(len(list_automate[automate_selected]["Etats_finaux"]) < 1):
					list_automate, automate_selected = changeStatesInitFinal(list_automate, automate_selected, 1)
				test = 0
			else:
				print("Veuillez entrer au moins une transition entre deux états")

		else: # the answer is incorrect
			print("votre entrée n'est pas correcte")
	return list_automate, automate_selected


def testTransition(list_automate, automate_selected, etat2): # testing if a state has transition leading to it
	for etat in list_automate[automate_selected]["Etats"]:
		for transition in list_automate[automate_selected]["Etats"][etat].keys():
			for liste_etats_suivants in list_automate[automate_selected]["Etats"][etat][transition]:
				if(etat2 in liste_etats_suivants):
					return 1
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
			del list_automate[automate_selected]["Etats"][choix]
			for etat, transition in list_automate[automate_selected]["Etats"].items():
				for etat_suivant in transition.values():
					if(choix in etat_suivant):
						etat_suivant.remove(choix)
				
				for trans in transition.keys():
					if(list_automate[automate_selected]["Etats"][etat][trans] == []): # after deleting the state, if there is transition starting from it, they are added to a list to be deleted (cannot do it when the loop is on these same transitions)
						dico[etat] = trans
			for etat in dico:
				del list_automate[automate_selected]["Etats"][etat][dico[etat]]
			if(choix in list_automate[automate_selected]["Etats_initiaux"]): # if the state is in the liste, it's deleted
				list_automate[automate_selected]["Etats_initiaux"].remove(choix)
			if(choix in list_automate[automate_selected]["Etats_finaux"]):
				list_automate[automate_selected]["Etats_finaux"].remove(choix)

			liste = []
			for etat in list_automate[automate_selected]["Etats"]:
				if(list_automate[automate_selected]["Etats"][etat] == {}): # if a state isn't anywhere in the FA, it's deleted
					if(testTransition(list_automate, automate_selected, etat) == 0):
						liste.append(etat)
			if(len(liste) != 0):
				#print(liste)
				for etat in liste:
					del list_automate[automate_selected]["Etats"][etat] 
					if(etat in list_automate[automate_selected]["Etats_initiaux"]): # if the deleted states are in the initals or finals states, they are deleted too
						list_automate[automate_selected]["Etats_initiaux"].remove(etat)
					if(etat in list_automate[automate_selected]["Etats_finaux"]):
						list_automate[automate_selected]["Etats_finaux"].remove(etat)
				
			if(len(list_automate[automate_selected]["Etats"]) <= 1): # if all the states have been removed, enter a new FA
				print("\n\n\n\n\n\n\n\n\n\n\n\n\n\nVous ne pouvez pas manipuler un AEF vide, veuillez en entrer un nouveau :")
				return editStates(list_automate, automate_selected)
			if(len(list_automate[automate_selected]["Etats_initiaux"]) == 0): # if there is 0 initial state, ask another one
				print("\n\n\n\n\n\n\n\n\n\n\nVous avez supprimé le seul état initial, veuillez en entrer un nouveau")
				list_automate, automate_selected = changeStatesInitFinal(list_automate, automate_selected, 0)
			if(len(list_automate[automate_selected]["Etats_finaux"]) == 0): # if there is 0 final state, ask another one
				print("\n\n\n\n\n\n\n\n\n\n\nVous avez supprimé le seul état final, veuillez en entrer un nouveau")
				list_automate, automate_selected = changeStatesInitFinal(list_automate, automate_selected, 1)
		else:
			print("action annulée")
	elif(choix == ""):
		return list_automate, automate_selected
	else:
		print("Veuillez entrer une des options proposées")
	return list_automate, automate_selected


def renameStates(list_automate, automate_selected): # rename all apparitions of a state (can be used to fuse two states)
	print("\n\n\n\n\n\n\n\n")
	dis.displayAEF(list_automate[automate_selected])
	print("\n\n\n\n")
	choix = input("Entrez l'état à renommer ou appuyez sur entrer pour revenir en arrière : ").strip()
	if(choix in list_automate[automate_selected]["Etats"]):
		ancien = choix
		nouveau = input(f"Entrez le nouveau nom à donner à l'état {ancien} ou appuyez sur entrer pour revenir en arrière : ").strip()
		if(nouveau in list_automate[automate_selected]["Etats"]):
			choix = input(f"L'état {nouveau} existe déjà dans l'AEF, êtes vous sûr de vouloir fusionner les états {ancien} et {nouveau} ?\n1 : oui\n2 : non\n\n").strip()
			if(choix != "1"):
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
						print("impossible de fusionner les deux états, car il s'agit des deux seuls états de l'AEF")
						return list_automate, automate_selected
		elif(nouveau == ""):
			return list_automate, automate_selected
		else:
			list_automate[automate_selected]["Etats"][nouveau] = {} # if the state doesn't exist, create it


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
		return list_automate, automate_selected
	else:
		print("Erreur : l'état", ancien, "n'existe pas dans l'AEF")

	return list_automate, automate_selected



def changeStatesInitFinal(list_automate, automate_selected, nbr): # add or delete initials or finals states
	test = 1
	if(nbr == 0):
		etat = "Etats_initiaux"
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
			list_automate[automate_selected][etat].remove(choix)
		elif(choix in list_automate[automate_selected]["Etats"]):
			if(nbr == 0 and len(list_automate[automate_selected]["Etats_initiaux"]) >= 1):
				print("Vous ne pouvez rentrer qu'un état initial")
			else:
				if(nbr == 0):
					if(len(list_automate[automate_selected]["Etats"][choix].keys()) != 0): # check if initial state lead to another state
						list_automate[automate_selected][etat].append(choix)
					else:
						print("Erreur, l'état", choix, "ne peux pas être défini comme état initial car il ne contient aucune transition")
				else:
					if(testTransition(list_automate, automate_selected, choix) != 0):
						list_automate[automate_selected][etat].append(choix)
					else:
						print("Erreur, l'état", choix, "ne peux pas être défini comme état final car aucune transition n'y conduit")
		elif(choix == ""):
			if(0<len(list_automate[automate_selected][etat])):
				test = 0
			else:
				print("Votre AEF doit contenir au moins un état ", nom)
		else:
			print("Erreur, l'état", choix, "n'existe pas dans cet automate")
	print("\n\n")
	return list_automate, automate_selected



def demandDelete(liste_automate, automate_selected): # ask confirmation before deleting the FA
	print("\n\n\n")
	dis.displayAEF(liste_automate[automate_selected])
	choix = input("\n\n\nEtes-vous sûr de vouloir supprimer cet AEF ?\n1 : oui\n2 : non\n\n").strip()
	if(choix == "1"):
		return deleteAutomate(liste_automate, automate_selected)
	else:
		return liste_automate, automate_selected


def deleteAutomate(liste_automate, automate_selected): # delete the FA
	liste_automate.pop(automate_selected)
	automate_selected = -1
	return file.loadAutomate(liste_automate, automate_selected)


