#this file contains all the functions of th"e product of two automates 
"""  The functions are an adaption of the algorithm described here : 
        https://www.desmontils.net/emiage/Module209EMiage/c5/Ch5_10.htm (section 10.4)
"""
import data.structure as strct
import data.file as file
from copy import deepcopy

def calculLineProduct(stateList: list, alphabet: list, automate1: dict, automate2: dict):
    line = {}
    for key in alphabet:
        line[key] = [[],[]]

    for state in stateList[0]:
        for key in line:
            if key in automate1["Etats"][state]:
                for transitionTpo in automate1["Etats"][state][key]:
                    if transitionTpo not in line[key]:
                        line[key][0].append(transitionTpo)
    
    for state in stateList[1]:
        for key in line:
            if key in automate2["Etats"][state]:
                for transitionTpo in automate2["Etats"][state][key]:
                    if transitionTpo not in line[key]:
                        line[key][1].append(transitionTpo)
    return line



def product (automate1: dict, automate2: dict):
    alphabet = list(set( strct.alphabet(automate1) +  strct.alphabet(automate2) ))
    existingSet = [] #list of existing set of state
    newAutomateBP = [] #list of tuple (set of state, {"key":set of state for the key,...}). Make the blueprint for the new automate

    #each set will be structured as [ [automate1 states], [automate2 states] ], the sepration make sure that sere is no name conflict.

    #collect the starting state of each one.
    startingState = [[],[]]

    for state in automate1["Etats"]:
        if state in automate1["Etats_initiaux"]:
            startingState[0].append(state)

    for state in automate2["Etats"]:
        if state in automate2["Etats_initiaux"]:
            startingState[1].append(state)
    
    existingSet.append(startingState) #add as first set

    for Set in existingSet:
        transitions = calculLineProduct(Set, alphabet, automate1, automate2)
        newAutomateBP.append( (Set, transitions) )
        
        for key in transitions:
            
            #add any new set generated that is not a void aka [ [], [] ]
            if transitions[key] not in existingSet and (len(transitions[key][0]) > 0 or len(transitions[key][1]) > 0):
                existingSet.append(transitions[key])
    

    #creation of new automate
    newAutomate = {	
        "Etats": {},
		"Etats_initiaux": [],
		"Etats_finaux": [],
		"Nom": automate1["Nom"]+"x"+automate2["Nom"]
	}

    #creation of the state
    i = 0
    for Set in newAutomateBP:

        #test if the set (aka new state) is an end state in one automate.
        isEnd = False
        for state in Set[0][0]:
            if state in automate1["Etats_finaux"]:
                isEnd = True
                break
        
        if not isEnd:
            for state in Set[0][1]:
                if  state in automate2["Etats_finaux"]:
                    isEnd = True
                    break
        
        newAutomate["Etats"][f"e{i}"] = {}
        if i == 0:
            newAutomate["Etats_initiaux"].append(f"e{i}")
        if isEnd:
            newAutomate["Etats_finaux"].append(f"e{i}")
        i += 1
    
    #adding transition
    i = 0
    for Set in newAutomateBP:
        for key in alphabet:
            if Set[1][key] in existingSet:
                if key in newAutomate["Etats"][f"e{i}"]:
                    newAutomate["Etats"][f"e{i}"][key].append(f"e{existingSet.index(Set[1][key])}")
                else:
                    newAutomate["Etats"][f"e{i}"][key] = [f"e{existingSet.index(Set[1][key])}"]
        i += 1
    
    return newAutomate



def produit(liste, num_automate): # Choose the 2nd automaton, run the product() function, and add the result to the list
	num_automate2 = -1
	print("\n\n\n\n\n\n\n\n\n\n\n")
	print("Séléctionnez un deuxième AEF à comparer")
	liste, num_automate2 = file.loadAutomate(liste, num_automate2)
	automate = product(deepcopy(liste[num_automate]), deepcopy(liste[num_automate2]))
	automate["Nom"] = liste[num_automate]["Nom"] + "_*_" + liste[num_automate2]["Nom"]
	num_automate = len(liste)
	liste.append(automate)
	return liste, num_automate