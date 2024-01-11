import display as dis
import structure as strct
import modif as md






def main(): # in a function so it can be called by tests.py
	
	global list_automate
	list_automate = []
	global automate_selected
	automate_selected = -1
	list_automate, automate_selected = strct.loadAutomate(list_automate, automate_selected)

	test2=1
	while test2:

		print("1 : séléctionner un AEF")
		print("2 : afficher l'AEF")
		print("3 : éditer l'AEF")
		print("4 : supprimer l'AEF")
		print("5 : quitter le programme")
		print("\n\n\n")

		choice = input("Choisissez une action : ")
		choice = choice.strip()
		if(choice == "1"):
			print("\033[2J") # clear the screen
			list_automate, automate_selected = strct.loadAutomate(list_automate, automate_selected)
		elif(choice == "2"):
			print("\033[2J") # clear the screen
			dis.displayAEF(list_automate[automate_selected])
		elif(choice == "3"):
			print("\033[2J") # clear the screen
			list_automate, automate_selected = dis.menu_edit(list_automate, automate_selected)
		elif(choice == "4"):
			list_automate, automate_selected = md.demandDelete(list_automate, automate_selected)
		elif(choice == "5"):
			test2 = 0
			return 0
		else:
			print("\033[2J") # clear the screen
			print("Veuillez entrer l'une des options proposées\n")



print("\033[2J") # clear the screen
main()