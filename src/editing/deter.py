# This file contains all functions to verify if an automate is determinist and to change it into a determinist one 

from data.structure import createAutomate
from copy import deepcopy
from display.display import displayAEF

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


automate0 ={ # initializes the deterministic automaton
   "Etats": {
   },
   "Etats_initiaux": [],
   "Etats_finaux": [],
   "Nom" : ""
}


def rendredeterministe(automate):
    if est_deterministe(automate): # checks if the automaton is already determinist
        print("il n'y a pas besoin de modification.")
    else:
        listechgmt = []
        nouvetat = []
        automate0["Etats_initiaux"] = automate["Etats_initiaux"] # initializes the deterministic automaton
        automate0["Etats_finaux"] = automate["Etats_finaux"]
        automate0["Nom"] = automate["Nom"]
        automate0["Nom"] += "_deterministe"
        i = automate0["Etats_initiaux"] # initialize variables for loops
        etats = automate["Etats"]
        for etat, transitions in etats.items(): # loops for each etat
            if etat in i: # checks that the state corresponds to the desired state
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
        while len(nouvetat) > 0 : # is carried out as long as there remains unprocessed state
            etat_rechercher = nouvetat[0]
            etat_rechercherc = [nouvetat.pop(0)]
            etat_rechercherl = list(map(str, etat_rechercherc[0].split(',')))
            if len(etat_rechercherl) == 1:
                for etat, transitions in etats.items():
                    if etat in etat_rechercherl: # checks that the state corresponds to the desired state
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
                                    nouvetat.append(etatfinc)
            else :
                for etat, transitions in etats.items():
                    if etat in etat_rechercherl: # checks that the state corresponds to the desired state
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
                                        nouvetat.append(etatfinc)
                            else :
                                temp = ','.join(automate0["Etats"][etat_rechercherc[0]][transi])
                                etatcreer = list(map(str, temp.split(',')))
                                if etatfinc not in etatcreer:
                                    etatcomplet = [",".join(etatfinl+automate0["Etats"][etat_rechercherc[0]][transi])]
                                    automate0["Etats"][etat_rechercherc[0]][transi] = etatcomplet                   
            etats0 = automate0["Etats"]
            u = '"' + str(etat_rechercher) + '"'
            for etat, transitions in etats0.items():
                if etat in u: # checks that the state corresponds to the desired state
                    for transi, etatfin in transitions.items():
                        etatfinc = ','.join(etatfin)
                        if etatfinc not in etats0:
                            listechgmt.append(etatfinc)
            while listechgmt : # adds to nouvetat the states created which did not yet exist
                automate0["Etats"][listechgmt[0]] = {}
                nouvetat.append(listechgmt[0])
                listechgmt.pop(0)
        print("\nAutomate converti :")
        displayAEF(automate0)
        return automate0

def autodeter(liste, num_automate):
	automate = liste[num_automate]
	automated = rendredeterministe(automate)
	num_automate = len(liste)
	liste.append(deepcopy(automated))
	return liste, num_automate                       

# automate ={
#    "Etats": {
#        "1": {"a": ["1","3"], "b": ["2"]},
#        "2": {"b": ["1","4"]},
#        "3": {"a": ["4"], "b": ["2"]},
#        "4": {"a": ["4"], "b": ["2"]}
#    },
#    "Etats_initiaux": ["1"],
#    "Etats_finaux": ["2"],
#    "Nom" : "automate"
# }

# automatevoulu ={
#    "Etats": {
#        "1": {"a": ["1,3"], "b": ["2"]},
#        "2": {"b": ["1,4"]},
#        "1,3": {"a": ["1,3,4"], "b": ["2"]},
#        "1,3,4": {"a": ["1,3,4"], "b": ["2"]},
#        "1,4": {"a": ["1,3,4"], "b": ["2"]}
#    },
#    "Etats_initiaux": ["1"],
#    "Etats_finaux": ["2"],
# }                       
                        
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