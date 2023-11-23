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
		"Etats_finaux": []
	}


def open_or_new(liste_automate, automate_selected):
	while True:
		choice = input("Voulez vous :\n1 : importer un automate d'état fini (AEF)\n2 : en créer un nouveau ?\n\n")
		choice = choice.strip()
		if(choice == "1" or choice == "2"):
			choice = int(choice)
			break
		else:
			print("\nVeuillez entrez une des options proposée")
	if(choice == 1):
		nom_fichier = input("\nentrez le nom du fichier .json : ")
		nom_fichier = nom_fichier + ".json"
		try:
			with open(nom_fichier, 'r') as file:
				automate = json.load(file)
				liste_automate.append(automate)
				print(f"AEF chargé à partir de {nom_fichier}")
		except FileNotFoundError:
			print(f"Le fichier {nom_fichier} n'existe pas. Veuillez vérifier le nom du fichier.")
			open_or_new(liste_automate, automate_selected)
	else:
		automate_selected = len(liste_automate)
		liste_automate.append(creer_automate_vide())
	return liste_automate, automate_selected




def saisir_automate(liste_automate, automate_selected):
	print("\n\nEntrez les états et transitions (état, transition, état_suivant): ")
	
	while True:
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
			break
		else:
			print("votre entrée n'est pas correcte")

	print("\n")

	while True:
		etat = input("entrez un état initial (ou appuyez sur entrer pour terminer): ") # demander les états initiaux
		if(etat in liste_automate[automate_selected]["Etats"] and etat not in liste_automate[automate_selected]["Etats_initiaux"]):
			liste_automate[automate_selected]["Etats_initiaux"].append(etat)
		elif(etat == ""):
			if(len(liste_automate[automate_selected]["Etats_initiaux"]) == 0):
				print("Veuillez entrer au moins un état initial")
			else:
				break
		else:
			print("votre entrée n'est pas correcte")

	print("\n")

	while True:
		etat = input("entrez un état final (ou appuyez sur entrer pour terminer): ") # demander les états initiaux
		if(etat in liste_automate[automate_selected]["Etats"] and etat not in liste_automate[automate_selected]["Etats_finaux"]):
			liste_automate[automate_selected]["Etats_finaux"].append(etat)
		elif(etat == ""):
			if(len(liste_automate[automate_selected]["Etats_finaux"]) == 0):
				print("Veuillez entrer au moins un état final")
			else:	
				break
		else:
			print("votre entrée n'est pas correcte")
	return liste_automate, automate_selected



def alphabet(liste_automate, automate_selected):
	transitions_liste = []
	for transitions in liste_automate[automate_selected]["Etats"].values():
		transitions_liste.extend(transitions.keys())
	alphabet = list(set(transitions_liste))  # Suppression des doublons
	return alphabet



def sauvegarder_AEF(liste_automate, automate_selected, fichier):	
	with open(fichier, 'w') as file:
		json.dump(liste_automate[automate_selected], file, indent=4)
	print(f"AEF sauvegardé dans {fichier}")

def test_nom_fichier(nom):
	motif = r"^[a-zA-Z0-9_\-\.]+$"
	if(re.match(motif, nom)):
		return True # nom conforme
	else:
		return False # non conforme

def afficher_AEF(liste_automate, automate_selected):
	print("Alphabet:", alphabet(liste_automate, automate_selected))
	print("États:", liste_automate[automate_selected]["Etats"])
	print("États initiaux:", liste_automate[automate_selected]["Etats_initiaux"])
	print("États finaux:", liste_automate[automate_selected]["Etats_finaux"])
