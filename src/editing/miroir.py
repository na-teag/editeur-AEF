from copy import deepcopy
"""
automate ={
	"Etats": {                                                      #exemple
	   "Etat0": {"Transition1": ["Etat0"], "Transition2": ["Etat1"]},
	   "Etat1": {"Transition1": ["Etat1"], "Transition2": ["Etat1","Etat0"]},
   },
   "Etats_initiaux":{"Etat0"},
   "Etats_finaux": {"Etat1"},
}"""

def automatevide(automate):                                         #create a disctinct copy of a dictionnary (for the mirror
	automatem = deepcopy(automate)                                  #function)
	for etat in automatem['Etats']:                                 #empty the dictionnary
		automatem['Etats'][etat]= {}
	automatem['Etats_finaux'] = {}                                  #deleting the status from the new dictionnary
	automatem['Etats_initiaux'] = {}
	return automatem


def miroir(automate,automatem):                                     #function creating a distinct mirror

	for e in automate['Etats']:                                     #looking at states
		for t in automate['Etats'][e]:                              #looking at transition
			n=automate['Etats'][e][t]                               #taking target state of the transition t
			#print(n)
			for c in n:
				if t not in automatem['Etats'][c]:
					automatem['Etats'][c][t]=[]
				automatem['Etats'][c][t].append(e)                  #sending mirror transition to the mirror automaton

	automatem['Etats_finaux'] = automate['Etats_initiaux']          #giving mirror automaton opposite initial and final state
	automatem['Etats_initiaux'] = automate['Etats_finaux']
	return automatem

def miroirf(liste, num_automate): # call the function, with a copy of the  automaton, then add and select the new one
	automate = liste[num_automate]
	automatem = automatevide(automate)
	automatem = miroir(automate,automatem)

	automatem["Nom"] += "_miroir"
	num_automate = len(liste)
	liste.append(deepcopy(automatem))
	return liste, num_automate


