# This file contains all functions to verify if an automate is complete and to change it into a complete one 

from data.structure import alphabet
from copy import deepcopy

################################################################ Function for checking the complete status of the automaton #############################################

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

################################################################ Completion function of an automaton #######################################################################

def rendrecomplet(automate):
    if est_complet(automate): # checks if the automaton is already complete
        print("il n'y a pas besoin de modification.")
    else:
        Alphabet=alphabet(automate) # calculate the alphabet and put it in a variable
        etats = automate['Etats']
        for etat, transitions in etats.items(): # loops for each etat
            for symbole in Alphabet: # loops for each variable
                if symbole not in transitions:
                    automate["Etats"][etat][symbole] = [etat] # Add the missing transition
        print("L'automate est maintenant complet.")
        return automate

def autocomp(liste, num_automate): # call the function, with a copy of the  automaton, then add and select the new one
    automate = liste[num_automate] # stock the automaton
    automatec = rendrecomplet(deepcopy(automate)) # call rendrecomplet
    automatec["Nom"] += "_complet" # adds complete to the name of the automaton
    num_automate = len(liste) # calculates the number associated with the automaton
    liste.append(automatec) # add the number associated with the automaton
    return liste, num_automate  