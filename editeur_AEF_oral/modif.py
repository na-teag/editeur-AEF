# This file contains all functions to edit an automate
import display as dis
import structure as strct
import re



def verif(val):
    return bool(re.match(r'^[0-9a-bA-B]+$', val)) # letters, numbers, underscore or -





def editStates(list_automate, automate_selected): # add or delete transition or states

	if(list_automate[automate_selected]["Nom"] == ""):
		list_automate[automate_selected]["Nom"] = input("Veuillez donner un nom à l'automate : ")
	if(list_automate[automate_selected]["Nom"] == ""):
		return strct.loadAutomate(list_automate, automate_selected)
	test = 1
	while test:
		print("\n\n\n\n\n\n\n\n\n")
		dis.displayAEF(list_automate[automate_selected])
		print("\nEntrez les états et transitions sous la forme : état, transition, état_suivant.\nUne transition déjà existante sera supprimée, ou ajoutée si elle n'existe pas")
		print("\nCaractères autorisés : lettres et chiffres (restrictions dûes au rendu graphique)")
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
				if(len(list_automate[automate_selected]["Etats_initiaux"]) == 0):
					print("\033[2J") # clear the screen
					list_automate, automate_selected = changeStatesInitFinal(list_automate, automate_selected, 0)
				if(len(list_automate[automate_selected]["Etats_finaux"]) == 0):
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




def demandDelete(list_automate, automate_selected): # ask confirmation before deleting the FA
	print("\033[2J") # clear the screen
	dis.displayAEF(list_automate[automate_selected])
	choix = input("\n\n\nEtes-vous sûr de vouloir supprimer cet AEF ?\n1 : oui\n2 : non\n\n").strip()
	if(choix == "1"):
		print("\033[2J") # clear the screen
		return deleteAutomate(list_automate, automate_selected)
	else:
		print("\033[2J") # clear the screen
		return list_automate, automate_selected




def deleteAutomate(list_automate, automate_selected): # delete the FA
	list_automate.pop(automate_selected)
	automate_selected = -1
	return strct.loadAutomate(list_automate, automate_selected)
