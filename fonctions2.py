import json
import re  # regex to test files names


def creer_automate_vide():
	return {
		"Etats": {},
		"Etats_initiaux": [],
		"Etats_finaux": [],
		"Nom": ""
	}



def alphabet(automate): # calculate the alphabet
	transitions_liste = []
	for transitions in automate["Etats"].values():
		transitions_liste.extend(transitions.keys())
	alphabet = list(set(transitions_liste))  # deleting doubles
	return alphabet


def sauvegarder_AEF(automate):
	test=1
	while test:
			nom_fichier = input("entrez le nom du fichier : ")
			if(nom_fichier != ""):
				if(test_nom_fichier(nom_fichier)):
					nom_fichier = nom_fichier + ".json"
					with open(nom_fichier, 'w') as file:
						json.dump(automate, file, indent=4)
					test=0
					print(f"AEF sauvegardé dans {nom_fichier}")
				else:
					print("un fichier ne peut pas contenir de caractères spéciaux\n")
			else:
				print("fichier non sauvegardé")



def test_nom_fichier(nom): # check the file name
	motif = r"^[a-zA-Z0-9_\-\.]+$"
	if(re.match(motif, nom)):
		return True # nom conforme
	else:
		return False # non conforme



def afficher_AEF(automate):
	print("Nom :", automate["Nom"])
	print("Alphabet:", alphabet(automate))
	print("États: {")
	for etat, transitions in automate["Etats"].items():
		print(f"\t{etat}")
		for transition, etat_suivant in transitions.items():
			print(f"\t   {transition} , {etat_suivant}")
	print("\t}")
	print("États initiaux:", automate["Etats_initiaux"])
	print("États finaux:", automate["Etats_finaux"])