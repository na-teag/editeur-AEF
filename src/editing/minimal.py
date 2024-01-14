# this file contains all funcions to change an automate into a minimal one 

import data.structure as strct 
from copy import deepcopy

def MooreMinimal(startBilan: dict, automate: dict) -> dict:
    """
    ### Description
    Calulate an new bilan from a starting bilan. Recurcively call until the starting bilna is the same as the new one.
    
    ### Return:
        Dictionnary for wich each state as for a key in the alphabet the id referening the state it transtion to with the key.
    
    """
    alphabet =  strct.alphabet(automate)
    outcome = {}

    #add start bilan to the final outcome table
    for state in startBilan:
        outcome[state] = list(startBilan[state])
    

    for state in outcome:
        for key in alphabet:
            if key in automate["Etats"][state]:
                outcome[state].append(outcome[automate["Etats"][state][key][0]][0])

    #count different arrangement and give them an unique ID. If already exist give it the corresponding ID
    bilan = {}
    alreadyAddedArrangement = []
    i=0
    for state in outcome:
        if outcome[state] not in alreadyAddedArrangement:
            bilan[state] = [i]
            alreadyAddedArrangement.append(outcome[state])
            i+=1
        else:
            bilan[state] = [alreadyAddedArrangement.index(outcome[state])]

    if bilan == startBilan:
        return outcome
    else:
        return MooreMinimal(bilan, automate)

def toMinimal(automate: dict):
    """
    ### Description
    Create an Automate being the minimalistic version of the input automate.

    ### Return:
        New minimal automate.
    
    """

    #create the bilan
    startBilan = {}
    for state in automate["Etats"]:
        startBilan[state] = [int(state in automate["Etats_finaux"])]

    minimalisedMap = MooreMinimal(startBilan, automate)

    #create a table of reference between an id and a state
    idToState = {}
    for state in minimalisedMap:
        if int(minimalisedMap[state][0]) not in idToState:
            idToState[int(minimalisedMap[state][0])] = state


    #creation of the new Automate
    newAutomate = {	
        "Etats": {},
		"Etats_initiaux": [],
		"Etats_finaux": [],
		"Nom": automate["Nom"]+"_minimal"
	}

    #creating states
    for i in idToState:
        newAutomate["Etats"][idToState[i]] = {}
        if idToState[i] in automate["Etats_finaux"]:
            newAutomate["Etats_finaux"].append(idToState[i])
        if idToState[i] in automate["Etats_initiaux"]:
            newAutomate["Etats_initiaux"].append(idToState[i])

    #creating transition
    i = -1
    alphabet = strct.alphabet(automate)
    for state in minimalisedMap:
        if minimalisedMap[state][0] > i:
            i+=1
            for key in range(0, len(alphabet)):
                newAutomate["Etats"][state][alphabet[key]] = idToState[minimalisedMap[state][key+1]]
    
    return newAutomate



def minimal(liste, num_automate): # call the function, with a copy of the  automaton, then add and select the new one

    automate = liste[num_automate]
    automatee = toMinimal(deepcopy(automate))
    automatee["Nom"] += "_minimal"
    num_automate = len(liste)
    liste.append(automatee)
    return liste, num_automate