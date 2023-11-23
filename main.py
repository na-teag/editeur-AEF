import json
import re # expression régulière pour tester le nom des fichiers

from fonctions import *


#automate ={
#    "Etats": {
#        "Etat0": {"Transition1": "Etat1", "Transition2": "Etat0"},
#        "Etat1": {"Transition3": "Etat0", "Transition4": "Etat1"}
#    },
#    "Etats_initiaux": ["Etat0"],
#    "Etats_finaux": ["Etat1"]
#}







def afficher_menu():
	print("\n\n\n\n\n\n\n\n")
	print("1 : visualiser l'AEF séléctionné")
	print("2 : éditer l'AEF")
	print("3 : sauvegarder l'AEF")
	print("4 : faire des tests sur l'AEF")
	print("5 : modifier l'AEF selon une propriété")
	print("6 : générer un AEF à partir de celui-ci")
	print("7 : supprimer l'AEF")
	print("8 : quitter le programme")
	print("\n\n\n")

def afficher_menu_test():
	print("\n\n\n\n\n\n\n\n")
	print("1 : tester si un mot est reconnu")
	print("2 : tester si l'AEF est complet")
	print("3 : tester si l'AEF est déterministe")
	print("4 : tester si l'AEF est émondé")
	print("5 : tester si l'AEF est minimal")
	print("6 : tester si cet AEF et un autre sont équivalents")
	print("7 : retour")
	print("\n\n\n")

def afficher_menu_modif():
	print("\n\n\n\n\n\n\n\n")
	print("1 : rendre l'AEF complet")
	print("2 : rendre l'AEF déterministe")
	print("3 : rendre l'AEF émondé")
	print("4  :rendre l'AEF minimal")
	print("5 : retour")
	print("\n\n\n")

def afficher_menu_generer():
	print("\n\n\n\n\n\n\n\n")
	print("1 : générer une expression régulière")
	print("2 : générer l'AEF complément")
	print("3 : générer l'AEF miroir")
	print("4 : générer le produit de cet AEF et d'un autre")
	print("5 : générer la concaténation de cet AEF et d'un autre")
	print("6 : retour")
	print("\n\n\n")

def menu_test():
	while True:
		afficher_menu_test()
		choice = input("Choisissez une action : ")
		choice = choice.strip()
		if(choice == "1"):
			print("non disponible") ###### A FAIRE ######
		elif(choice == "2"):
			print("non disponible") ###### A FAIRE ######
		elif(choice == "3"):
			print("non disponible") ###### A FAIRE ######
		elif(choice == "4"):
			print("non disponible") ###### A FAIRE ######
		elif(choice == "5"):
			print("non disponible") ###### A FAIRE ######
		elif(choice == "6"):
			print("non disponible") ###### A FAIRE ######
		elif(choice == "7"):
			break
		else:
			print("Veuillez entrer l'une des options proposés\n")

def menu_generer():
	while True:
		afficher_menu_generer()
		choice = input("Choisissez une action : ")
		choice = choice.strip()
		if(choice == "1"):
			print("non disponible") ###### A FAIRE ######
		elif(choice == "2"):
			print("non disponible") ###### A FAIRE ######
		elif(choice == "3"):
			print("non disponible") ###### A FAIRE ######
		elif(choice == "4"):
			print("non disponible") ###### A FAIRE ######
		elif(choice == "5"):
			print("non disponible") ###### A FAIRE ######
		elif(choice == "6"):
			break
		else:
			print("Veuillez entrer l'une des options proposés\n")

def menu_modif():
	while True:
		afficher_menu_modif()
		choice = input("Choisissez une action : ")
		choice = choice.strip()
		if(choice == "1"):
			print("non disponible") ###### A FAIRE ######
		elif(choice == "2"):
			print("non disponible") ###### A FAIRE ######
		elif(choice == "3"):
			print("non disponible") ###### A FAIRE ######
		elif(choice == "4"):
			print("non disponible") ###### A FAIRE ######
		elif(choice == "5"):
			break
		else:
			print("Veuillez entrer l'une des options proposés\n")



print("\n\n") 

liste_automate = []
automate_selected=-1
liste_automate, automate_selected = open_or_new(liste_automate, automate_selected) # séléctionner un AEF


if(liste_automate[automate_selected]["Etats"] == {}):
	liste_automate, automate_selected = saisir_automate(liste_automate, automate_selected)



while True:
	afficher_menu()
	choice = input("Choisissez une action : ")
	choice = choice.strip()
	if(choice == "1"):
		afficher_AEF(liste_automate, automate_selected)
	elif(choice == "2"):
		print("non disponible") ###### A FAIRE ######
	elif(choice == "3"):
		while True:
			nom_fichier = input("entrez le nom du fichier : ")
			if(test_nom_fichier(nom_fichier)):
				nom_fichier = nom_fichier + ".json"
				sauvegarder_AEF(liste_automate, automate_selected, nom_fichier)
				break
			else:
				print("un fichier ne peut pas contenir de caractères spéciaux\n")
	elif(choice == "4"):
		menu_test()
	elif(choice == "5"):
		menu_modif()
	elif(choice == "6"):
		menu_generer()
	elif(choice == "7"):
		print("non disponible") ###### A FAIRE ######
	elif(choice == "8"):
		break
	else:
		print("Veuillez entrer l'une des options proposés\n")



