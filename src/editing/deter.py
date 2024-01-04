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
    while len(nouvetat) > 0 :
        etat_rechercher = nouvetat[0]
        print(automate0["Etats"]["1,3"])
        print(nouvetat)
        etat_rechercherc = [nouvetat.pop(0)]
        print("************************************************************************************************************")
        print(etat_rechercherc[0])
        print(nouvetat)
        etat_rechercherl = list(map(str, etat_rechercherc[0].split(',')))
        print(etat_rechercherl)
        print("*************************************************************************************************************")
        
        if len(etat_rechercherl) == 1:
            for etat, transitions in etats.items():
                if etat in etat_rechercherl:
                    print("on rentre dans l'etat nouv")
                    print("----")
                    print(automate0["Etats"]["1,3"])
                    for transi, etatfin in transitions.items():
                        etatfinl = [','.join(etatfin)]
                        etatfinc = ','.join(etatfin)
                        print("1")
                        print(automate0["Etats"]["1,3"])
                        if len(etatfin) > 1:
                            automate0["Etats"][etat][transi] = etatfinl
                            if etatfinc not in automate0["Etats"]:
                                automate0["Etats"][etatfinc] = {}
                                nouvetat.append(etatfinc)
                                print(nouvetat)
                        else :
                            print(automate0["Etats"]["1,3"])
                            automate0["Etats"][etat][transi] = etatfin
                            print(automate0["Etats"]["1,3"])
                            if etatfinc not in automate0["Etats"]:
                                automate0["Etats"][etatfinc] = {}
                                nouvetat.append(etatfin)
                                print(nouvetat)
            print(automate0["Etats"]["1,3"])
            print("fin etat rajouté")
            print(nouvetat)
        else :
            print("osjidnfgsgf")
            for etat, transitions in etats.items():
                print("boucleetat")
                if etat in etat_rechercherl:
                    print("on rentre dans l'etat relou")
                    print("----")
                    for transi, etatfin in transitions.items():
                        print("hm")
                        etatfinl = [','.join(etatfin)]
                        etatfinc = ','.join(etatfin)
                        print(automate0["Etats"][etat_rechercherc[0]])
                        print(automate0["Etats"]["1,3"])
                        print(etat_rechercherc)
                        print(etat_rechercherl)
                        print(etat_rechercherc[0])
                        print("\nAutomate converti :")
                        print(automate0)
                        #if etat_rechercherc[0] in automate0["Etats"]:
                            #print("l'etat existe")
                        if transi not in automate0["Etats"][etat_rechercherc[0]]:
                            print("mais pas la transi")
                            print(etatfin)
                            if len(etatfin) > 1:
                                automate0["Etats"][etat_rechercherc[0]][transi] = etatfinl
                                if etatfinc not in automate0["Etats"]:
                                    automate0["Etats"][etatfinc] = {}
                                    nouvetat.append(etatfinc)
                                    print(nouvetat)
                            else :
                                automate0["Etats"][etat_rechercherc[0]][transi] = etatfin
                                if etatfinc not in automate0["Etats"]:
                                    automate0["Etats"][etatfinc] = {}
                                    nouvetat.append(etatfin)
                                    print(nouvetat)
                                print("transi+etatfin créer")
                        else :
                            print("la transi existe")
                            print(automate0["Etats"]["1,3"])
                            print(automate0["Etats"][etat_rechercherc[0]][transi])
                            print(etatfin)
                            print(etatfinl)
                            print(etat_rechercherc[0])
                            temp = ','.join(automate0["Etats"][etat_rechercherc[0]][transi])
                            print(temp[0])
                            etatcreer = list(map(str, temp.split(',')))
                            print(etatcreer)
                            print(etatfinc)
                            print("--------")
                            if etatfinc not in etatcreer:
                                etatcomplet = [",".join(etatfinl+automate0["Etats"][etat_rechercherc[0]][transi])]
                                automate0["Etats"][etat_rechercherc[0]][transi] = etatcomplet
                                print(automate0["Etats"]["1,3"])
                            
        etats0 = automate0["Etats"]
        u = '"' + str(etat_rechercher) + '"'
        for etat, transitions in etats0.items():
            if etat in u:
                for transi, etatfin in transitions.items():
                    etatfinc = ','.join(etatfin)
                    print("ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
                    
                    print(u)
                    print(etatfinc)
                    print(automate0["Etats"])
                    if etatfinc not in etats0:
                        listechgmt.append(etatfinc)
        while listechgmt :
            automate0["Etats"][listechgmt[0]] = {}
            nouvetat.append(listechgmt[0])
            print(nouvetat)
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