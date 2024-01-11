import modif as md
import structure as strct


def displayAEF(automate):
	print("Nom :", automate["Nom"])
	print("Alphabet:", strct.alphabet(automate))
	print("États: {")
	for state, transitions in automate["Etats"].items():
		print(f"\t{state}")
		for transition, etat_suivant in transitions.items():
			print(f"\t   {transition} , {etat_suivant}")
	print("\t}")
	print("États initiaux:", automate["Etats_initiaux"])
	print("États finaux:", automate["Etats_finaux"])
	print("\n\n\n")



def menu_edit(list_automate, automate_selected):
	choix = 0
	while(choix != "5" and choix != ""):
		choix = input("\n\nQue souhaitez vous modifier ?\n\n1 : Nom\n2 : Etats et transitions\n3 : Etats initiaux\n4 : Etats finaux\n5 : retour\n\n").strip()
		if(choix == "1"):
			print("\033[2J") # clear the screen
			print("Nom actuel :", list_automate[automate_selected]["Nom"])
			nom = input("Entrez le nouveau nom : ").strip()
			if(nom != ""):
				list_automate[automate_selected]["Nom"] = nom
				print("\033[2J") # clear the screen
			else:
				print("\033[2J") # clear the screen
				print("Action annulée")
				print("\n\n\n\n\n\n\n\n\n\n\n")
		elif(choix == "2"):
			print("\033[2J") # clear the screen
			list_automate, automate_selected = md.editStates(list_automate, automate_selected)
		elif(choix == "3"):
			print("\033[2J") # clear the screen
			list_automate, automate_selected = md.changeStatesInitFinal(list_automate, automate_selected, 0)
		elif(choix == "4"):
			print("\033[2J") # clear the screen
			list_automate, automate_selected = md.changeStatesInitFinal(list_automate, automate_selected, 1)
		elif(choix != "5" and choix != ""):
			print("\033[2J") # clear the screen
			print("Veuillez entrer une des options proposées")
			print("\n\n\n\n\n\n\n\n\n\n\n")
	print("\033[2J") # clear the screen
	return list_automate, automate_selected