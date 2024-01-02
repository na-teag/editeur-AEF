
import editing.modif as md
import editing.complet as comp
import editing.deter as det
import editing.testermot as testermot
import display.image as im
import display.display as dis
import data.structure as strct
import data.file as dfile
import editing.complement as complt
import editing.mirroir as mir
from copy import deepcopy



#automate ={
#    "Etats": {
#        "Etat0": {"Transition1": ["Etat1"], "Transition2": ["Etat0"]},
#        "Etat1": {"Transition3": ["Etat0"], "Transition4": ["Etat1"]}
#    },
#    "Etats_initiaux": ["Etat0"],
#    "Etats_finaux": ["Etat1"],
#    "Nom" : "test"
#}







def afficher_menu():
	print("\n\n\n\n\n\n\n\n")
	print("1 : séléctionner un AEF")
	print("2 : visualiser l'AEF séléctionné")
	print("3 : générer une image de l'AEF")
	print("4 : éditer l'AEF")
	print("5 : sauvegarder l'AEF")
	print("6 : faire des tests sur l'AEF")
	print("7 : modifier l'AEF selon une propriété")
	print("8 : générer un AEF à partir de celui-ci")
	print("9 : supprimer l'AEF")
	print("10 : quitter le programme")
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
	print("4 : rendre l'AEF minimal")
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
			testermot.tester(list_automate[automate_selected]) # calls the function tester
		elif(choice == "2"):
			comp.est_complet(list_automate[automate_selected]) # calls the function est_complet
		elif(choice == "3"):
			det.est_deterministe(list_automate[automate_selected]) # calls the function est_deterministe
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
			print("non disponible")  ###### A FAIRE ######
		elif(choice == "2"):
			complt.complement(list_automate[automate_selected]) # calls the function complement
		elif(choice == "3"):
			list_automate[automate_selected]=deepcopy(mir.miroirf(list_automate[automate_selected])	)	# calls the function complement
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
			comp.rendrecomplet(list_automate[automate_selected]) # calls the function rendrecomplet
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

def main(): # in a function so it can be called by tests.py

	global list_automate
	list_automate = []
	global automate_selected
	automate_selected = -1
	list_automate, automate_selected = dfile.loadAutomate(list_automate, automate_selected) # select a FA



	test2=1
	while test2:
		afficher_menu()
		choice = input("Choisissez une action : ")
		choice = choice.strip()
		if(choice == "1"):
			list_automate, automate_selected = dfile.loadAutomate(list_automate, automate_selected)
		elif(choice == "2"):
			dis.displayAEF(list_automate[automate_selected])
		elif(choice == "3"):
			im.image(list_automate, automate_selected)
		elif(choice == "4"):
			list_automate, automate_selected = dis.editAEF(list_automate, automate_selected)
		elif(choice == "5"):
			dfile.saveAEF(list_automate[automate_selected])
		elif(choice == "6"):
			menu_test()
		elif(choice == "7"):
			menu_modif()
		elif(choice == "8"):
			menu_generer()
		elif(choice == "9"):
			list_automate, automate_selected = md.demandDelete(list_automate, automate_selected)
		elif(choice == "10"):
			test2 = 0
			return 0
		else:
			print("Veuillez entrer l'une des options proposées\n")



if __name__ == '__main__':
	main()