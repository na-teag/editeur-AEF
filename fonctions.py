from fonctions2 import *

#automate ={
#    "Etats": {
#        "Etat0": {"Transition1": ["Etat1"], "Transition2": ["Etat0"]},
#        "Etat1": {"Transition3": ["Etat0"], "Transition4": ["Etat1"]}
#    },
#    "Etats_initiaux": ["Etat0"],
#    "Etats_finaux": ["Etat1"]
#}


    
def openjson(liste_automate, automate_selected): # liste_automate needed, do not remove it
	nom_fichier = input("\nentrez le nom du fichier .json : ")
	print(nom_fichier)
	if(nom_fichier != ""):
		nom_fichier = nom_fichier + ".json"
		try:
			with open(nom_fichier, 'r') as file:
				automate = json.load(file)
				automate_selected = len(liste_automate)
				liste_automate.append(automate)
				print(f"AEF chargé à partir de {nom_fichier}")
		except FileNotFoundError:
			print(f"Le fichier {nom_fichier} n'existe pas. Veuillez vérifier le nom du fichier.")
			liste_automate, automate_selected = openjson(liste_automate, automate_selected) 
		return liste_automate, automate_selected
	else:
		return select(liste_automate, automate_selected) # if the name is empty, back to the last menu



def select(liste_automate, automate_selected): # create, import or select an existing DFA
	if(automate_selected == -1):
		print("\n\n\n\n\nAEF séléctionné : aucun")
	else:
		print("AEF séléctionné : ", automate_selected+1)
	print("\nséléctionnez un AEF :\n1 : importer depuis un fichier\n2 : créer un nouvel AEF")
	nbr = 3
	for aef in liste_automate: # print all DFA's names
		print(nbr, ":", aef["Nom"])
		nbr+=1

	test=1
	while(test):
		test2 = 1
		while test2:
			try:
				choix = int(input("\nSélectionnez un AEF : "))
				test2 = 0
			except ValueError:
				print("Veuillez entrer un nombre")
		if(choix == 1):
			liste_automate, automate_selected = openjson(liste_automate, automate_selected) # open the file, and add the content to the list
			test=0
		elif(choix == 2):
			automate_selected = len(liste_automate) # the index of the DFA is the lenght of the list before it's added to it : empty list -> first DFA atindex 0
			liste_automate.append(creer_automate_vide())
			liste_automate, automate_selected = editer_etats(liste_automate, automate_selected)
			test=0
		elif(2 < choix and choix < len(liste_automate)+3):
			automate_selected = choix-3 # 2 options added in the list begging at 1 -> the index is shifted by 3
			test=0
		else:
			print("Veuillez choisir une des options proposées")
	return liste_automate, automate_selected
			




def editAEF(liste_automate, automate_selected): # choose the modification
	choix = 0
	while(choix != "5"):
		choix = input("\n\nQue souhaitez vous modifier ?\n\n1 : Nom\n2 : Etats et transitions\n3 : Etats initiaux\n4 : Etats finaux\n5 : retour\n\n").strip()
		if(choix == "1"):
			print("Nom actuel :", liste_automate[automate_selected]["Nom"])
			liste_automate[automate_selected]["Nom"] = input("Entrez le nouveau nom : ").strip()
		elif(choix == "2"):
			liste_automate, automate_selected = modif_etats(liste_automate, automate_selected)
		elif(choix == "3"):
			liste_automate, automate_selected = changer_etats_ini_fin(liste_automate, automate_selected, 0)
		elif(choix == "4"):
			liste_automate, automate_selected = changer_etats_ini_fin(liste_automate, automate_selected, 1)
		elif(choix != "5"):
			print("Veuillez entrer une des options proposées")
	return liste_automate, automate_selected

	
def modif_etats(liste_automate, automate_selected): # choose to either edit, rename, or delete states
	choix = 0
	while(choix != "4"):
		print("\n\n\n\n\n\n\n\n\n\n\n")
		afficher_AEF(liste_automate[automate_selected])
		choix = input("\n\n\nQue voulez vous faire ?\n1 : Ajouter ou supprimer des transitions\n2 : Renommer un état\n3 : Supprimer un état\n4 : Retour\n\n\n").strip()
		if(choix == "1"):
			liste_automate, automate_selected = editer_etats(liste_automate, automate_selected)
		elif(choix == "2"):
			liste_automate, automate_selected = renommer_etats(liste_automate, automate_selected)
		elif(choix == "3"):
			liste_automate, automate_selected = suppr_etat(liste_automate, automate_selected)
		elif(choix != "4"):
			print("Veuillez entrer une des options proposées")
	return liste_automate, automate_selected


def editer_etats(liste_automate, automate_selected): # add or delete transition or states
	while(liste_automate[automate_selected]["Nom"] == ""):
		liste_automate[automate_selected]["Nom"] = input("Veuillez donner un nom à l'automate : ")
	test = 1
	while test:
		print("\n\n\n\n\n\n\n\n\n\n\n")
		afficher_AEF(liste_automate[automate_selected])
		print("\nEntrez les états et transitions sous la forme : état, transition, état_suivant.\nUne transition déjà existante sera supprimée, ou ajoutée si elle n'existe pas")
		print("\nCaractères interdits : espace virgule epsilon union étoile plus guillemets")
		transition_input = input("Entrez la nouvelle partie de votre AEF ou appuyez sur Entrer pour terminer : ").split(',') # nom d'état : pas d'espace, de virgule, de plus ou d'étoile, d'union, d'epsilon
		# print(transition_input)
		if(len(transition_input) == 3 and transition_input[0].strip() != "" and transition_input[1].strip() != "" and transition_input[2].strip() != "" and "+" not in transition_input[1].strip() and "*" not in transition_input[1].strip() and "ɛ" not in transition_input[1].strip() and "∪" not in transition_input[1].strip() and " " not in transition_input[1].strip() and " " not in transition_input[0].strip() and " " not in transition_input[2].strip() and "'" not in transition_input[1].strip() and "'" not in transition_input[0].strip() and "'" not in transition_input[2].strip() and '"' not in transition_input[1].strip() and '"' not in transition_input[0].strip() and '"' not in transition_input[2].strip()):
			etat = transition_input[0].strip() # delete space
			transition = transition_input[1].strip()
			etat_suivant = transition_input[2].strip()
			if(etat_suivant not in liste_automate[automate_selected]["Etats"]):# Add state if not already existing
				liste_automate[automate_selected]["Etats"][etat_suivant] = {}
			if(etat not in liste_automate[automate_selected]["Etats"]): # if not existing, it' added with the transition     ######## PROBLEME ####### si on déclare q0,a,q1 et q2,b,q3 on a 2 AEF différent, et le code ne le détecte pas  ######## PROBLEME #######
				liste_automate[automate_selected]["Etats"][etat] = {}
				liste_automate[automate_selected]["Etats"][etat][transition] = []
				liste_automate[automate_selected]["Etats"][etat][transition].append(etat_suivant)
			elif(transition not in liste_automate[automate_selected]["Etats"][etat]): # if the state exist but without this transition, create it
				liste_automate[automate_selected]["Etats"][etat][transition] = []
				liste_automate[automate_selected]["Etats"][etat][transition].append(etat_suivant)
			elif(etat_suivant in liste_automate[automate_selected]["Etats"][etat][transition]): # if the state already exist with this transition, it's deleted
				liste_automate[automate_selected]["Etats"][etat][transition].remove(etat_suivant)

			else: # the state exist with this transition but leading to another state, so we add the next state to the list
				liste_automate[automate_selected]["Etats"][etat][transition].append(etat_suivant)

			liste = []
			for etat in liste_automate[automate_selected]["Etats"]:
				if(liste_automate[automate_selected]["Etats"][etat] == {}): # if the state doesn't have any transition leading or beginning from it, it's deleted because it's not related tho the DFA anymore
					if(test_transition_entrante(liste_automate, automate_selected, etat) == 0): # testing if the state has transition leading to it
						liste.append(etat)
			if(len(liste) != 0):
				for etat in liste:
					del liste_automate[automate_selected]["Etats"][etat]
				if(liste_automate[automate_selected]["Etats"] == {}): # if all the states have been deleted, ask to enter a new DFA
					print("\n\n\n\n\n\n\n\n\n\n\n\n\nVous ne pouvez pas manipuler un AEF vide, merci d'en réenregistrer un :")
					liste_automate[automate_selected]["Etats_initiaux"] = []
					liste_automate[automate_selected]["Etats_finaux"] = []
					return editer_etats(liste_automate, automate_selected)
				if(set(liste_automate[automate_selected]["Etats_initiaux"]) <= set(liste)): # if all the initials state have been deleted, ask for new one
					print("\n\n\n\n\n Il n'y a aucun état initial, veuillez en entrez un ")
					liste_automate[automate_selected]["Etats_initiaux"] = []
					liste_automate, automate_selected = changer_etats_ini_fin(liste_automate, automate_selected, 0)
				if(set(liste_automate[automate_selected]["Etats_finaux"]) <= set(liste)): # same for fianl states
					print("\n\n\n\n\n Il n'y a aucun état final, veuillez en entrez un nouveau")
					liste_automate[automate_selected]["Etats_finaux"] = []
					liste_automate, automate_selected = changer_etats_ini_fin(liste_automate, automate_selected, 1)


		elif(transition_input == ['']): # if the answer is empty
			if(len(liste_automate[automate_selected]["Etats"].keys()) >= 1):
				if(len(liste_automate[automate_selected]["Etats_initiaux"]) < 1):
					liste_automate, automate_selected = changer_etats_ini_fin(liste_automate, automate_selected, 0)
				if(len(liste_automate[automate_selected]["Etats_finaux"]) < 1):
					liste_automate, automate_selected = changer_etats_ini_fin(liste_automate, automate_selected, 1)
				test = 0
			else:
				print("Veuillez entrer au moins une transition entre deux états")

		else: # the answer is incorrect
			print("votre entrée n'est pas correcte")
	return liste_automate, automate_selected



def test_transition_entrante(liste_automate, automate_selected, etat2): # testing if a state has transition leading to it
	for etat in liste_automate[automate_selected]["Etats"]:
		for transition in liste_automate[automate_selected]["Etats"][etat].keys():
			for liste_etats_suivants in liste_automate[automate_selected]["Etats"][etat][transition]:
				if(etat2 in liste_etats_suivants):
					return 1
	return 0





def suppr_etat(liste_automate, automate_selected): # delete all apparition of a state
	print("\n\n\n\n\n\n\n\n")
	afficher_AEF(liste_automate[automate_selected])
	print("\n\n\n\n")
	choix = input("Entrez l'état à supprimer ou appuyez sur entrer pour revenir en arrière : ").strip()
	if(choix in liste_automate[automate_selected]["Etats"]):
		choix2 = input(f"Etes-vous sûr de vouloir supprimer l'état {choix} ? Cette action est irréversible\n1 : oui\n2 : non\n\n\n").strip()
		if(choix2 == "1"):
			dico = {}
			del liste_automate[automate_selected]["Etats"][choix]
			for etat, transition in liste_automate[automate_selected]["Etats"].items():
				for etat_suivant in transition.values():
					if(choix in etat_suivant):
						etat_suivant.remove(choix)
				
				for trans in transition.keys():
					if(liste_automate[automate_selected]["Etats"][etat][trans] == []): # after deleting the state, if there is transition starting from it, they are added to a list to be deleted (cannot do it when the loop is on these same transitions)
						dico[etat] = trans
			for etat in dico:
				del liste_automate[automate_selected]["Etats"][etat][dico[etat]]
			if(choix in liste_automate[automate_selected]["Etats_initiaux"]): # if the state is in the liste, it's deleted
				liste_automate[automate_selected]["Etats_initiaux"].remove(choix)
			if(choix in liste_automate[automate_selected]["Etats_finaux"]):
				liste_automate[automate_selected]["Etats_finaux"].remove(choix)

			liste = []
			for etat in liste_automate[automate_selected]["Etats"]:
				if(liste_automate[automate_selected]["Etats"][etat] == {}): # if a state isn't anywhere in the DFA, it's deleted
					if(test_transition_entrante(liste_automate, automate_selected, etat) == 0):
						liste.append(etat)
			if(len(liste) != 0):
				print(liste)
				for etat in liste:
					del liste_automate[automate_selected]["Etats"][etat] 
					if(etat in liste_automate[automate_selected]["Etats_initiaux"]): # if the deleted states are in the initals or finals states, they are deleted too
						liste_automate[automate_selected]["Etats_initiaux"].remove(etat)
					if(etat in liste_automate[automate_selected]["Etats_finaux"]):
						liste_automate[automate_selected]["Etats_finaux"].remove(etat)
				
			if(len(liste_automate[automate_selected]["Etats"]) <= 1): # if all the states have been removed, enter a new DFA
				print("\n\n\n\n\n\n\n\n\n\n\n\n\n\nVous ne pouvez pas manipuler un AEF vide, veuillez en entrer un nouveau :")
				return editer_etats(liste_automate, automate_selected)
			if(len(liste_automate[automate_selected]["Etats_initiaux"]) == 0):
				print("\n\n\n\n\n\n\n\n\n\n\nVous avez supprimé le seul état initial, veuillez en entrer un nouveau")
				liste_automate, automate_selected = changer_etats_ini_fin(liste_automate, automate_selected, 0)
			if(len(liste_automate[automate_selected]["Etats_finaux"]) == 0):
				print("\n\n\n\n\n\n\n\n\n\n\nVous avez supprimé le seul état final, veuillez en entrer un nouveau")
				liste_automate, automate_selected = changer_etats_ini_fin(liste_automate, automate_selected, 1)
		else:
			print("action annulée")
	elif(choix == ""):
		return liste_automate, automate_selected
	else:
		print("Veuillez entrer une des options proposées")
	return liste_automate, automate_selected





def renommer_etats(liste_automate, automate_selected): # rename all apparitions of a state (can be used to fuse two states)
	print("\n\n\n\n\n\n\n\n")
	afficher_AEF(liste_automate[automate_selected])
	print("\n\n\n\n")
	choix = input("Entrez l'état à renommer ou appuyez sur entrer pour revenir en arrière : ").strip()
	if(choix in liste_automate[automate_selected]["Etats"]):
		ancien = choix
		nouveau = input(f"Entrez le nouveau nom à donner à l'état {ancien} ou appuyez sur entrer pour revenir en arrière : ").strip()
		if(nouveau in liste_automate[automate_selected]["Etats"]):
			choix = input(f"L'état {nouveau} existe déjà dans l'AEF, êtes vous sûr de vouloir fusionner les états {ancien} et {nouveau} ?\n1 : oui\n2 : non\n\n").strip()
			if(choix != "1"):
				return liste_automate, automate_selected
			else:
				if(len(liste_automate[automate_selected]["Etats"]) < 3):
					test = 0
					for transition in liste_automate[automate_selected]["Etats"][ancien].keys():
						if(nouveau in liste_automate[automate_selected]["Etats"][ancien][transition]):
							test = 1
					for transition in liste_automate[automate_selected]["Etats"][nouveau].keys():
						if(ancien in liste_automate[automate_selected]["Etats"][nouveau][transition]):
							test = 1
					if(not(len(liste_automate[automate_selected]["Etats"]) == 2 and test)): # if the result is a state with a transition on itself, it's ok
						print("impossible de fusionner les deux états, car il s'agit des deux seuls états de l'AEF")
						return liste_automate, automate_selected
		elif(nouveau == ""):
			return liste_automate, automate_selected
		else:
			liste_automate[automate_selected]["Etats"][nouveau] = {} # if the state doesn't exist, create it


		for transition, liste_etats_suivants in liste_automate[automate_selected]["Etats"][ancien].items(): # duplicate all the transition to the new state
			if(transition not in liste_automate[automate_selected]["Etats"][nouveau].keys()):
				liste_automate[automate_selected]["Etats"][nouveau][transition] = []
			for transition2 in liste_etats_suivants:
				liste_automate[automate_selected]["Etats"][nouveau][transition].append(transition2)
			list(set(liste_automate[automate_selected]["Etats"][nouveau][transition]))
		for etat in liste_automate[automate_selected]["Etats"]:
			if(etat != ancien):
				for transition, liste_etats_suivants in liste_automate[automate_selected]["Etats"][etat].items(): # change all the transition leading to this state
					if(ancien in liste_automate[automate_selected]["Etats"][etat][transition]):
						liste_automate[automate_selected]["Etats"][etat][transition].remove(ancien)
						if(nouveau not in liste_automate[automate_selected]["Etats"][etat][transition]):
							liste_automate[automate_selected]["Etats"][etat][transition].append(nouveau)
		del liste_automate[automate_selected]["Etats"][ancien] # after all the transitions have been removed, the state is deleted

		if(ancien in liste_automate[automate_selected]["Etats_initiaux"]): # if the former state is in the list of initials or finales states, rename them too
			liste_automate[automate_selected]["Etats_initiaux"].remove(ancien)
			liste_automate[automate_selected]["Etats_initiaux"].append(nouveau)
		if(ancien in liste_automate[automate_selected]["Etats_finaux"]):
			liste_automate[automate_selected]["Etats_finaux"].remove(ancien)
			liste_automate[automate_selected]["Etats_finaux"].append(nouveau)

	elif(choix == ""):
		return liste_automate, automate_selected
	else:
		print("Erreur : l'état", ancien, "n'existe pas dans l'AEF")

	return liste_automate, automate_selected






def changer_etats_ini_fin(liste_automate, automate_selected, nbr): # add or delete initials or finals states
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
		afficher_AEF(liste_automate[automate_selected])
		print("\n\n\nEntrez un état", nom, "déjà présent pour l'effacer, appuyez sur entrer pour sortir")
		choix = input(f"Entrez l'état {nom} que vous voulez ajouter : ").strip()
		if choix in liste_automate[automate_selected][etat]:
			liste_automate[automate_selected][etat].remove(choix)
		elif(choix in liste_automate[automate_selected]["Etats"]):
			if(nbr == 0 and len(liste_automate[automate_selected]["Etats_initiaux"]) >= 1):
				print("Vous ne pouvez rentrer qu'un état initial")
			else:
				liste_automate[automate_selected][etat].append(choix)
		elif(choix == ""):
			if(0<len(liste_automate[automate_selected][etat])):
				test = 0
			else:
				print("Votre AEF doit contenir au moins un état ", nom)
		else:
			print("Erreur, l'état", choix, "n'existe pas dans cet automate")
	print("\n\n")
	return liste_automate, automate_selected






def demande_suppr(liste_automate, automate_selected): # ask confirmation before deleting the DFA
	print("\n\n\n")
	afficher_AEF(liste_automate[automate_selected])
	choix = input("\n\n\nEtes-vous sûr de vouloir supprimer cet AEF ?\n1 : oui\n2 : non\n\n").strip()
	if(choix == "1"):
		return suppr(liste_automate, automate_selected)
	else:
		return liste_automate, automate_selected


def suppr(liste_automate, automate_selected): # delete the DFA
	liste_automate.pop(automate_selected)
	automate_selected = -1
	return select(liste_automate, automate_selected)





