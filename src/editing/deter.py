# This file contains all functions to verify if an automate is determinist and to change it into a determinist one 

from data.structure import createAutomate
from copy import deepcopy
from display.display import displayAEF

################################################################ Function for checking the deterministic state of the automaton ############################################

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

################################################################ Function for determining an automaton ####################################################################

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
        for etat, transitions in etats.items(): # loops for each etat --------------------------------------- FIRST LOOP - initialize the initial state
            if etat in i: # checks that the state corresponds to the desired state
                automate0["Etats"][etat] = {}
                for transi, etatfin in transitions.items():
                    if len(etatfin) > 1: # checks if the transition can lead to several states
                        etatfinc = ','.join(etatfin) # converts the state into a format expected in the automaton : a string element
                        automate0["Etats"][etatfinc] = {}
                        nouvetat.append(etatfinc) # adds to nouvetat the states created
                        etatfinl = [','.join(etatfin)]
                        automate0["Etats"][etat][transi] = etatfinl
                    else:
                        automate0["Etats"][etat][transi] = etatfin
                        etatfinc = ','.join(etatfin) # converts the state into a format expected in the automaton : a string element
                        nouvetat.append(etatfinc) # adds to nouvetat the states created
                        automate0["Etats"][etatfinc] = {}
        while len(nouvetat) > 0 : # is carried out as long as there remains unprocessed state ---------------- SECOND LOOP - adds the corresponding transitions for each state added to the new automaton
            etat_rechercher = nouvetat[0]
            etat_rechercherc = [nouvetat.pop(0)]
            etat_rechercherl = list(map(str, etat_rechercherc[0].split(',')))
            if len(etat_rechercherl) == 1: # adds transitions corresponding to a single state
                for etat, transitions in etats.items():
                    if etat in etat_rechercherl: # checks that the state corresponds to the desired state
                        for transi, etatfin in transitions.items():
                            etatfinl = [','.join(etatfin)] # converts the state into a format expected in the automaton : a list composed of a string element
                            etatfinc = ','.join(etatfin) # converts the state into a format expected in the automaton : a string element
                            if len(etatfin) > 1: # checks if the transition can lead to several states
                                automate0["Etats"][etat][transi] = etatfinl
                                if etatfinc not in automate0["Etats"]:
                                    automate0["Etats"][etatfinc] = {}
                                    nouvetat.append(etatfinc) # adds to nouvetat the states created
                            else :
                                automate0["Etats"][etat][transi] = etatfin
                                if etatfinc not in automate0["Etats"]:
                                    automate0["Etats"][etatfinc] = {}
                                    nouvetat.append(etatfinc) # adds to nouvetat the states created
            else : # adds the transitions corresponding to a sum state of several
                for etat, transitions in etats.items():
                    if etat in etat_rechercherl: # checks that the state corresponds to the desired state
                        for transi, etatfin in transitions.items():
                            etatfinl = [','.join(etatfin)] # converts the state into a format expected in the automaton : a list composed of a string element
                            etatfinc = ','.join(etatfin) # converts the state into a format expected in the automaton : a string element
                            if transi not in automate0["Etats"][etat_rechercherc[0]]:
                                if len(etatfin) > 1: # checks if the transition can lead to several states
                                    automate0["Etats"][etat_rechercherc[0]][transi] = etatfinl
                                    if etatfinc not in automate0["Etats"]:
                                        automate0["Etats"][etatfinc] = {}
                                        nouvetat.append(etatfinc) # adds to nouvetat the states created
                                else :
                                    automate0["Etats"][etat_rechercherc[0]][transi] = etatfin
                                    if etatfinc not in automate0["Etats"]:
                                        automate0["Etats"][etatfinc] = {}
                                        nouvetat.append(etatfinc) # adds to nouvetat the states created
                            else : # add several arrival states because appearing in several difference state transitions
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
                        if etatfinc not in etats0: # check if the states created did not yet exist
                            listechgmt.append(etatfinc)
            while listechgmt : # adds to nouvetat the states created which did not yet exist because being the sum of several states
                automate0["Etats"][listechgmt[0]] = {}
                nouvetat.append(listechgmt[0]) # adds to nouvetat the states created
                listechgmt.pop(0)
        print("\nAutomate converti :")
        displayAEF(automate0) # display the deterministic automaton
        return automate0 # return the deterministic automaton

def autodeter(liste, num_automate): # call the function, with a copy of the  automaton, then add and select the new one
	automate = liste[num_automate] # stock the automaton
	automated = rendredeterministe(automate) # call rendredeterministe
	num_automate = len(liste) # calculates the number associated with the automaton
	liste.append(deepcopy(automated)) # copy and add the number associated with the automaton
	return liste, num_automate