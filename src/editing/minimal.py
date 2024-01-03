# this file contains all funcions to change an automate into a minimal one 

import data.structure as strct 

def isMinimal(automate):
    
    
    
    return True


def MooreMinimal (startBilan, automate) : 
    """  
    ### DESCRIPTION : 
    this function is an adaption of the Moore algorithm : it calculates a new bilan from a starting bilan. 
    It recurcively calls itself until the starting bilan is the same as the new one.  
     
    

    ### Return :
        Dictionnary for wich each state as for a key in the alphabet the id referening the state it transtion to with the key.   
    """
    result= {}

    automate = {
        "Alphabet": strct.alphabet(automate), 
        "Etats":{},
        "Etats_initiaux": [],
        "Etats_finaux": []
    }
    alphabet=strct.alphabet(automate)
    #add start bilan to the final result table
    for state in startBilan:
        result[state]=list(startBilan[state])

    for state in result : 
        for i in range(0,len(alphabet)):
            result[state].append(result[automate["Etats"][state]["Alphabet"[i][0][0]]])

    #Count different arrangement and give them an unique ID. If already exist give it the corresponding ID
    bilan={}
    alreadyAddedArrangement = []
    i=0
    for state in result:
        if result[state] not in alreadyAddedArrangement:
            bilan[state] = [i]
            alreadyAddedArrangement.append(result[state])
            i+=1
        else:
            bilan[state] = [alreadyAddedArrangement.index(result[state])]

    if bilan == startBilan:
        return result
    else:
        return MooreMinimal(bilan,automate)




def toMinimal(automate):
    """ 

    ### Description
    Create an Automate being the minimalistic version of the input automate.


    ### Return:
        New minimal automate.
    
    """
    #Create the bilan 
    startBilan={}
    for state in automate["Etats"] : 
        startBilan[state]=[int(state not in automate["Etats_finaux"])]
    
    minimalisedMap = MooreMinimal(startBilan,automate)

    #create a table of reference between and id and a state 
    idToState={}
    for state in minimalisedMap:
        if int(minimalisedMap[state][0]) not in idToState:
            idToState[int(minimalisedMap[state][0])] = state

    #creation of the new automate 
    i=-1
    automate["Etats"] = {}
    for state in minimalisedMap:
        if minimalisedMap[state][0] > i:
            i+=1
            automate["Etats"][state] = {}
            for key in range(0, len(automate["Alphabet"])):
                automate["Etats"][state][automate["Alphabet"][key]] = [idToState[minimalisedMap[state][key+1]]]
        else:
            if state in automate["Etats_initiaux"]: automate["Etats_initiaux"].remove(state)
            if state in automate["Etats_finaux"]: automate["Etats_finaux"].remove(state)


    return automate

