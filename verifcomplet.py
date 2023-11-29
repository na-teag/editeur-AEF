def alphabet(automate): # calculate the alphabet
	transitions_liste = []
	for transitions in automate["Etats"].values():
		transitions_liste.extend(transitions.keys())
	alphabet = list(set(transitions_liste))  # Removing duplicates
	return alphabet

def est_complet(automate):
    Alphabet=alphabet(automate) # calculate the alphabet and put it in a variable
    etats = automate['Etats']
    for etat, transitions in etats.items(): # loops for each etat
        for symbole in Alphabet: # loops for each variable
            if symbole not in transitions:
                print("L'automate n'est pas complet.")
                return False
    print("L'automate est complet.")
    return True