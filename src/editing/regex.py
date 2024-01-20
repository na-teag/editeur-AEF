import re
import data.structure as strct
'''
automate = {
	"Etats": {
		"q0": {"a": ["q0"], "b": ["q1"]},
		"q1": {"b": ["q1"], "a": ["q0"], "c": ["q0"]}
	},
	"Etats_initiaux": ["q0"],
	"Etats_finaux": ["q1", "q0"],
	"Nom" : "test"
}
'''

def showEquations(equations):
	for etat, equation in equations.items():
		print(f'{etat} : {equation}')

def getEquations(automate): # get the equations of the FA
	equations = {}
	for etat in automate["Etats"].keys():
		equations[etat] = []
		for transition, etats_suivants in automate["Etats"][etat].items():
			for etat_suivant in etats_suivants:
				relation = transition + "." + etat_suivant
				equations[etat].append(relation)
		if etat in automate["Etats_finaux"]:
			equations[etat].append("ε")
	return equations

def deleteUnused(equations): # delete the equations that are unnecessary (if a state has no other state leading to it)
	liste = []
	for etat in equations.keys():
		test=0
		for etat2, equation in equations.items():
			if(etat2 != etat):
				if etat in '.'.join(equation):
					test=1
		if(test==0 and etat not in etats_initiaux):
			liste.append(etat)
	#print(liste)
	for etat in liste:
		del equations[etat]
	return equations


def replace(equations): # replace states by their values in the equations, only if these states do not lead to themself (else, it's arden that must be used first)
	liste = []
	for etat, equation in equations.items():
		test=0
		for elem in equation:
			if etat in elem:
				test=1
		if(test == 0 and etat not in etats_initiaux):
			liste.append(etat)
	
	for etat in liste:
		dico_delete = {}
		dico_add = {}
		for etat2, equation in equations.items():
			dico_delete[etat2] = []
			dico_add[etat2] = []
			for elem in equation:
				if etat in elem:
					chaine = elem[:elem.index(etat)]
					dico_delete[etat2].append(equation.index(elem))
					for equation2 in equations[etat]:
						chaine2 = chaine + equation2
						dico_add[etat2].append(chaine2)
		for etat2 in dico_add:
			for elem in dico_add[etat2]:
				equations[etat2].append(elem)
		for etat2 in dico_delete:
			for elem in dico_delete[etat2]:
				del equations[etat2][elem]
		del equations[etat]
	return equations


def replace_initials(equations): # replace states by their values in the equations, but do not delete the initial ones because they are from initials states
	test = 0
	liste = []
	for etat, equation in equations.items():
		liste.append('.'.join(equation))
	for etat in equations.keys():
		if etat in '.'.join(liste):
			test = 1
			break
	i = 0
	max = 250
	while test and i<max:
		liste = []
		for etat, equation in equations.items():
			for elem in equation:
				for etat2 in equations.keys():
					if etat2 in elem:
						test2 = 1
						if(len(equations[etat2]) == 1):
							for etat3 in equations.keys():
									if etat3 in equations[etat2][0]:
										test2 = 0
							if test2:
								equations[etat][equations[etat].index(elem)] = equations[etat][equations[etat].index(elem)].replace(etat2, equations[etat2][0])

		for etat in equations.keys():
			if etat in '.'.join(liste):
				test = 1
				break
		i+=1
	if(i >= max):
		print("erreur, impossible de terminer la simplification\nrésultat actuel :")
		print("\n\n\n\n\n")
	return equations



def arden(equations): # lemme of Arden ( X = aX+B  =>  X = a*B)
	choice = []
	for etat, equation in equations.items():
		for elem in equation:
			if etat in elem and etat not in choice:
				choice.append(etat)
	#print(choice)
	if(len(choice) != 0): # erratum : limit to one execution of arden at a time
		choice = [choice[0]]
	for etat in choice:
		liste = []
		for elem in equations[etat]:
			if etat in elem:
				liste.append(equations[etat].index(elem))
		liste2 = []
		#print(liste)
		for elem in liste:
			liste2.append(equations[etat][elem][:-(len(etat)+1)])
		if(len(liste2) != 1): # if the * affects multiples values
			a_etoile = '(' + ' + '.join(liste2) + ')*'
		else:
			a_etoile = liste2[0] + "*" # if there is only one value, do not use the ()
		#print(a_etoile)
		for elem in liste2:
			del equations[etat][equations[etat].index(elem + '.' + etat)]
		#print(equations[etat])
		for elem in equations[etat]:
			equations[etat][equations[etat].index(elem)] = a_etoile + "." + elem
	return equations


def simplify(equations):
	#print(equations)
	for transition in alphabet:
		for etat, equation in equations.items():
			for elem in equation:
				index = equations[etat].index(elem)
				test = 1
				while(test == 1):
					test = 0

					new = re.sub(r'\*+', '*', equations[etat][index]) # replace a** by a*
					if(new != equations[etat][index]):
						test = 1
					equations[etat][index] = new

					new = re.sub(f"{transition}\*\.{transition}\*", f"{transition}*", equations[etat][index]) # replace a*.a* by a*
					if(new != equations[etat][index]):
						test = 1
					equations[etat][index] = new

					new = re.sub(f"{transition}\*\.{transition}(?!\*)", f"{transition}+", equations[etat][index]) # replace a*.a by a+
					if(new != equations[etat][index]):
						test = 1
					equations[etat][index] = new

					new = re.sub(f"{transition}\.{transition}\*", f"{transition}+", equations[etat][index]) # replace a.a* by a+
					if(new != equations[etat][index]):
						test = 1
					equations[etat][index] = new

					new = re.sub(f"{transition}\+\.ε", f"{transition}*", equations[etat][index]) # replace a+.ε by a*
					if(new != equations[etat][index]):
						test = 1
					equations[etat][index] = new

					new = re.sub(f"{transition}\*\.ε", f"{transition}*", equations[etat][index]) # replace a*.ε by a*
					if(new != equations[etat][index]):
						test = 1
					equations[etat][index] = new

					new = re.sub(f"{transition} \+ ε(?!\.)", f"{transition}*", equations[etat][index]) # replace a + ε by a*
					if(new != equations[etat][index]):
						test = 1
					equations[etat][index] = new

					new = re.sub(f"{transition}\.ε(?!\.)", f"{transition}", equations[etat][index]) # replace a.ε by a
					if(new != equations[etat][index]):
						test = 1
					equations[etat][index] = new
	return equations



def regex(automate): # calculates the regex expression (several initial states accepted)
	print("\033[2J") # clear the screen
	global alphabet
	alphabet = strct.alphabet(automate)
	global etats_initiaux
	etats_initiaux = automate["Etats_initiaux"]
	equations = getEquations(automate) # calculates the equations
	#showEquations(equations)
	#print("")
	equations = deleteUnused(equations) # deletes the useless equations
	#print("")
	#showEquations(equations)
	#print("")
	test = 1
	while test:
		if(len(equations) == len(etats_initiaux)):
			test = 0
		equations = replace(equations) # replace expression of a state by its value in other states
		#print("")
		#showEquations(equations)
		#print("")
		equations = arden(equations) # use arden theorem
		#print("")
		#showEquations(equations)
		#print("")
	equations = simplify(equations)
	#showEquations(equations)
	#print("")
	equations = replace_initials(equations)
	#print("")
	#showEquations(equations)
	#print("")
	equations = simplify(equations)
	#showEquations(equations)
	#print("")
	result = ""
	for etat, equation in equations.items():
		for elem in equation:
			print(equations[etat][equations[etat].index(elem)])
			result += equations[etat][equations[etat].index(elem)]
			if(list(equations.keys()).index(etat) != len(equations)-1 or equations[etat].index(elem) != len(equation)-1):
				print("+")
				result += "  +  "
	print("\n\n\n\n\n\n\n\n\n")
	return result


# ajouter regex et arden dans les tags github