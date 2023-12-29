# this file contains all the functions of th"e product of two automates 
"""  The functions are an adaption of the algorithm described here : 
        https://www.desmontils.net/emiage/Module209EMiage/c5/Ch5_10.htm (section 10.4)
"""
import data.structure as strct


def product (automate1, automate2):

    alphabet=list(set(automate1["Alphabet"]+automate2["Alphabet"]))
    #list of existing set of state
    existingSet = [] 
    #list of tuple (set of state, {"key":set of state for the key,...}). Make the blueprint for the new automate
    newAutomateBP = [] 

    #collect the starting state of each one.
    startingState = [[],[]]

    for state in automate1["Etats"] : 
        


