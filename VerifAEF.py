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
