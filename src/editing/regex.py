import re
'''
n = 2
liste_etat_finaux = ["2","1"]
liste_etat_initiaux = ["1"]
'''

automate = {
	"Etats": {
		"q0": {"a": ["q0","q1"]},
		"q1": {"c": ["q0","q2"], "d": ["q1"]},
		"q2": {"a": ["q0"], "b": ["q1"]},
		"q3": {"b": ["q2"]}
	},
	"Etats_initiaux": ["q0"],
	"Etats_finaux": ["q2"],
	"Nom" : "test"
}

def creer_matrice(nbr):
	matrice = [['NULL' for _ in range(nbr)] for _ in range(nbr)]
	return matrice

def afficher(mat):
	for liste in mat:
		print(liste)
	print("\n")

def corriger_matrice(mat):
	for liste in mat:
		for i in range(len(liste)):
			liste[i] = re.sub(r'\++', '+', liste[i]) # replace +++++etc by only one +
			liste[i] = re.sub(r'\*+', '*', liste[i]) # same for *
			liste[i] = liste[i].replace('+*', '*') # replace "+*" by "*"
			liste[i] = liste[i].replace('*+', '*') # replace "*+" by "*"


def calculer_matrice(automate):
	liste = list(automate["Etats"].keys())
	mat = creer_matrice(len(automate["Etats"].keys()))

	for etat in liste:
		for etat2 in liste:
			for transition, etat_suivant in automate["Etats"][etat].items():
				if(etat2 in etat_suivant):
					if(mat[liste.index(etat)][liste.index(etat2)] == 'NULL'):
						mat[liste.index(etat)][liste.index(etat2)] = transition
					else:
						mat[liste.index(etat)][liste.index(etat2)] += ('|' + transition)
	return liste, mat



def result(mat, n, liste_etat_initiaux, liste_etat_finaux, liste):
	for k in range(0, n):
		for p in range(0, n):
			for q in range(0, n):
				if(not (mat[p][k] == "NULL" and mat[k][k] == "NULL" and mat[k][q] == "NULL")):
					if(mat[p][q] == mat[p][k] and mat[p][k] == mat[k][k] and mat[k][k] == mat[k][q]):
						if(mat[p][q] != "NULL"):
							mat[p][q] = mat[p][q] + "+"
					elif(mat[p][k] == mat[k][k] and mat[k][k] == mat[k][q]):
						mat[p][q] = "(" + mat[p][q] + " U " + mat[k][q] + "+ )"
					elif(mat[p][k] == mat[k][k]):
						if(mat[k][k] == "NULL"):
							if(mat[p][q] != mat[k][q]):
								mat[p][q] = "(" + mat[p][q] + " U " + mat[k][q] + ")"
						elif(mat[k][q] == "NULL"):
							if(mat[p][q] != "NULL"):
								mat[p][q] = "(" + mat[p][q] + " U " + mat[k][k] + "+ )"
							else:
								mat[p][q] = mat[k][k] + "*"
						else:
							mat[p][q] = "(" + mat[p][q] + " U " + mat[k][k] + "+ " + mat[k][q] + ")"
					elif(mat[k][k] == mat[k][q]):
						if(mat[p][k] == "NULL"):
							if(mat[p][q] != "NULL"):
								mat[p][q] = "(" + mat[p][q] + " U " + mat[k][k] + "+ )"
							else:
								mat[p][q] = mat[k][k] + "*"
						elif(mat[k][k] == "NULL"):
							if(mat[p][q] != mat[p][k]):
								mat[p][q] = "(" + mat[p][q] + " U " + mat[p][k] + ")"
						else:
							mat[p][q] = "(" + mat[p][q] + " U " + mat[p][k] + " " + mat[k][k] + "+ )"
					else:
						if(mat[p][k] == "NULL"):
							mat[p][q] = "(" + mat[p][q] + " U " + mat[k][k] + "* " + mat[k][q] + ")"
						elif(mat[k][k] == "NULL"):
							mat[p][q] = "(" + mat[p][q] + " U " + mat[p][k] +  " " + mat[k][q] + ")"
						elif(mat[k][q] == "NULL"):
							mat[p][q] = "(" + mat[p][q] + " U " + mat[p][k] + " " + mat[k][k] + "*" + ")"
						else:
							mat[p][q] = "(" + mat[p][q] + " U " + mat[p][k] + " " + mat[k][k] + "* " + mat[k][q] + ")"
				
		#afficher(mat)
	res = ""
	corriger_matrice(mat)
	for p in liste_etat_initiaux:
		for q in liste_etat_finaux:
			if(p == q):
				mat[liste.index(p)][liste.index(p)] = "(ɛ U " + mat[liste.index(p)][liste.index(p)] + ")"
			if(res != ""):
				res = "(" + res + " U " + mat[liste.index(p)][liste.index(p)] + ")"
			else:
				res = mat[liste.index(p)][liste.index(p)]
	
	#afficher(mat)
	return res

'''
liste = ["1","2"]
mat = [["a","b"],["NULL","b"]] # NULL
res = result(mat, len(liste), liste_etat_initiaux, liste_etat_finaux, liste)
print(res)
'''

def regex(automate):
	liste, mat = calculer_matrice(automate)
	print("\n\n\n\n\n\n\n\n\n\n")
	afficher(mat)
	print("\n\n\n")
	res = result(mat, len(liste), automate["Etats_initiaux"], automate["Etats_finaux"], liste)
	print(res)
	return res

#regex(automate)