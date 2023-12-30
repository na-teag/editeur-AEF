

def est_emonde(automate): # Check if the given automaton is émondé, every state either is a final state or has outgoing transitions.
    for etat in automate["Etats"]:
        if automate["Etats"][etat] == {} and etat not in automate["Etats_finaux"]:
            return False
    return True
