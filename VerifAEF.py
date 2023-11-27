automate ={
   "Etats": {
       "Etat0": {"Transition1": ["Etat1"], "Transition2": ["Etat0"], "Transition3": ["Etat0"], "Transition4": ["Etat0"]},
       "Etat1": {"Transition3": ["Etat0"], "Transition4": ["Etat1"], "Transition1": ["Etat1"], "Transition2": ["Etat1"]}
   },
   "Etats_initiaux": ["Etat0"],
   "Etats_finaux": ["Etat1"],
   "Alphabet": ["Transition1","Transition2","Transition3","Transition4"]
}

def est_complet(automate):
    etats = automate['Etats']  
    for etat, transitions in etats.items():
        for symbole in automate['Alphabet']:
            if symbole not in transitions:
                return False
    return True

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

# automate = {
#     'q0': {'a': 'q1', 'b': 'q2'},
#     'q1': {'a': 'q3', 'b': 'q4'},
#     'q2': {'a': 'q5', 'b': 'q6'},
#     'q3': {'a': 'q7', 'b': 'q8'},
#     'q4': {'a': 'q9', 'b': 'q10'},
#     'q5': {'a': 'q11', 'b': 'q12'},
#     'q6': {'a': 'q13', 'b': 'q14'},
#     'q7': {'a': 'q15', 'b': 'q16'},
# }

if est_deterministe(automate):
    print("L'automate est déterministe.")
else:
    print("L'automate n'est pas déterministe.")