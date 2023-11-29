def est_deterministe(automate):
    if len(automate["Etats_initiaux"])>1: # check that there is only one entry
        print("L'automate n'est pas déterministe.")
        return False
    etats = automate["Etats"]
    for etat, transitions in etats.items(): # loops for each etat
        for transi, etatfin in transitions.items(): # checks that there is only one arrival state for each transition
            if len(etatfin)>1:
                print("L'automate n'est pas déterministe.")
                return False
    print("L'automate est déterministe.")
    return True