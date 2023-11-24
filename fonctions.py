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


def select(liste_automate, automate_selected):
	if(automate_selected == -1):
		print("\n\n\n\n\nAEF séléctionné : aucun")
	else:
		print("AEF séléctionné : ", automate_selected+1)
	print("\nséléctionnez un AEF :\n1 : importer depuis un fichier\n2 : créer un nouvel AEF")
	nbr = 3
	for aef in liste_automate:
		print(nbr, ":", aef["Nom"])
		nbr+=1

	test=1
	while(test):
		choice = int(input("\nséléctionnez un AEF : "))
		if(choice == 1):
			liste_automate, automate_selected = openjson(liste_automate, automate_selected)
			test=0
		elif(choice == 2):
			automate_selected = len(liste_automate) # l'indice de l'AEF est la taille de la liste avant de l'ajouter : liste vide = taille de 0 -> le premier AEF sera à l'indice 0
			liste_automate.append(creer_automate_vide())
			liste_automate, automate_selected = saisir_automate(liste_automate, automate_selected)
			test=0
		elif(2 < choice and choice < len(liste_automate)+3):
			automate_selected = choice-3 # on a ajouté deux option dans une liste qui commence à 1 -> l'indice est décalé de 3
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



def alphabet(liste_automate, automate_selected):
	transitions_liste = []
	for transitions in liste_automate[automate_selected]["Etats"].values():
		transitions_liste.extend(transitions.keys())
	alphabet = list(set(transitions_liste))  # Suppression des doublons
	return alphabet



def demande_suppr(liste_automate, automate_selected):
	print("\n\n\n")
	afficher_AEF(liste_automate, automate_selected)
	choice = input("\n\n\nEtes-vous sûr de vouloir supprimer cet AEF ?\n1 : oui\n2 : non\n\n")
	if(choice == "1"):
		return suppr(liste_automate, automate_selected)
	else:
		return liste_automate, automate_selected

def suppr(liste_automate, automate_selected):
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

def test_nom_fichier(nom):
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
