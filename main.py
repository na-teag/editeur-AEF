import json
import re # expression régulière pour tester le nom des fichiers

from fonctions import *
from verifcomplet import *


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
	print("1 : séléctionner un AEF")
	print("2 : visualiser l'AEF séléctionné")
	print("3 : éditer l'AEF")
	print("4 : sauvegarder l'AEF")
	print("5 : faire des tests sur l'AEF")
	print("6 : modifier l'AEF selon une propriété")
	print("7 : générer un AEF à partir de celui-ci")
	print("8 : supprimer l'AEF")
	print("9 : quitter le programme")
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
	test=1
	while test:
		afficher_menu_test()
		choice = input("Choisissez une action : ")
		choice = choice.strip()
		if(choice == "1"):
			print("non disponible") ###### A FAIRE ######
		elif(choice == "2"):
			est_complet(liste_automate[automate_selected])
		elif(choice == "3"):
			print("non disponible") ###### A FAIRE ######
		elif(choice == "4"):
			print("non disponible") ###### A FAIRE ######
		elif(choice == "5"):
			print("non disponible") ###### A FAIRE ######
		elif(choice == "6"):
			print("non disponible") ###### A FAIRE ######
		elif(choice == "7"):
			test=0
		else:
			print("Veuillez entrer l'une des options proposées\n")

def menu_generer():
	test=1
	while test:
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
			test=0
		else:
			print("Veuillez entrer l'une des options proposées\n")

def menu_modif():
	test=1
	while test:
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
			test=0
		else:
			print("Veuillez entrer l'une des options proposées\n")



print("\n\n") 

liste_automate = []
automate_selected=-1
liste_automate, automate_selected = select(liste_automate, automate_selected) # séléctionner un AEF


if(liste_automate[automate_selected]["Etats"] == {}):
	liste_automate, automate_selected = saisir_automate(liste_automate, automate_selected)


test2=1
while test2:
	afficher_menu()
	choice = input("Choisissez une action : ")
	choice = choice.strip()
	if(choice == "1"):
		liste_automate, automate_selected = select(liste_automate, automate_selected)
	elif(choice == "2"):
		afficher_AEF(liste_automate, automate_selected)
	elif(choice == "3"):
		liste_automate, automate_selected = editAEF(liste_automate, automate_selected)
	elif(choice == "4"):
		sauvegarder_AEF(liste_automate, automate_selected)
	elif(choice == "5"):
		menu_test()
	elif(choice == "6"):
		menu_modif()
	elif(choice == "7"):
		menu_generer()
	elif(choice == "8"):
		liste_automate, automate_selected = demande_suppr(liste_automate, automate_selected)
	elif(choice == "9"):
		test2 = 0
	else:
		print("Veuillez entrer l'une des options proposées\n")



