# This file contains all functions to verify if an automate is determinist and to change it into a determinist one 


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



def rendredeterministe(automate):
    if est_deterministe(automate):
        print("L'automate est déjà déterministe.")
    else:
        if len(automate["Etats_initiaux"])>1: # check that there is only one entry
            print("L'automate n'est pas déterministe.")
            return False
        etats = automate["Etats"]
        for etat, transitions in etats.items(): # loops for each etat
            for transi, etatfin in transitions.items(): # checks that there is only one arrival state for each transition
                if len(etatfin)>1:
                    print(etat)
                    print(transi)
                    print(etatfin)
                    automate["Etats"][etat][transi] = [i]
                    for etattransi in etatfin:
                        print(etattransi)
                        if automate["Etats"][etattransi][transi] != [i]:
                            print(28)
                            print(automate["Etats"][etattransi][transi])
                    i =+ 1
                    print(i)
        print("L'automate est maintenant déterministe.")
        return True