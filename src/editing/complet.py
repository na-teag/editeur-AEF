# This file contains all functions to verify if an automate is complete and to change it into a complete one 


from data.structure import alphabet

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