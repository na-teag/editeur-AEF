# this file contains all the functions of th"e product of two automates 
"""  The functions are an adaption of the algorithm described here : 
        https://www.desmontils.net/emiage/Module209EMiage/c5/Ch5_10.htm (section 10.4)
"""
import data.structure as strct

"""" 
    automate={	
        "Etats": {},
		"Etats_initiaux": [],
		"Etats_finaux": [],
		"Nom": ""
	}



"""
def calculLineProduct():




def product (automate1, automate2):

    alphabet1 = strct.alphabet(automate1)
    alphabet2 =strct.alphabet(automate2)
    alphabet=alphabet1+alphabet2

    existingSet = [] #list of existing set of state
    newAutomateBP = [] #list of tuple (set of state, {"key":set of state for the key,...}). Make the blueprint for the new automate


     #each set will be structured as [ [automate1 states], [automate2 states] ], the sepration make sure that sere is no name conflict.

    #collect the starting state of each one.
    startingState = [[],[]]

            