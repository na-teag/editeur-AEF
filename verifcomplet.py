def alphabet(automate): # calculer l'alphabet
	transitions_liste = []
	for transitions in automate["Etats"].values():
		transitions_liste.extend(transitions.keys())
	alphabet = list(set(transitions_liste))  # Suppression des doublons
	return alphabet

def est_complet(automate):
    Alphabet=alphabet(automate)
    etats = automate['Etats']
    test = 0
    for etat, transitions in etats.items():
        for symbole in Alphabet:
            if symbole not in transitions:
                print("L'automate n'est pas complet.")
                test = 1
                break
        if(test == 1):
            break
    if(test == 0):
        print("L'automate est complet.")