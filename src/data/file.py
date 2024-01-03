# This file contains all functions for loading and saving an automate in/of a file

import data.structure as strct
import editing.modif as md
import json
import re  # regex to test files names
import glob

def loadAutomate(list_automate, automate_selected): # function to create, import or select an existing FA
	nbr = 3 # nbr of additional option other than existing FA
	if(automate_selected == -1):
		print("\n\n\n\n\nAEF séléctionné : aucun")
	else:
		print("AEF séléctionné : ", automate_selected+nbr)
	print("\nséléctionnez un AEF :\n1 : importer depuis un fichier\n2 : créer un nouvel AEF")
	for aef in list_automate: # print all FA's names
		print(nbr, ":", aef["Nom"])
		nbr+=1

	test=1
	while(test):
		test2 = 1
		while test2:
			try:
				choix = int(input("\nSélectionnez un AEF : ").strip())
				test2 = 0
			except ValueError:
				print("Veuillez entrer un nombre")
		if(choix == 1):
			list_automate, automate_selected = openjson(list_automate, automate_selected) # open the file, and add the content to the list
			test=0
		elif(choix == 2):
			automate_selected = len(list_automate) # the index of the FA is the lenght of the list before it's added to it : empty list -> first FA at index 0
			list_automate.append(strct.createAutomate())
			list_automate, automate_selected = md.editStates(list_automate, automate_selected)
			test=0
		elif(2 < choix and choix < len(list_automate)+3):
			automate_selected = choix-3 # 2 options added in the list begging at 1 -> the index is shifted by 3
			test=0
		else:
			print("Veuillez choisir une des options proposées")
	return list_automate, automate_selected
			


def openjson(list_automate, automate_selected): # list_automate needed, do not remove it
	print("Fichiers disponibles : ")
	fichiers_json = glob.glob('../file/' + "*.json")
	for fichier in fichiers_json:
		fichier = fichier.rsplit('/', 1)[-1]
		print(fichier, end='\t\t')
	print("\n")
	nom_fichier = input("\nentrez le nom du fichier .json : ")
	# print(nom_fichier)
	if(nom_fichier != ""):
		nom_fichier = nom_fichier + ".json"
		nom_fichier2 = "../file/" + nom_fichier
		try:
			with open(nom_fichier2, 'r') as file:
				automate = json.load(file)
				automate_selected = len(list_automate)
				list_automate.append(automate)
				print(f"AEF chargé à partir de {nom_fichier} depuis le dossier \"file\"")
		except FileNotFoundError:
			print(f"Le fichier {nom_fichier} n'existe pas dans le dossier \"file\". Veuillez vérifier le nom du fichier.")
			list_automate, automate_selected = openjson(list_automate, automate_selected) 
		return list_automate, automate_selected
	else:
		return loadAutomate(list_automate, automate_selected) # if the name is empty, back to the last menu





def test_nom_fichier(nom): # check the file name
	motif = r"^[a-zA-Z0-9_\-\.]+$"
	if(re.match(motif, nom)):
		return True # nom conforme
	else:
		return False # non conforme



def saveAEF(automate):
	test=1
	while test:
			nom_fichier = input("entrez le nom du fichier : ")
			if(nom_fichier != ""):
				if(test_nom_fichier(nom_fichier)):
					nom_fichier = nom_fichier + ".json"
					nom_fichier2 = "../file/" + nom_fichier
					with open(nom_fichier2, 'w') as file:
						json.dump(automate, file, indent=4)
					test=0
					print(f"AEF sauvegardé dans le dossier \"file\" en tant que {nom_fichier}")
				else:
					print("un fichier ne peut pas contenir de caractères spéciaux\n")
			else:
				print("fichier non sauvegardé")


