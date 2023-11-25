import json
import re # expression régulière pour tester le nom des fichiers


#automate ={
#    "Etats": {
#        "Etat0": {"Transition1": "Etat1", "Transition2": "Etat0"},
#        "Etat1": {"Transition3": "Etat0", "Transition4": "Etat1"}
#    },
#    "Etats_initiaux": ["Etat0"],
#    "Etats_finaux": ["Etat1"]
#}

def creer_automate_vide():
	return {
		"Etats": {},
		"Etats_initiaux": [],
		"Etats_finaux": [],
		"Nom": ""
	}


def select(liste_automate, automate_selected): # importer, créer, ou séléctionner un AEF existant
	if(automate_selected == -1):
		print("\n\n\n\n\nAEF séléctionné : aucun")
	else:
		print("AEF séléctionné : ", automate_selected+1)
	print("\nséléctionnez un AEF :\n1 : importer depuis un fichier\n2 : créer un nouvel AEF")
	nbr = 3
	for aef in liste_automate: # afficher tous les AEF existant
		print(nbr, ":", aef["Nom"])
		nbr+=1

	test=1
	while(test):
		choix = int(input("\nséléctionnez un AEF : "))
		if(choix == 1):
			liste_automate, automate_selected = openjson(liste_automate, automate_selected)
			test=0
		elif(choix == 2):
			automate_selected = len(liste_automate) # l'indice de l'AEF est la taille de la liste avant de l'ajouter : liste vide = taille de 0 -> le premier AEF sera à l'indice 0
			liste_automate.append(creer_automate_vide())
			liste_automate, automate_selected = saisir_automate(liste_automate, automate_selected)
			test=0
		elif(2 < choix and choix < len(liste_automate)+3):
			automate_selected = choix-3 # on a ajouté deux option dans une liste qui commence à 1 -> l'indice est décalé de 3
			test=0
		else:
			print("Veuillez choisir une des options proposées")
	return liste_automate, automate_selected
			




def openjson(liste_automate, automate_selected):
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
		return select(liste_automate, automate_selected) # si nom de fichier vide, retour au menu précédent

		




def saisir_automate(liste_automate, automate_selected):
	nom = input("\n\nEntrez le nom à donner à l'AEF : ")
	if(nom != ""):
		liste_automate[automate_selected]["Nom"] = nom 
		test=1
		while test:
			print("\nEntrez les états et transitions sous la forme : état, transition, état_suivant")
			transition_input = input("Entrez la nouvelle partie de votre AEF ou appuyez sur Entrée pour terminer : ").split(',')

			if(len(transition_input) == 3 and transition_input[0].strip() != "" and transition_input[1].strip() != "" and transition_input[2].strip() != "" ):
				etat = transition_input[0].strip() # supprimer les espaces
				transition = transition_input[1].strip()
				etat_suivant = transition_input[2].strip()

				if etat not in liste_automate[automate_selected]["Etats"]:
					liste_automate[automate_selected]["Etats"][etat] = {}  # Ajoute les états s'ils ne sont pas présent
				if etat_suivant not in liste_automate[automate_selected]["Etats"]:
					liste_automate[automate_selected]["Etats"][etat_suivant] = {}
				liste_automate[automate_selected]["Etats"][etat][transition] = etat_suivant # Ajoute la transition à l'état

			elif(transition_input == ['']):
				test=0
			else:
				print("votre entrée n'est pas correcte")

		print("\n")
		test=1
		while test:
			etat = input("entrez un état initial (ou appuyez sur entrer pour terminer): ") # demander les états initiaux
			if(etat in liste_automate[automate_selected]["Etats"] and etat not in liste_automate[automate_selected]["Etats_initiaux"]):
				liste_automate[automate_selected]["Etats_initiaux"].append(etat)
			elif(etat == ""):
				if(len(liste_automate[automate_selected]["Etats_initiaux"]) == 0):
					print("Veuillez entrer au moins un état initial")
				else:
					test=0
			else:
				print("votre entrée n'est pas correcte")

		print("\n")
		test=1
		while test:
			etat = input("entrez un état final (ou appuyez sur entrer pour terminer): ") # demander les états initiaux
			if(etat in liste_automate[automate_selected]["Etats"] and etat not in liste_automate[automate_selected]["Etats_finaux"]):
				liste_automate[automate_selected]["Etats_finaux"].append(etat)
			elif(etat == ""):
				if(len(liste_automate[automate_selected]["Etats_finaux"]) == 0):
					print("Veuillez entrer au moins un état final")
				else:	
					test=0
			else:
				print("votre entrée n'est pas correcte")
		return liste_automate, automate_selected
	else:	# si nom de l'aef vide, on réapplique la fonction select()
		suppr(liste_automate, automate_selected) # on supprime l'AEF vide créé dans select()
		return select(liste_automate, automate_selected)


def editAEF(liste_automate, automate_selected): # choisir quelles modifications on veux faire
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

	
def modif_etats(liste_automate, automate_selected): # choisir si l'on veut éditer, renommer ou supprimer des états
	choix = 0
	while(choix != "4"):
		print("\n\n\n\n\n\n\n\n\n\n\n")
		afficher_AEF(liste_automate, automate_selected)
		choix = input("\n\n\nQue voulez vous faire ?\n1 : Ajouter ou supprimer des transitions\n2 : Renommer toutes les occurences d'un état\n3 : Supprimer toutes les occurences d'un état\n4 : Retour\n\n\n").strip()
		if(choix == "1"):
			liste_automate, automate_selected = editer_etats(liste_automate, automate_selected)
		elif(choix == "2"):
			liste_automate, automate_selected = renommer_etats(liste_automate, automate_selected)
		elif(choix == "3"):
			liste_automate, automate_selected = suppr_etat(liste_automate, automate_selected)
		elif(choix != "4"):
			print("Veuillez entrer une des options proposées")
	return liste_automate, automate_selected


def editer_etats(liste_automate, automate_selected): # ajouter ou supprimer des transitions
	test = 1
	while test:
		print("\n\n\n\n\n\n\n\n\n\n\n")
		afficher_AEF(liste_automate, automate_selected)
		print("\nEntrez les états et transitions sous la forme : état, transition, état_suivant.\nUne transition déjà existante sera supprimée, ou ajoutée si elle n'exise pas")
		transition_input = input("Entrez la nouvelle partie de votre AEF ou appuyez sur Entrée pour terminer : ").split(',')
		print(transition_input)
		if(len(transition_input) == 3 and transition_input[0].strip() != "" and transition_input[1].strip() != "" and transition_input[2].strip() != "" ):
			etat = transition_input[0].strip() # supprimer les espaces
			transition = transition_input[1].strip()
			etat_suivant = transition_input[2].strip()
			if etat_suivant not in liste_automate[automate_selected]["Etats"]:# Ajouter les états s'ils ne sont pas présent
				liste_automate[automate_selected]["Etats"][etat_suivant] = {}
			if etat not in liste_automate[automate_selected]["Etats"]: # si l'état n'existe pas, on le créé et on ajoute sa trnasition     ######## PROBLEME ####### si on déclare q0,a,q1 et q2,b,q3 on a 2 AEF différent, et le code ne le détecte pas  ######## PROBLEME #######
				liste_automate[automate_selected]["Etats"][etat] = {}
				liste_automate[automate_selected]["Etats"][etat][transition] = etat_suivant
			elif(transition not in liste_automate[automate_selected]["Etats"][etat]): # si l'état existe mais qu'il n'a pas de transition à ce nom là, on en créé une vers l'état suivant
				liste_automate[automate_selected]["Etats"][etat][transition] = etat_suivant
			elif(liste_automate[automate_selected]["Etats"][etat][transition] == etat_suivant): # l'état existe avec cette transition vers cet état suivant -> on supprime
				del liste_automate[automate_selected]["Etats"][etat][transition]
			else: # l'état existe avec cette transition mais vers un état suivant différent, or on ne peut pas avoir de clé pointant vers deux état différent -> on change l'état suivant
				liste_automate[automate_selected]["Etats"][etat][transition] = etat_suivant
		elif(transition_input == ['']): # si la chaîne saisie est vide
			test = 0
		else: # la saisie est incorrecte
			print("votre entrée n'est pas correcte")
	return liste_automate, automate_selected

				


# def suppr_etat(liste_automate, automate_selected): # supprimer toutes les occurences d'un état


# def renommer_etats(liste_automate, automate_selected): # renommer toutes les occurences d'un état (peut servir à fusionner deux états)


# refaire la fonction saisir_automate() en utilisant les autres fonctions


# modélisation graphique



def changer_etats_ini_fin(liste_automate, automate_selected, nbr): # ajouter ou supprimer des états initiaux ou finaux
	test = 1
	if(nbr == 0):
		etat = "Etats_initiaux"
	elif(nbr == 1):
		etat = "Etats_finaux"
	else:
		print("erreur, le 3e parametre de changer_etats_ini_fin() ne peut être que 0 ou 1")
		exit(1)
	while test:
		print("\n\n\n\n\n\n\n\n\n\n\n")
		afficher_AEF(liste_automate, automate_selected)
		print("\n\n\nEntrez un état déjà présent pour l'effacer, appuyez sur entrer pour sortir")
		choice = input("Entrez l'état que vous voulez ajouter : ").strip()
		if choice in liste_automate[automate_selected][etat]:
			liste_automate[automate_selected][etat].remove(choice)
		elif(choice in liste_automate[automate_selected]["Etats"]):
			liste_automate[automate_selected][etat].append(choice)
		elif(choice == ""):
			if(0<len(liste_automate[automate_selected][etat])):
				test = 0
			else:
				print("Vous ne pouvez pas faire d'AEF avec 0 états", etat[6:])
		else:
			print("Erreur, l'état", choice, "n'existe pas dans cet automate")
	return liste_automate, automate_selected






def alphabet(liste_automate, automate_selected): # calculer l'alphabet
	transitions_liste = []
	for transitions in liste_automate[automate_selected]["Etats"].values():
		transitions_liste.extend(transitions.keys())
	alphabet = list(set(transitions_liste))  # Suppression des doublons
	return alphabet



def demande_suppr(liste_automate, automate_selected): # demande de confirmation avant suppression de l'AEF
	print("\n\n\n")
	afficher_AEF(liste_automate, automate_selected)
	choix = input("\n\n\nEtes-vous sûr de vouloir supprimer cet AEF ?\n1 : oui\n2 : non\n\n").strip()
	if(choix == "1"):
		return suppr(liste_automate, automate_selected)
	else:
		return liste_automate, automate_selected

def suppr(liste_automate, automate_selected): # supprimer l'AEF
	liste_automate.pop(automate_selected)
	automate_selected = -1
	return select(liste_automate, automate_selected)



def sauvegarder_AEF(liste_automate, automate_selected):
	test=1
	while test:
			nom_fichier = input("entrez le nom du fichier : ")
			if(nom_fichier != ""):
				if(test_nom_fichier(nom_fichier)):
					nom_fichier = nom_fichier + ".json"
					with open(nom_fichier, 'w') as file:
						json.dump(liste_automate[automate_selected], file, indent=4)
					test=0
					print(f"AEF sauvegardé dans {nom_fichier}")
				else:
					print("un fichier ne peut pas contenir de caractères spéciaux\n")
			else:
				print("fichier non sauvegardé")



def test_nom_fichier(nom): # vérifier le nom d'un fichier
	motif = r"^[a-zA-Z0-9_\-\.]+$"
	if(re.match(motif, nom)):
		return True # nom conforme
	else:
		return False # non conforme



def afficher_AEF(liste_automate, automate_selected):
	print("Nom :", liste_automate[automate_selected]["Nom"])
	print("Alphabet:", alphabet(liste_automate, automate_selected))
	print("États: {")
	for etat, transitions in liste_automate[automate_selected]["Etats"].items():
		print(f"\t{etat}")
		for transition, etat_suivant in transitions.items():
			print(f"\t   {transition} , {etat_suivant}")
	print("\t}")
	print("États initiaux:", liste_automate[automate_selected]["Etats_initiaux"])
	print("États finaux:", liste_automate[automate_selected]["Etats_finaux"])
