
import display.image as im
import display.display as dis
import data.structure as strct
import data.file as dfile
import editing.modif as md
import editing.complet as comp
import editing.deter as det
import editing.testermot as testermot
import editing.complement as complt
import editing.miroir as mir
import editing.minimal as mini
import editing.langage as lang
import editing.emonde as emon
import editing.regex as regex
import editing.concat as concat
import editing.produit as prod
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
	print("1 : séléctionner un AEF")
	print("2 : visualiser l'AEF séléctionné")
	print("3 : générer une image de l'AEF")
	print("4 : éditer l'AEF")
	print("5 : sauvegarder l'AEF")
	print("6 : faire des tests sur l'AEF")
	print("7 : modifier l'AEF selon une propriété")
	print("8 : générer un AEF à partir de celui-ci")
	print("9 : faire une copie de l'AEF")
	print("10 : supprimer l'AEF")
	print("11 : quitter le programme")
	print("\n\n\n")

def afficher_menu_test():
	print("1 : tester si un mot est reconnu")
	print("2 : tester si l'AEF est complet")
	print("3 : tester si l'AEF est déterministe")
	print("4 : tester si l'AEF est émondé")
	print("5 : tester si cet AEF et un autre sont équivalents")
	print("6 : retour")
	print("\n\n\n")

def afficher_menu_modif():
	print("1 : rendre l'AEF complet")
	print("2 : rendre l'AEF déterministe")
	print("3 : rendre l'AEF émondé")
	print("4 : rendre l'AEF minimal")
	print("5 : retour")
	print("\n\n\n")

def afficher_menu_generer():
	print("1 : générer une expression régulière")
	print("2 : générer le langage de l'AEF")
	print("3 : générer l'AEF complément")
	print("4 : générer l'AEF miroir")
	print("5 : générer le produit de cet AEF et d'un autre")
	print("6 : générer la concaténation de cet AEF et d'un autre")
	print("7 : retour")
	print("\n\n\n")

def menu_test():
	test=1
	while test:
		afficher_menu_test()
		choice = input("Choisissez une action : ")
		choice = choice.strip()
		if(choice == "1"):
			print("\033[2J") # clear the screen
			dis.displayAEF(list_automate[automate_selected])
			print("\n\n\n\n")
			testermot.tester(list_automate[automate_selected]) # calls the function tester
			print("\n\n\n\n\n\n\n\n\n\n\n")
		elif(choice == "2"):
			print("\033[2J") # clear the screen
			comp.est_complet(list_automate[automate_selected]) # calls the function est_complet
			print("\n\n\n\n\n\n\n\n\n\n\n")
		elif(choice == "3"):
			print("\033[2J") # clear the screen
			det.est_deterministe(list_automate[automate_selected]) # calls the function est_deterministe
			print("\n\n\n\n\n\n\n\n\n\n\n")
		elif(choice == "4"):
			print("\033[2J") # clear the screen
			emon.est_emonde(list_automate[automate_selected]) # calls the function est_emonde
			print("\n\n\n\n\n\n\n\n\n\n\n")
		elif(choice == "5"):
			print("\033[2J") # clear the screen
			lang.test_automates_equivalents(list_automate, automate_selected)  ###### ERREURS ######
			print("\n\n\n\n\n\n\n\n\n\n\n")
		elif(choice == "6" or choice == ""):
			test=0
			print("\033[2J") # clear the screen
		else:
			print("\033[2J") # clear the screen
			print("Veuillez entrer l'une des options proposées\n")
			print("\n\n\n\n\n\n\n\n\n\n\n")

def menu_generer(list_automate, automate_selected):
	test=1
	while test:
		afficher_menu_generer()
		choice = input("Choisissez une action : ")
		choice = choice.strip()
		if(choice == "1"):
			print("\033[2J") # clear the screen
			regex.regex(list_automate[automate_selected]) # calls the function regex
			print("\n\n\n\n\n\n\n\n\n\n\n")
		elif(choice == "2"):
			print("\033[2J") # clear the screen
			lang.generer_langage(list_automate[automate_selected])  ###### ERREURS ######
			print("\n\n\n\n\n\n\n\n\n\n\n")
		elif(choice == "3"):
			print("\033[2J") # clear the screen
			list_automate, automate_selected = complt.complement(list_automate, automate_selected) # calls the function complement
			print("Complément généré et séléctionné\n\n\n\n\n\n\n\n\n\n\n")
		elif(choice == "4"):
			print("\033[2J") # clear the screen
			list_automate, automate_selected = mir.miroirf(list_automate, automate_selected) # calls the function miroir
			print("miroir généré et séléctionné\n\n\n\n\n\n\n\n\n\n\n")
		elif(choice == "5"):
			print("\033[2J") # clear the screen
			list_automate, automate_selected = prod.produit(list_automate, automate_selected) # calls the function miroir
			print("\n\n\n\n\n\n\n\n\n\n\n")
		elif(choice == "6"):
			print("\033[2J") # clear the screen
			list_automate, automate_selected = concat.concatener(list_automate, automate_selected) # calls the function concatener
			print("concaténation générée et séléctionnée\n\n\n\n\n\n\n\n\n\n\n")
		elif(choice == "7" or choice == ""):
			test=0
			print("\033[2J") # clear the screen
		else:
			print("\033[2J") # clear the screen
			print("Veuillez entrer l'une des options proposées\n")
			print("\n\n\n\n\n\n\n\n\n\n\n")
	return list_automate, automate_selected

def menu_modif(list_automate, automate_selected):
	test=1
	while test:
		afficher_menu_modif()
		choice = input("Choisissez une action : ")
		choice = choice.strip()
		if(choice == "1"):
			print("\033[2J") # clear the screen
			list_automate, automate_selected = comp.autocomp(list_automate, automate_selected) # calls the function autocomp
			print("\n\n\n\n\n\n\n\n\n\n\n")
		elif(choice == "2"):
			print("\033[2J") # clear the screen
			list_automate, automate_selected = det.autodeter(list_automate, automate_selected) # calls the function autodeter
			print("\n\n\n\n\n\n\n\n\n\n\n")
		elif(choice == "3"):
			print("\033[2J") # clear the screen
			list_automate, automate_selected = emon.emonde(list_automate, automate_selected) # calls the function emonde
			print("\n\n\n\n\n\n\n\n\n\n\n")
		elif(choice == "4"):
			print("\033[2J") # clear the screen
			#list_automate, automate_selected = mini.minimal(list_automate, automate_selected) # calls the function minimal   ###### ERREURS ######
			print("\n\n\n\n\n\n\n\n\n\n\n")
		elif(choice == "5" or choice == ""):
			test=0
			print("\033[2J") # clear the screen
		else:
			print("\033[2J") # clear the screen
			print("Veuillez entrer l'une des options proposées\n")
			print("\n\n\n\n\n\n\n\n\n\n\n")
	return list_automate, automate_selected







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
			print("\033[2J") # clear the screen
			list_automate, automate_selected = dfile.loadAutomate(list_automate, automate_selected)
		elif(choice == "2"):
			print("\033[2J") # clear the screen
			dis.displayAEF(list_automate[automate_selected])
		elif(choice == "3"):
			im.image(list_automate, automate_selected)
		elif(choice == "4"):
			print("\033[2J") # clear the screen
			list_automate, automate_selected = dis.editAEF(list_automate, automate_selected)
		elif(choice == "5"):
			print("\033[2J") # clear the screen
			dfile.saveAEF(list_automate[automate_selected])
		elif(choice == "6"):
			print("\033[2J") # clear the screen
			menu_test()
		elif(choice == "7"):
			print("\033[2J") # clear the screen
			list_automate, automate_selected = menu_modif(list_automate, automate_selected)
		elif(choice == "8"):
			print("\033[2J") # clear the screen
			list_automate, automate_selected = menu_generer(list_automate, automate_selected)
		elif(choice == "9"):
			print("\033[2J") # clear the screen
			list_automate.append(deepcopy(list_automate[automate_selected]))
			automate_selected = len(list_automate)-1
			list_automate[automate_selected]["Nom"] += "_copie"
			print("Copie effectuée et séléctionnée\n\n\n\n\n\n\n\n\n\n\n")
		elif(choice == "10"):
			list_automate, automate_selected = md.demandDelete(list_automate, automate_selected)
		elif(choice == "11"):
			test2 = 0
			return 0
		else:
			print("\033[2J") # clear the screen
			print("Veuillez entrer l'une des options proposées\n")



if __name__ == '__main__': # call the main function only if run by main.py, if called by tests.py, then do not call it
	print("\033[2J") # clear the screen
	main()