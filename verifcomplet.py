def alphabet(automate): # calculer l'alphabet
	transitions_liste = []
	for transitions in automate["Etats"].values():
		transitions_liste.extend(transitions.keys())
	alphabet = list(set(transitions_liste))  # Suppression des doublons
	return alphabet

def est_complet(automate):
    Alphabet=alphabet(automate)
    etats = automate['Etats']  
    for etat, transitions in etats.items():
        for symbole in automate['Alphabet']:
            if symbole not in transitions:
                print("L'automate n'est pas complet.")
                break
    print("L'automate est complet.")