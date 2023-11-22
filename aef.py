#definition de l'automate 
automate ={
    "Etats": {
        "Etat0": {"Transition1": "Etat1", "Transition2": "Etat0"},
        "Etat1": {"Transition3": "Etat0", "Transition4": "Etat1"}
    },
    "EtatsInitiaux": ["Etat0"],
    "EtatsFinaux": ["Etat1"]
}
