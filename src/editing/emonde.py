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

    for etat in automate["Etats"]:
        if etat not in automate["Etats_finaux"] and automate["Etats"][etat] == {}:
            print("L'automate n'est pas émondé")
            return False

    print("L'automate est émondé")
    return True




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
    etats_accessibles = set(etats_initiaux)

    for etat_initial in etats_initiaux:
        dfs(etat_initial)

    etats_a_supprimer = list(set(automate["Etats"].keys()) - etats_accessibles - set(automate["Etats_finaux"]))

    for etat in etats_a_supprimer:
        if etat in automate["Etats"]:
            del automate["Etats"][etat]

    automate["Etats_initiaux"] = list(etats_initiaux.intersection(etats_accessibles))
    automate["Etats_finaux"] = list(set(automate["Etats_finaux"]).intersection(etats_accessibles))

    if len(etats_a_supprimer) > 0:
        print("L'automate a été rendu émondé.")
    else:
        print("L'automate était déjà émondé.")

    return automate


def emonde(liste, num_automate):
    automate = liste[num_automate]
    automatee = rendre_emonde(deepcopy(automate))
    automatee["Nom"] += "_emonde"
    num_automate = len(liste)
    liste.append(automatee)
    return liste, num_automate
