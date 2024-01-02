automate ={
    "Etats": {                                                      #exemple
       "Etat0": {"Transition1": ["Etat0"], "Transition2": ["Etat1"]},
       "Etat1": {"Transition1": ["Etat1"], "Transition2": ["Etat1"]},
   },
   "Etats_initiaux":{"Etat0"},
   "Etats_finaux": {"Etat1"},
}


def complement(automate):                                           #modify the automaton to make his complement
    sEtat = automate['Etats_finaux']                                #list to look at final states
    Liste = []
    for etat in automate["Etats"].keys():                           #comparing which state is not final
        if etat not in sEtat:
            Liste.append(etat)                                      #filling the list of final states
    automate['Etats_finaux']= {}
    automate['Etats_finaux'] = Liste                                #switching states
    print("complement of the automaton")