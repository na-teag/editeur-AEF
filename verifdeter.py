def est_deterministe(automate):
    if len(automate["Etats_initiaux"])>1:
        print("L'automate n'est pas déterministe.")
        return False
    etats = automate["Etats"]
    for etat, transitions in etats.items():
        for transi, etatfin in transitions.items():
            if len(etatfin)>1:
                print("L'automate n'est pas déterministe.")
                return False
    print("L'automate est déterministe.")
    return True