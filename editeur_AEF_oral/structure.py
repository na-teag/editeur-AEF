#   This file contains all functions for basic structure 
import modif as md

'''
automate ={
    "Etats": {
        "Etat0": {"Transition1": ["Etat1"], "Transition2": ["Etat0"]},
        "Etat1": {"Transition3": ["Etat0"], "Transition4": ["Etat1"]}
    },
    "Etats_initiaux": ["Etat0"],
    "Etats_finaux": ["Etat1"],
    "Nom" : "test"
}
'''



def createAutomate():
	return {
		"Etats": {},
		"Etats_initiaux": [],
		"Etats_finaux": [],
		"Nom": ""
	}



def alphabet(automate): # calculate the alphabet
	transitions_liste = []
	for transitions in automate["Etats"].values():
		transitions_liste.extend(transitions.keys())
	alphabet = list(set(transitions_liste))  # deleting doubles
	return alphabet





def loadAutomate(list_automate, automate_selected):
	if(automate_selected > -1 and list_automate[automate_selected] == createAutomate()):
		list_automate, automate_selected = md.deleteAutomate(list_automate, automate_selected) # in case we created a new one and exited the creat function
	nbr = 1 # nbr of additional option other than existing FA 
	nbr += 1 # +1 because menu starts at 1 and not 0
	if(automate_selected == -1):
		print("\n\n\n\n\nAEF séléctionné : aucun")
	else:
		print("AEF séléctionné : ", automate_selected+nbr)
	nbr2=nbr
	print("\nséléctionnez un AEF :\n1 : créer un nouvel AEF")
	for aef in list_automate: # print all FA's names
		print(nbr2, ":", aef["Nom"])
		nbr2+=1
	
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
			automate_selected = len(list_automate) # the index of the FA is the lenght of the list before it's added to it : empty list -> first FA at index 0
			list_automate.append(createAutomate())
			print("\033[2J") # clear the screen
			list_automate, automate_selected = md.editStates(list_automate, automate_selected)
			test=0
			print("\033[2J") # clear the screen
		elif(nbr <= choix and choix < len(list_automate)+nbr):
			automate_selected = choix-nbr # 1 options added in a list begging at 1 -> the index is shifted by nbr
			test=0
			print("\033[2J") # clear the screen
		else:
			print("\n\nVeuillez choisir une des options proposées")
	return list_automate, automate_selected