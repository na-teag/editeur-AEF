from copy import deepcopy

automate ={
    "Etats": {                                                      #exemple
       "Etat0": {},
       "Etat1": {},
   },
   "Etats_initiaux":{},
   "Etats_finaux": {},
}

def automatevide(automate):                                         #create a disctinct copy of a dictionnary (for the mirror
    automatem = deepcopy(automate)                                  #function)
    for etat in automatem['Etats']:                                 #empty the dictionnary
        automatem['Etats'][etat]= {}
    automatem['Etats_finaux'] = {}                                  #deleting the status from the new dictionnary
    automatem['Etats_initiaux'] = {}
    return automatem


def miroir(automate):                                               #function creating a distinct mirror

    for e in automate['Etats']:                                     #looking at states
        for t in automate['Etats'][e]:                              #looking at transition
            n=automate['Etats'][e][t]                               #taking target state of the transition t
            automatem['Etats'][n[0]][t]=e                           #sending mirror transition to the mirror automaton

    automatem['Etats_finaux']=automate['Etats_initiaux']            #giving mirror automaton opposite initial and final state
    automatem['Etats_initiaux'] = automate['Etats_finaux']




automatem = automatevide(automate)
miroir(automate)