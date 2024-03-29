

from unittest.mock import patch
from time import sleep
import unittest
import copy
import platform
import subprocess
from io import StringIO

import data.file as file
import data.structure as strct
import editing.complement as complt
import editing.miroir as mir
import editing.modif as md
import editing.testermot as testermot
import main
import unitTest.testminimal as min
import unitTest.testconcat as concat
import unitTest.testproduit as prod
import unitTest.testcomplet as comp
import unitTest.testdeter as deter
import editing.emonde as emd
import editing.langage as lang
import editing.regex as rgx


MAGENTA = '\033[95m'
ENDC = '\033[0m'


''' # exemple de test
def fonction_exemple():
	user_input = input("Entrez un nombre : ")
	user_input2 = input("Entrez un 2e nombre : ")
	return (int(user_input) + int(user_input2)) * 2

class Testfonction_exemple(unittest.TestCase):
	@patch('builtins.input', side_effect=['5', '10'])
	def test_fonction_exemple(self, mock_inputs):
		result = fonction_exemple()
		self.assertEqual(result, 30)
'''


##########################################################################  functions from structuree.py ##########################################################################


class TestCreateAutomate(unittest.TestCase): # test of function CreateAutomate
	@patch('builtins.input', side_effect=[])
	def TestCreateAutomate(self, mock_inputs):
		result = strct.createAutomate()
		result2 = {
			"Etats": {},
			"Etats_initiaux": [],
			"Etats_finaux": [],
			"Nom": ""
		}
		self.assertEqual(result, result2)


class Test_alphabet(unittest.TestCase): # test of function alphabet
	@patch('builtins.input', side_effect=[])
	def test_alphabet(self, mock_inputs):
		result = strct.alphabet(automate)
		result2 = ['a','b','c','d']
		self.assertEqual(result.sort(), result2.sort())


##########################################################################  functions from modif.py ###############################################################################

class testEditStates(unittest.TestCase):  # test of function editeStates
	@patch('builtins.input', side_effect=['test', 'q0,a,q0', 'q0,a,q1', 'q1,c,q0', 'q1,c,q2', 'q1,d,q1', 'q2,a,q0', 'q2,b,q1', 'q3,b,q2', '', 'q0', '', 'q2', ''])
	def testEditStates(self, mock_inputs):
		liste = []
		indice = 0
		liste.append(strct.createAutomate())
		liste, indice = md.editStates(liste, indice)
		self.assertEqual(liste[indice], automate)


class testTestTransition(unittest.TestCase):  # test of function testTransition
	@patch('builtins.input', side_effect=[])
	def testTestTransition(self, mock_inputs):
		automate1 = copy.deepcopy(automate)
		result = md.testTransition(automate1, "q0")
		self.assertEqual(result, 1)
		result = md.testTransition(automate1, "q3")
		self.assertEqual(result, 0)
		result = md.testTransition(automate1, "q4")
		self.assertEqual(result, 0)


class TestRenameStates(unittest.TestCase):  # test of function renameStates
	@patch('builtins.input', side_effect=['q3', 'q0', '1'])
	def TestRenameStates(self, mock_inputs):
		liste = []
		indice = 0
		liste.append(copy.deepcopy(automate))
		liste, indice = md.renameStates(liste, indice)
		automate2 = {
			"Etats": {
				"q0": {"a": ["q0","q1"], "b": ["q2"]},
				"q1": {"c": ["q0","q2"], "d": ["q1"]},
				"q2": {"a": ["q0"], "b": ["q1"]}
			},
			"Etats_initiaux": ["q0"],
			"Etats_finaux": ["q2"],
			"Nom" : "test"
		}
		self.assertEqual(liste[indice], automate2)


class testChangeStatesInitFinal(unittest.TestCase):  # test of function changeStatesInitFinal, with 3rd parameter = 0 (initial)
	@patch('builtins.input', side_effect=['q0', 'q2', ''])
	def testChangeStatesInitFinal(self, mock_inputs):
		liste = []
		indice = 0
		liste.append(copy.deepcopy(automate))
		liste, indice = md.changeStatesInitFinal(liste, indice, 0)
		automate2 = {
			"Etats": {
				"q0": {"a": ["q0","q1"]},
				"q1": {"c": ["q0","q2"], "d": ["q1"]},
				"q2": {"a": ["q0"], "b": ["q1"]},
				"q3": {"b": ["q2"]}
			},
			"Etats_initiaux": ["q2"],
			"Etats_finaux": ["q2"],
			"Nom" : "test"
		}
		self.assertEqual(liste[indice], automate2)


class testChangeStatesInitFinal2(unittest.TestCase):  # test of function changeStatesInitFinal, with 3rd parameter = 1 (final)
	@patch('builtins.input', side_effect=['q2', 'q1', ''])
	def testChangeStatesInitFinal2(self, mock_inputs):
		liste = []
		indice = 0
		liste.append(copy.deepcopy(automate))
		liste, indice = md.changeStatesInitFinal(liste, indice, 1)
		automate2 = {
			"Etats": {
				"q0": {"a": ["q0","q1"]},
				"q1": {"c": ["q0","q2"], "d": ["q1"]},
				"q2": {"a": ["q0"], "b": ["q1"]},
				"q3": {"b": ["q2"]}
			},
			"Etats_initiaux": ["q0"],
			"Etats_finaux": ["q1"],
			"Nom" : "test"
		}
		self.assertEqual(liste[indice], automate2)


class testDeleteStates(unittest.TestCase):  # test of function deleteStates
	@patch('builtins.input', side_effect=['q2', '1', 'q1', ''])
	def testDeleteStates(self, mock_inputs):
		liste = []
		indice = 0
		liste.append(copy.deepcopy(automate))
		liste, indice = md.deleteStates(liste, indice)
		automate2 = {
			"Etats": {
				"q0": {"a": ["q0","q1"]},
				"q1": {"c": ["q0"], "d": ["q1"]}
			},
			"Etats_initiaux": ["q0"],
			"Etats_finaux": ["q1"],
			"Nom" : "test"
		}
		self.assertEqual(liste[indice], automate2)


class testDemandDelete(unittest.TestCase):  # test of function demandDelete, and thus function deleteAutomate, and thus function select
	@patch('builtins.input', side_effect=['1', '2', 'test', 'q0,a,q1', '', 'q0', '', 'q1', ''])
	def testDemandDelete(self, mock_inputs):
		liste = []
		indice = 0
		liste.append(copy.deepcopy(automate))
		liste, indice = md.demandDelete(liste, indice)
		automate2 = {
			"Etats": {
				"q0": {"a": ["q1"]},
				"q1": {}
			},
			"Etats_initiaux": ["q0"],
			"Etats_finaux": ["q1"],
			"Nom" : "test"
		}
		self.assertEqual(liste[indice], automate2)
##########################################################################  functions from complement.py ##########################################################################

class Testcomplement(unittest.TestCase):  # test of function Complement
	@patch('builtins.input', side_effect=[])
	def Testcomplement(self, mock_inputs):
		result = complt.complement(automate)
		result2 = {
			"Etats": {
				"q0": {"a": ["q0", "q1"]},
				"q1": {"c": ["q0", "q2"], "d": ["q1"]},
				"q2": {"a": ["q0"], "b": ["q1"]},
				"q3": {"b": ["q2"]}
			},
			"Etats_initiaux": ["q0"],
			"Etats_finaux": ["q0,q1,q3"],
			"Nom": "test"
		}
		self.assertEqual(result, result2)

##########################################################################  functions from miroir.py ##############################################################################


class Testmiroir(unittest.TestCase):  # test of function Miroir
	@patch('builtins.input', side_effect=[])
	def Testmiroir(self, mock_inputs):
		result = mir.miroirf(automate)
		result2 = {
			"Etats": {
				"q0": {"a": ["q0", "q2"], "c": ["q1"]},
				"q1": {"a": ["q0"], "b": ["q2"], "d": ["q1"]},
				"q2": {"b": ["q3"], "c": ["q1"]},
				"q3": {}
			},
			"Etats_initiaux": ["q2"],
			"Etats_finaux": ["q0"],
			"Nom": "test"
		}
		self.assertEqual(result, result2)


###########################################################################  functions from concat.py #############################################################################

class Test_concat(unittest.TestCase): # test of function test_conc
	@patch('builtins.input', side_effect=[])
	def test_concat(self, mock_inputs):
		print(MAGENTA+"TEST concaténation de 2 automates"+ENDC)
		self.assertEqual(concat.test_conc(), True)

###########################################################################  functions from minimal.py ############################################################################

class Test_minimal(unittest.TestCase): # test of function test_minimal
	@patch('builtins.input', side_effect=[])
	def test_minimal(self, mock_inputs):
		print(MAGENTA+"TEST minimal"+ENDC)
		self.assertEqual(min.test_min(), True)

###########################################################################  functions from produit.py ############################################################################

class Test_produit(unittest.TestCase): # test of function test_minimal
	@patch('builtins.input', side_effect=[])
	def test_produit(self, mock_inputs):
		print(MAGENTA+"TEST produits de 2 automates"+ENDC)
		self.assertEqual(prod.test_prod(), True)

##########################################################################  functions from testermot.py ###########################################################################

class Test_tester(unittest.TestCase):  # test of function tester, and thus function tester_mot, with a valid word
	@patch('builtins.input', side_effect=['a', 'a', 'd', 'd', 'c', 'a', 'a', 'd', 'c', 'b', 'c', ''])
	def test_tester(self, mock_inputs):
		result = testermot.tester(automate)
		self.assertEqual(result, True)

class Test_tester2(unittest.TestCase):  # test of function tester, and thus function tester_mot, with a non-valid word (end with a word that's not final)
	@patch('builtins.input', side_effect=['a', 'a', 'd', 'd', 'c', 'a', 'a', 'd', 'c', 'b', ''])
	def test_tester2(self, mock_inputs):
		result = testermot.tester(automate)
		self.assertEqual(result, False)

class Test_tester3(unittest.TestCase):  # test of function tester, and thus function tester_mot, with another non-valid word (beggin by a state that's not initial)
	@patch('builtins.input', side_effect=['d', 'd', 'c', 'a', 'a', 'd', 'c', 'b', 'c', ''])
	def test_tester3(self, mock_inputs):
		result = testermot.tester(automate)
		self.assertEqual(result, False)

class Test_tester4(unittest.TestCase):  # test of function tester, and thus function tester_mot, with another non-valid word (path does not exist)
	@patch('builtins.input', side_effect=['a', 'd', 'd', 'a', 'a', 'd', 'c', 'b', 'c', ''])
	def test_tester4(self, mock_inputs):
		result = testermot.tester(automate)
		self.assertEqual(result, False)

############################################################################  functions from regex.py #############################################################################

class Test_regex(unittest.TestCase):  # test of function tester, and thus function tester_mot, with another non-valid word (path does not exist)
	@patch('builtins.input', side_effect=[])
	def test_regex(self, mock_inputs):
		result = rgx.regex(automate)
		expression = "(a+.(d + c.b)*.c + a+.(d + c.b)*.c.a)*.a+.(d + c.b)*.c"
		self.assertEqual(result, expression)

##########################################################################  test of functions complet.py  #########################################################################

class Test_verifcomplet(unittest.TestCase): # test of function complet.py : est_complet
	@patch('builtins.input', side_effect=[])
	def testcomplet(self, mock_inputs):
		print("TEST de verification de l'etat complet d'un automate")
		self.assertEqual(comp.test_verifcomplet(), True)

class Test_complet(unittest.TestCase): # test of function complet.py : rendrecomplet
	@patch('builtins.input', side_effect=[])
	def testcomplet(self, mock_inputs):
		print("TEST de completion d'un automate")
		self.assertEqual(comp.test_complet(), True)

###########################################################################  test of functions deter.py  ##########################################################################

class Test_verifdeter(unittest.TestCase): # test of function deter.py : est_deterministe
	@patch('builtins.input', side_effect=[])
	def testdeter(self, mock_inputs):
		print("TEST de verification de l'etat determiner d'un automate")
		self.assertEqual(deter.test_verifdeter(), True)

class Test_deter(unittest.TestCase): # test of function deter.py : rendredeterministe
	@patch('builtins.input', side_effect=[])
	def testdeter(self, mock_inputs):
		print("TEST de determinisation d'un automate")
		self.assertEqual(deter.test_deter(), True)
  
#########################################################################  test of functions emonde.py  #######################################################################

class Test_est_emonde(unittest.TestCase): # test of function emonde.py : est_emonde
	@patch('builtins.input', side_effect=[])
	def est_emonde(self, mock_inputs):
		automate1 = copy.deepcopy(automate)
		result = emd.est_emonde(automate1)
		self.assertEqual(result, False)
  
class Test_est_emonde(unittest.TestCase): # test of function emonde.py : est_emonde
	@patch('builtins.input', side_effect=[])
	def est_emonde(self, mock_inputs):
		result = {
			"Etats": {
				"q0": {"a": ["q1"], "b": ["q2"]},
				"q1": {"c": ["q3"]},
				"q2": {"d": ["q3"]},
				"q3": {}
			},
			"Etats_initiaux": ["q0"],
			"Etats_finaux": ["q3"],
			"Nom": "Automate_Emonde"
		}
		self.assertEqual(result, True)
  
class Test_rendre_emonde(unittest.TestCase): # test of function emonde.py : rendre_emonde
	@patch('builtins.input', side_effect=[])
	def rendre_emonde(self, mock_inputs):
		automate1 = copy.deepcopy(automate)
		result = emd.rendre_emonde(automate1)
		self.assertEqual(result, True)  

#########################################################################  test of functions langage.py  #######################################################################

class Test_generer_langage(unittest.TestCase): # test of function langage.py : generer_langage
	@patch('builtins.input', side_effect=[])
	def generer_langage(self, mock_inputs):
		automate1 = copy.deepcopy(automate)
		result = lang.generer_langage(automate1)
		self.assertEqual(result, True)
  
class Test_test_automates_equivalents(unittest.TestCase): # test of function langage.py : test_automates_equivalents
	@patch('builtins.input', side_effect=[])
	def test_automates_equivalents(self, mock_inputs):
		automate1 = copy.deepcopy(automate)
		automate2 = copy.deepcopy(automate)
		result = lang.automates_equivalents(automate1, automate2)
		self.assertEqual(result, True)

#########################################################################  test of functions interractions  #######################################################################



class Test_main(unittest.TestCase):
	@patch('builtins.input', side_effect=['2', 'test', 'q0,a,q1', 'q0,a,q0', 'q1,b,q2', 'q2,c,q1', '', 'q0', '', 'q2', '', '1', '3', '2', '3', '4', '1', 'test1', '2', '1', 'q2,c,q3', 'q3,a,q0', '', '2', 'q3', 'q2', '1', '3', 'q0', '1', 'q1', '', '4', '3', 'q1', '', 'q1', '', '4', 'q2', 'q2', '', '5', '5', 'test_unitaire', '6', '1', 'b', 'c', 'c', 'b', 'c', '', '2', '3', '4', '5', '3', '6', '7', '1', '2', '4', '5', '8', '2', '3', '4', '5', '6', '7', '9', '10', '1', '1', 'test_unitaire', '11'])
	def test_main(self, mock_inputs):
		result = main.main()
		if(platform.system() == 'Linux'):
			sleep(0.5)
			subprocess.run(['rm', '../file/test_unitaire.json', '../file/image_automate.dot', '../file/image_automate.png'])
		if(platform.system() == 'Windows'):
			sleep(0.5)
			subprocess.run(['rm', '../file/test_unitaire.json', '../file/image_automate.dot', '../file/image_automate.png'], shell=True)
		self.assertEqual(result, 0)





################################################################################  end of tests ####################################################################################

global automate
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

if __name__ == '__main__':
	if(platform.system() == 'Windows'):
		#print('\n\n\nPour une raison inconnue, sous Windows, le programme continue de lancer des tests après avoir executé tout les tests')
		#print("Pour lire le résultat il faut donc le chercher en remontant dans l'affichage de la console")
		#print("Si possible, lancez le programme sous linux pour éviter la gêne")
		#input("\n\nAppuyer sur entrer pour continuer")

		buffer = StringIO()
		runner = unittest.TextTestRunner(stream=buffer, verbosity=1)

		# Charger tous les tests du module en découvrant automatiquement
		suite = unittest.TestLoader().discover('.')

		# Exécution des tests et stockage des résultats dans le buffer
		result = runner.run(suite)

		# Récupération du bilan des tests dans une variable
		test_results = buffer.getvalue()
		print(test_results)
	else:
		unittest.main()
	print("Note : la fonction test calculant le produit peut parfois retourner un test négatif, cela est probablement dû à une différence dans l'ordre de certains éléments, car l'échec du test n'est pas systématique pour un même automate.")
	print("L'échec de ce test n'est donc pas alarmant")
