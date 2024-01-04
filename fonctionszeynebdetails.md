1. initialize the final automate automateFinal 

- this automate has a new structure which includes : 
    - "Alphabet": Union of the alphabets of automate1 and automate2.
    - "Etats": A dictionary representing states in the new automaton.
    - "Etats_initiaux": An empty list for initial states.
    - "Etats_finaux": An empty list for final states.

2. Create State Mappings (oldToNew1 and oldToNew2):

- These two dictionaries (oldToNew1 and oldToNew2) will store mappings from the old state names to the corresponding new state names in automateFinal. This is necessary because when combining two automates, we need to ensure that the state names are unique across both automate.
* 

## Product of two FAs 
The functions in this file create a new automate as the outcome of the product of two automates. This algorithme is an adapation of the one explain here: https://www.desmontils.net/emiage/Module209EMiage/c5/Ch5_10.htm (section 10.4)
### Function calculLineProduct
### Function product
