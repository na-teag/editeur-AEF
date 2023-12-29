# Create an automate from the concatenation of two automates 

import data.structure as strct


def concat (automate1, automate2) :
    # create new automate 
    automateFinal= {
        "Alphabet": list(set(automate1["Alphabet"]+automate2["Alphabet"])), 
        "Etats":{},
        "Etats_initiaux": [],
        "Etats_finaux": []
    }

    i=0
     
    for state in automate1["Etats"] : 
        automateFinal[]
