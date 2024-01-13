# This file contains all functions for loading and saving an automate in/of a file

import data.structure as strct
import editing.modif as md
import json
import re  # regex to test files names
import glob # to list available files
import os


def loadAutomate(list_automate, automate_selected): # function to create, import or select an existing FA
	if(automate_selected > -1 and list_automate[automate_selected] == strct.createAutomate()):
		list_automate, automate_selected = md.deleteAutomate(list_automate, automate_selected) # in case we created a new one and exited the creat function
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
				print("\n\n\n\nVeuillez entrer un nombre")
		if(choix == 1):
			print("\033[2J") # clear the screen
			list_automate, automate_selected = openjson(list_automate, automate_selected) # open the file, and add the content to the list
			test=0
		elif(choix == 2):
			automate_selected = len(list_automate) # the index of the FA is the lenght of the list before it's added to it : empty list -> first FA at index 0
			list_automate.append(strct.createAutomate())
			print("\033[2J") # clear the screen
			list_automate, automate_selected = md.editStates(list_automate, automate_selected)
			test=0
			print("\033[2J") # clear the screen
		elif(2 < choix and choix < len(list_automate)+3):
			automate_selected = choix-3 # 2 options added in the list begging at 1 -> the index is shifted by 3
			test=0
			print("\033[2J") # clear the screen
		else:
			print("\n\nVeuillez choisir une des options proposées")
	return list_automate, automate_selected
			


def openjson(list_automate, automate_selected): # list_automate needed, do not remove it

	print("\n\n\n\nFichiers json disponibles :\n")
	path = "../file/"
	chemin = os.path.abspath(path) # change the relative path in absolute path
	if not os.path.exists(chemin):
		path = "file/" # for unknown reason the path must sometimes be this one to work
		chemin = os.path.abspath(path) # change the relative path in absolute path
		if not os.path.exists(chemin):
			print("\033[2J") # clear the screen
			print("Aucun fichier json n'a été trouvé dans le dossier \"file\"")
			print("\n\n\n\n\n\n\n\n\n\n\n")
			return loadAutomate(list_automate, automate_selected)
	fichiers = os.listdir(chemin) # get the json files
	fichiers_json = []
	for fichier in fichiers:
		if(fichier[-5:] == ".json"):
			fichiers_json.append(fichier)
	if(len(fichiers_json) == 0): # if there is no file
		print("\033[2J") # clear the screen
		print("Aucun fichier json n'a été trouvé dans le dossier \"file\"")
		print("\n\n\n\n\n\n\n\n\n\n\n")
		return loadAutomate(list_automate, automate_selected) # if there isn't any FA, back to the last menu
	for fichier in fichiers_json:
		index = fichier.rfind('/') # find the last /
		if(index != -1): # check if there is one
			index += 1
			fichier = fichier[index:] # delete the path before print it
		index = fichier.rfind('\\') # find the last \
		if(index != -1): # check if there is one
			index += 1
			fichier = fichier[index:] # delete the path before print it
		print(fichier[:-5], end='\t\t')
	print("\n\n")
	nom_fichier = input("\nentrez le nom du fichier .json : ")
	# print(nom_fichier)
	if(nom_fichier != ""):
		if(not test_nom_fichier(nom_fichier)):
			print("\033[2J") # clear the screen
			print("un fichier ne peut pas contenir de caractères spéciaux\n")
			print("\n\n\n\n\n\n\n\n\n\n\n")
			return openjson(list_automate, automate_selected)
		path_file = path + nom_fichier + ".json"
		try:
			with open(path_file, 'r') as file:
				automate = json.load(file)
				automate_selected = len(list_automate)
				list_automate.append(automate)
				print("\033[2J") # clear the screen
				print(f"AEF chargé à partir de {nom_fichier}.json")
				print("\n\n\n\n\n\n\n\n\n\n\n")
		except FileNotFoundError:
			print("\033[2J") # clear the screen
			print(f"Le fichier {nom_fichier}.json n'existe pas dans le dossier \"file\". Veuillez vérifier le nom du fichier.")
			list_automate, automate_selected = openjson(list_automate, automate_selected) 
		return list_automate, automate_selected
	else:
		print("\033[2J") # clear the screen
		return loadAutomate(list_automate, automate_selected) # if the name is empty, back to the last menu





def test_nom_fichier(nom): # check the file name
	motif = r"^[a-zA-Z0-9_\.]+$"
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
				path = "../file/"
				chemin = os.path.abspath(path) # change the relative path in absolute path
				if not os.path.exists(chemin):
					path = "file/" # for unknown reason the path must sometimes be this one to work
					chemin = os.path.abspath(path) # change the relative path in absolute path
					if not os.path.exists(chemin):
						print("\033[2J") # clear the screen
						print("Erreur : impossible d'accéder au dossier \"file\"")
						print("\n\n\n\n\n\n\n\n\n\n\n")
						return 1
				path_file = path + nom_fichier + ".json"
				chemin = os.path.abspath(path_file)
				with open(chemin, 'w') as file:
					json.dump(automate, file, indent=4)
				test=0
				print("\033[2J") # clear the screen
				print(f"AEF sauvegardé dans le dossier \"file\" en tant que {nom_fichier}.json")
				print("\n\n\n\n\n\n\n\n\n\n\n")
			else:
				print("\033[2J") # clear the screen
				print("un fichier ne peut pas contenir de caractères spéciaux\n")
		else:
			print("\033[2J") # clear the screen
			print("fichier non sauvegardé")
			print("\n\n\n\n\n\n\n\n\n\n\n")
			test=0


