import json
import re # regex to test files names

from verifcomplet import *

def alphabet(automate): # calculate the alphabet
	transitions_liste = []
	for transitions in automate["Etats"].values():
		transitions_liste.extend(transitions.keys())
	alphabet = list(set(transitions_liste))  # Removing duplicates
	return alphabet

def rendrecomplet(automate):
    if est_complet(automate):
        print("L'automate est déjà complet.")
    else:
        Alphabet=alphabet(automate) # calculate the alphabet and put it in a variable
        etats = automate['Etats']
        for etat, transitions in etats.items(): # loops for each etat
            for symbole in Alphabet: # loops for each variable
                if symbole not in transitions:
                    automate["Etats"][etat][symbole] = [etat] # Add the missing transition
        print("L'automate est maintenant complet.")
        return True