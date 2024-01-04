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

automatevoulu ={
   "Etats": {
       "1": {"a": ["1,3"], "b": ["2"]},
       "2": {"b": ["1,4"]},
       "1,3": {"a": ["1,3,4"], "b": ["2"]},
       "1,3,4": {"a": ["1,3,4"], "b": ["2"]},
       "1,4": {"a": ["1,3,4"], "b": ["2"]}
   },
   "Etats_initiaux": ["1"],
   "Etats_finaux": ["2"],
}

def rendredeterministe(automate):
    listechgmt = []
    nouvetat = []
    automate0["Etats_initiaux"] = automate["Etats_initiaux"]
    automate0["Etats_finaux"] = automate["Etats_finaux"]
    i = automate0["Etats_initiaux"]
    etats = automate["Etats"]
    for etat, transitions in etats.items(): # loops for each etat
    
        if etat in i:
            automate0["Etats"][etat] = {}
            for transi, etatfin in transitions.items():
                if len(etatfin) > 1:
                    etatfinc = ','.join(etatfin)
                    automate0["Etats"][etatfinc] = {}
                    
                    nouvetat.append(etatfinc)
                    
                    etatfinl = [','.join(etatfin)]
                    automate0["Etats"][etat][transi] = etatfinl
                else:
                    automate0["Etats"][etat][transi] = etatfin
                    etatfinc = ','.join(etatfin)
                    nouvetat.append(etatfinc)
                    automate0["Etats"][etatfinc] = {}
    while len(nouvetat) > 0 :
        etat_rechercher = nouvetat[0]
        etat_rechercherc = [nouvetat.pop(0)]
        etat_rechercherl = list(map(str, etat_rechercherc[0].split(',')))
        if len(etat_rechercherl) == 1:
            for etat, transitions in etats.items():
                if etat in etat_rechercherl:
                    for transi, etatfin in transitions.items():
                        etatfinl = [','.join(etatfin)]
                        etatfinc = ','.join(etatfin)
                        if len(etatfin) > 1:
                            automate0["Etats"][etat][transi] = etatfinl
                            if etatfinc not in automate0["Etats"]:
                                automate0["Etats"][etatfinc] = {}
                                nouvetat.append(etatfinc)
                        else :
                            automate0["Etats"][etat][transi] = etatfin
                            if etatfinc not in automate0["Etats"]:
                                automate0["Etats"][etatfinc] = {}
                                nouvetat.append(etatfin)
        else :
            for etat, transitions in etats.items():
                if etat in etat_rechercherl:
                    for transi, etatfin in transitions.items():
                        etatfinl = [','.join(etatfin)]
                        etatfinc = ','.join(etatfin)
                        if transi not in automate0["Etats"][etat_rechercherc[0]]:
                            if len(etatfin) > 1:
                                automate0["Etats"][etat_rechercherc[0]][transi] = etatfinl
                                if etatfinc not in automate0["Etats"]:
                                    automate0["Etats"][etatfinc] = {}
                                    nouvetat.append(etatfinc)
                            else :
                                automate0["Etats"][etat_rechercherc[0]][transi] = etatfin
                                if etatfinc not in automate0["Etats"]:
                                    automate0["Etats"][etatfinc] = {}
                                    nouvetat.append(etatfin)
                        else :
                            temp = ','.join(automate0["Etats"][etat_rechercherc[0]][transi])
                            etatcreer = list(map(str, temp.split(',')))
                            if etatfinc not in etatcreer:
                                etatcomplet = [",".join(etatfinl+automate0["Etats"][etat_rechercherc[0]][transi])]
                                automate0["Etats"][etat_rechercherc[0]][transi] = etatcomplet
                            
        etats0 = automate0["Etats"]
        u = '"' + str(etat_rechercher) + '"'
        for etat, transitions in etats0.items():
            if etat in u:
                for transi, etatfin in transitions.items():
                    etatfinc = ','.join(etatfin)
                    if etatfinc not in etats0:
                        listechgmt.append(etatfinc)
        while listechgmt :
            automate0["Etats"][listechgmt[0]] = {}
            nouvetat.append(listechgmt[0])
            listechgmt.pop(0)
    print("\nAutomate converti :")
    print(automate0)                           

                        
                        
# rendredeterministe(automate)
# print("\nAutomate d'origine :")
# print(automate)
# print("\nAutomate converti :")
# print(automate0)
# print("\nAutomate voulue :")
# print(automatevoulu)

#else :
                            #print("l'etat existe pas")
            #nouvetat.pop(0)


#etatfin = etatfin.split(',')
#list(map(str, etatfin[0].split(',')))
#list_a = ["1", "2", "3"]
#list_b = ["4,5,6"]

#list_c = ",".join(list_a + list_b)