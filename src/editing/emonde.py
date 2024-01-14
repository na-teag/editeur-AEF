from copy import deepcopy 

def est_emonde(automate): # verify if the automate is pruned
    reachable_states = set()

    def dfs(etat_actuel): # traverse the automate and mark reachable states
        nonlocal reachable_states
        reachable_states.add(etat_actuel)

        for etats_suivants in automate["Etats"][etat_actuel].values():
            for etat_suivant in etats_suivants:
                if etat_suivant not in reachable_states:
                    dfs(etat_suivant)

    for etat_initial in automate["Etats_initiaux"]:
        dfs(etat_initial)
    etats_co_accessibles = co_accessible(automate)
    
    if reachable_states.intersection(etats_co_accessibles) != set(automate["Etats"].keys()):
        print("L'automate n'est pas émondé")
        return False

    print("L'automate est émondé")
    return True



def path(automate, etat, chemin, co_accessibles): # traverse the automate and mark states leading to a final state
    if etat in co_accessibles:
        return []
    else:
        chemin.append(etat)
    for transition, etats_suivants in automate["Etats"][etat].items():
        for etat_suivant in etats_suivants:
            if etat_suivant in co_accessibles:
                return chemin
            if etat_suivant not in chemin:
                result = path(automate, etat_suivant, chemin.copy(), co_accessibles)
                if result:
                    return result
    return []



def co_accessible(automate): # checking which states can lead to a final state
    co_accessibles = automate["Etats_finaux"]
    for etat in list(set(automate["Etats"]) - set(co_accessibles)):
        co_accessibles += path(automate, etat, [], co_accessibles)
    return list(set(co_accessibles))






def rendre_emonde(automate):
    def dfs(etat):
        nonlocal etats_accessibles
        transitions = automate["Etats"].get(etat, {})
        for etats_suivants in transitions.values():
            for etat_suivant in etats_suivants:
                if etat_suivant not in etats_accessibles:
                    etats_accessibles.add(etat_suivant)
                    dfs(etat_suivant)


    etats_initiaux = set(automate["Etats_initiaux"])
    etats_finaux = set(automate["Etats_finaux"])
    etats_accessibles = set(etats_initiaux)

    for etat_initial in etats_initiaux:
        dfs(etat_initial)

    etats_co_accessibles = co_accessible(automate)

    etats_a_supprimer = set(automate["Etats"].keys()) - etats_accessibles.intersection(etats_co_accessibles)
    etats_a_consever = set(automate["Etats"].keys()) - etats_a_supprimer
    etats_a_supprimer = list(etats_a_supprimer)
    etats_a_consever = list(etats_a_consever)

    liste_transition = []
    for etat in etats_a_supprimer:
        if etat in automate["Etats"]:
            del automate["Etats"][etat] # delete the state
        for etat1 in automate["Etats"].keys():
            for transitions, etats_suivants in automate["Etats"][etat1].items():
                for transition in transitions:
                    if etat in automate["Etats"][etat1][transition]:
                        automate["Etats"][etat1][transition].remove(etat) # delete the transitions to the state
                        liste_transition += transition
            for transition in liste_transition:
                if automate["Etats"][etat1][transition] == []:
                    del automate["Etats"][etat1][transition]
            liste_transition = []


    automate["Etats_initiaux"] = list(etats_initiaux.intersection(etats_a_consever))
    automate["Etats_finaux"] = list(etats_finaux.intersection(etats_a_consever))

    if automate["Etats"].keys() == {}:
        print("L'automate émondé est un automate vide")
        return None
    else:
        if len(etats_a_supprimer) > 0:
            print("L'automate a été rendu émondé.")
        else:
            print("L'automate était déjà émondé.")

    return automate







def emonde(liste, num_automate): # call the function, with a copy of the  automaton, then add and select the new one
    automate = liste[num_automate]
    automatee = rendre_emonde(deepcopy(automate))
    if automatee != None:
        automatee["Nom"] += "_emonde"
        num_automate = len(liste)
        liste.append(automatee)
    return liste, num_automate
