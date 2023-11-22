import json


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


def open_or_new():
	while True:
		choice = input("Voulez vous importer un automate (1) en éditer un (2) ou en créer un nouveau (3) ?\n")
		choice.strip()
		if(choice == "1" or choice == "2" or choice == "3"):
			choice = int(choice)
			break
		else:
			print("Veuillez entrez une des options proposée")
	if(choice == 1):
		nom_fichier = input("entrez le nom du fichier : ")
		try:
			with open(nom_fichier, 'r') as file:
				automate = json.load(file)
				liste_automate.append(automate)
				print(f"Automate chargé à partir de {nom_fichier}")
		except FileNotFoundError:
			print(f"Le fichier {nom_fichier} n'existe pas. Veuillez vérifier le nom du fichier.")
			open_or_new()
	elif(choice == 2):
		if(len(liste_automate) == 0):
			print("aucun automate créé")
			open_or_new()
		else:
			print("séléctionner l'automate à éditer (non disponible)")
			open_or_new()
	else:
		automate_selected = len(liste_automate)
		liste_automate.append(creer_automate_vide())
		return automate_selected
	return -1




def saisir_automate(automate_selected):
	print("Entrez les états et transitions (état, transition, état_suivant): ")
	
	while True:
		transition_input = input("Entrez la nouvelle partie de votre automate ou appuyez sur Entrée pour terminer : ").split(',')
		
		if len(transition_input) == 3:
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
			print(transition_input)
			print("votre entrée n'est pas correcte")

	print("\n")

	while True:
		etat = input("entrez un état initial (appuyez sur entrer pour terminer): ") # demander les états initiaux
		if(etat in liste_automate[automate_selected]["Etats"] and etat not in liste_automate[automate_selected]["Etats_initiaux"]):
			liste_automate[automate_selected]["Etats_initiaux"].append(etat)
		elif(etat == ""):
			if(len(liste_automate[automate_selected]["Etats_initiaux"]) == 0):
				print("Veuillez entrer au moins un état initial")
			else:
				break
		else:
			print(etat)
			print("votre entrée n'est pas correcte")

	print("\n")

	while True:
		etat = input("entrez un état final (appuyez sur entrer pour terminer): ") # demander les états initiaux
		if(etat in liste_automate[automate_selected]["Etats"] and etat not in liste_automate[automate_selected]["Etats_finaux"]):
			liste_automate[automate_selected]["Etats_finaux"].append(etat)
		elif(etat == ""):
			if(len(liste_automate[automate_selected]["Etats_finaux"]) == 0):
				print("Veuillez entrer au moins un état final")
			else:	
				break
		else:
			print(etat)
			print("votre entrée n'est pas correcte")



def alphabet(selection):
	transitions_liste = []
	for transitions in liste_automate[selection]["Etats"].values():
		transitions_liste.extend(transitions.keys())
	alphabet = list(set(transitions_liste))  # Suppression des doublons
	return alphabet



def sauvegarder_AEF(selection, fichier):	
	with open(fichier, 'w') as file:
		json.dump(liste_automate[selection], file, indent=4)
	print(f"AEF sauvegardé dans {fichier}")


def afficher_AEF(selection):
	print("Alphabet:", alphabet(selection))
	print("États:", liste_automate[selection]["Etats"])
	print("États initiaux:", liste_automate[selection]["Etats_initiaux"])
	print("États finaux:", liste_automate[selection]["Etats_finaux"])


print("\n\n")

liste_automate = []
automate_selected=-1

if(automate_selected == -1):
	automate_selected = open_or_new()

if(liste_automate[automate_selected]["Etats"] == {}):
	saisir_automate(automate_selected)



print("\n\n")
print(liste_automate[automate_selected])
print("\n\n")
print(afficher_AEF(automate_selected))
print("\n\n")
sauvegarder_AEF(automate_selected, "test.json")