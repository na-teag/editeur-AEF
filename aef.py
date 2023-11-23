#!!!RQ on peut séparer le code en fichiers par exemple
"""
 les fonctions our enregistrer dans un fichier ou importer d'un fichier dans un autre dossier/fichier
 Les fonctions  pour modifier l'automate (ajouter,supprimer..) dans un dossier/fichier
 le main juste l'interface/menu 
 après ça reste une proposition 
"""
#---------------FUNCTIONS TO CREATE AUTOMATE---------------

#Function that takes an input as string and transforms it to an alphabet and removes duplicated values
"""
>>> createAlphabet("a b c d e f e")
    ["a", "b", "c", "d", "e", "f"]

"""
def createAlphabet(input) : 
    alphabet=list(set(input.split())) #split the str on spaces and removes duplicate values by passing list to set 
    return alphabet
#Function to create a new automate: takes a alphabet(list) : the alphabet of the automate and returns Dictionnary with all the data set to default value

def createAutomate(alphabet ) : 
    newAutomate = {
        "alphabet" : alphabet,
        "states" : [] #maybe name it element ??
    }

    return newAutomate

#Create a new state that can be add to an automate and returns Dictionnary with all the data set to default value for the corresponding automate. 
"""state : list of all the state constant of the element. Default is no state.
"""
def createState(alphabet, state) : 
    transitionDefault={}
    for key in alphabet : 
        transitionDefault[key] =None
    
    newState = {   #maybe name it element ( element= state+transition) ??
        "state":state,
        "transition":transitionDefault
    }

    return newState

#--------FUNCTIONS TO EDIT THE AUTOMATE(ADD/DELETE ELEMENTS/TRANSITIONS)---------------------------------
#j'ai pas pris en compte le truc de l'epsilone ou jsp quoi pas trop compris ce concept faut que je m'y penche 

#function to add an element(states) to an automate
def addElementToAutomate(automate,element) :
    automate["element"].append(element)

#function to delete an element from the automate
def deleteElementFromAutomate(automate,element) :
    automate["element"].remove(element) 

#function to delete all the elements from the automate??? (A faire ou pas?)
#function to add a transition for a key from an element source to an other element (target)
"""
    elementSource= element (as a dictionnary) to which we add the transition
    elementTarget = element (as a dictionnary) to which the transition goes to 
    key : the key of the transition (str?)

"""
def addTransition(elementSource, key, elementTarget) :

    elementSource["transition"][key] = elementTarget

#function to delete the transition ?? (pas sure de mon code) 
def delTransition(elementSource, key) :

    elementSource["transition"][key] = None
