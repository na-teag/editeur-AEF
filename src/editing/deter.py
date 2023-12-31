# This file contains all functions to verify if an automate is determinist and to change it into a determinist one 

from data.structure import createAutomate

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
        automate2 = createAutomate()
        automate2["Etats_initiaux"] = automate["Etats_initiaux"]
        automate2["Etats_finaux"] = automate["Etats_finaux"]
        automate2["Nom"] = automate["Nom"]
        automate["Etats"]["Etats_initiaux"]



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

automate ={
   "Etats": {
       "1": {"a": ["1","3"], "b": ["2"]},
       "2": {"b": ["1","4"]},
       "3": {"a": ["4"], "b": ["2"]},
       "4": {"a": ["4"], "b": ["2"]}
   },
   "Etats_initiaux": ["1"],
   "Etats_finaux": ["2"],
}

automate0 ={
   "Etats": {
   },
   "Etats_initiaux": [],
   "Etats_finaux": [],
}

def rendredeterministe(automate):
    nouvetat = []
    automate0["Etats_initiaux"] = automate["Etats_initiaux"]
    automate0["Etats_finaux"] = automate["Etats_finaux"]
    i = automate0["Etats_initiaux"]
    etats = automate["Etats"]
    for etat, transitions in etats.items(): # loops for each etat
    
        if etat in i:
            print("on rentre dans l'etat ini")
            automate0["Etats"][etat] = {}
            for transi, etatfin in transitions.items():
                if len(etatfin) > 1:
                    etatfinc = ','.join(etatfin)
                    automate0["Etats"][etatfinc] = {}
                    
                    nouvetat.append(etatfinc)
                    print(nouvetat)
                    
                    etatfinl = [','.join(etatfin)]
                    automate0["Etats"][etat][transi] = etatfinl
                    
                    print("fin")
                else:
                    automate0["Etats"][etat][transi] = etatfin
                    etatfinc = ','.join(etatfin)
                    nouvetat.append(etatfinc)
                    print(nouvetat)
                    automate0["Etats"][etatfinc] = {}
    print("fin etat ini")
    print(nouvetat)
    print("-----------------------------------------------")
    letat = []
    ltransi = []
    letatfin = []
    while len(nouvetat) > 0 :
        etat_rechercher = [nouvetat.pop(0)]
        print("**************")
        print(nouvetat)
        print(etat_rechercher)
        print(list(map(str, etat_rechercher[0].split(','))))
        print("**************")
        
        if len(list(map(str, etat_rechercher[0].split(',')))) == 1:
            for etat, transitions in etats.items():
                if etat in etat_rechercher:
                    print("on rentre dans l'etat nouv")
                    print("----")
                    for transi, etatfin in transitions.items():
                        etatfinl = [','.join(etatfin)]
                        etatfinc = ','.join(etatfin)
                        if len(etatfin) > 1:
                            automate0["Etats"][etat][transi] = etatfinl
                            if etatfinc not in automate0["Etats"]:
                                automate0["Etats"][etatfinc] = {}
                                nouvetat.append(etatfinc)
                                print(nouvetat)
                        else :
                            automate0["Etats"][etat][transi] = etatfin
                            if etatfinc not in automate0["Etats"]:
                                automate0["Etats"][etatfinc] = {}
                                nouvetat.append(etatfin)
                                print(nouvetat)
            print("fin etat rajouté")
            print(nouvetat)
        else :
            print("osjidnfgsgf")
            for etat, transitions in etats.items():  
                if etat in etat_rechercher:
                    print("on rentre dans l'etat relou")
                    print("----")
                    letat.append(etat)
                    for transi, etatfin in transitions.items():
                        ltransi.append(transi)
                        letatfin.append(etatfin)
            #nouvetat.pop(0)

rendredeterministe(automate)
print("\nAutomate d'origine :")
print(automate)
print("\nAutomate converti :")
print(automate0)


#etatfin = etatfin.split(',')
#list(map(str, etatfin[0].split(',')))