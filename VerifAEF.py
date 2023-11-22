def est_complet(automate):
    etats = automate['etats']
    alphabet = automate['alphabet']
    transition = automate['transition']
    
    for etat in etats:
        for symbole in alphabet:
            if (etat, symbole) not in transition:
                return False
                
    return True

automate = {
    'etats': {'q0', 'q1'},
    'alphabet': {'0', '1'},
    'transition': {('q0', '0'): 'q1', ('q0', '1'): 'q0', ('q1', '0'): 'q1', ('q1', '1'): 'q0'},
    'etat_initial': 'q0',
    'etats_finaux': {'q1'}
}

if est_complet(automate):
    print("L'automate est complet.")
else:
    print("L'automate n'est pas complet.")

def est_deterministe(automate):
    for etat, transitions in automate.items():
        symboles = set()
        for symbole, destination in transitions.items():
            # Vérifie si le symbole a déjà une transition depuis cet état
            if symbole in symboles:
                return False
            symboles.add(symbole)
    return True

automate = {
    'q0': {'a': 'q1', 'b': 'q2'},
    'q1': {'a': 'q3', 'b': 'q4'},
    'q2': {'a': 'q5', 'b': 'q6'},
    'q3': {'a': 'q7', 'b': 'q8'},
    'q4': {'a': 'q9', 'b': 'q10'},
    'q5': {'a': 'q11', 'b': 'q12'},
    'q6': {'a': 'q13', 'b': 'q14'},
    'q7': {'a': 'q15', 'b': 'q16'},
}

if est_deterministe(automate):
    print("L'automate est déterministe.")
else:
    print("L'automate n'est pas déterministe.")

