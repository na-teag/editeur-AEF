#   This file contains all functions for basic structure 

def createAutomate(): # creates an empty antomaton
	return {
		"Etats": {},
		"Etats_initiaux": [],
		"Etats_finaux": [],
		"Nom": ""
	}



def alphabet(automate): # calculates the alphabet
	transitions_liste = []
	for transitions in automate["Etats"].values():
		transitions_liste.extend(transitions.keys())
	alphabet = list(set(transitions_liste))  # deleting doubles
	return alphabet

