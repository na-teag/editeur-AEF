# This file contains all functions to display and choose anautomate

import editing.modif as md
import display.display as dis
import data.structure as strct
def editAEF(list_automate, automate_selected): # choose the modification
	choix = 0
	while(choix != "5"):
		choix = input("\n\nQue souhaitez vous modifier ?\n\n1 : Nom\n2 : Etats et transitions\n3 : Etats initiaux\n4 : Etats finaux\n5 : retour\n\n").strip()
		if(choix == "1"):
			print("Nom actuel :", list_automate[automate_selected]["Nom"])
			list_automate[automate_selected]["Nom"] = input("Entrez le nouveau nom : ").strip()
		elif(choix == "2"):
			list_automate, automate_selected = chooseModif(list_automate, automate_selected)
		elif(choix == "3"):
			list_automate, automate_selected = md.changeStatesInitFinal(list_automate, automate_selected, 0)
		elif(choix == "4"):
			list_automate, automate_selected = md.changeStatesInitFinal(list_automate, automate_selected, 1)
		elif(choix != "5"):
			print("Veuillez entrer une des options proposées")
	return list_automate, automate_selected

def chooseModif(list_automate, automate_selected): # choose to either edit, rename, or delete states
	choix = 0
	while(choix != "4"):
		print("\n\n\n\n\n\n\n\n\n\n\n")
		dis.displayAEF(list_automate[automate_selected])
		choix = input("\n\n\nQue voulez vous faire ?\n1 : Ajouter ou supprimer des transitions\n2 : Renommer un état\n3 : Supprimer un état\n4 : Retour\n\n\n").strip()
		if(choix == "1"):
			list_automate, automate_selected = md.editStates(list_automate, automate_selected)
		elif(choix == "2"):
			list_automate, automate_selected = md.renameStates(list_automate, automate_selected)
		elif(choix == "3"):
			list_automate, automate_selected = md.deleteStates(list_automate, automate_selected)
		elif(choix != "4"):
			print("Veuillez entrer une des options proposées")
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