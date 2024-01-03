# This file contains all functions to display and choose anautomate

import editing.modif as md
import display.display as dis
import data.structure as strct
def editAEF(list_automate, automate_selected): # choose the modification
	choix = 0
	while(choix != "5" and choix != ""):
		choix = input("\n\nQue souhaitez vous modifier ?\n\n1 : Nom\n2 : Etats et transitions\n3 : Etats initiaux\n4 : Etats finaux\n5 : retour\n\n").strip()
		if(choix == "1"):
			print("\033[2J")
			print("Nom actuel :", list_automate[automate_selected]["Nom"])
			nom = input("Entrez le nouveau nom : ").strip()
			if(nom != ""):
				list_automate[automate_selected]["Nom"] = nom
				print("\033[2J")
			else:
				print("\033[2J")
				print("Action annulée")
				print("\n\n\n\n\n\n\n\n\n\n\n")
		elif(choix == "2"):
			print("\033[2J")
			list_automate, automate_selected = chooseModif(list_automate, automate_selected)
		elif(choix == "3"):
			print("\033[2J")
			list_automate, automate_selected = md.changeStatesInitFinal(list_automate, automate_selected, 0)
		elif(choix == "4"):
			print("\033[2J")
			list_automate, automate_selected = md.changeStatesInitFinal(list_automate, automate_selected, 1)
		elif(choix != "5" and choix != ""):
			print("\033[2J")
			print("Veuillez entrer une des options proposées")
			print("\n\n\n\n\n\n\n\n\n\n\n")
	print("\033[2J")
	return list_automate, automate_selected

def chooseModif(list_automate, automate_selected): # choose to either edit, rename, or delete states
	choix = 0
	while(choix != "4" and choix != ""):
		dis.displayAEF(list_automate[automate_selected])
		choix = input("\n\n\nQue voulez vous faire ?\n1 : Ajouter ou supprimer des transitions\n2 : Renommer un état\n3 : Supprimer un état\n4 : Retour\n\n\n").strip()
		if(choix == "1"):
			print("\033[2J")
			list_automate, automate_selected = md.editStates(list_automate, automate_selected)
		elif(choix == "2"):
			print("\033[2J")
			list_automate, automate_selected = md.renameStates(list_automate, automate_selected)
		elif(choix == "3"):
			print("\033[2J")
			list_automate, automate_selected = md.deleteStates(list_automate, automate_selected)
		elif(choix != "4" and choix != ""):
			print("\033[2J")
			print("Veuillez entrer une des options proposées")
			print("\n\n\n\n\n\n\n\n\n\n\n")
	print("\033[2J")
	return list_automate, automate_selected




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