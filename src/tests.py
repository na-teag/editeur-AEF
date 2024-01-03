

from unittest.mock import patch
from time import sleep
import unittest
import copy
import platform
import subprocess

import data.file as file
import data.structure as strct
import editing.modif as md
import editing.testermot as testermot
import main

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


##########################################################################  functions from modif.py ##########################################################################

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
		liste = []
		liste.append(copy.deepcopy(automate))
		result = md.testTransition(liste, 0, "q0")
		self.assertEqual(result, 1)
		result = md.testTransition(liste, 0, "q3")
		self.assertEqual(result, 0)
		result = md.testTransition(liste, 0, "q4")
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


class testChangeStatesInitFinal(unittest.TestCase):  # test of function changeStatesInitFinal, with 3rd parameter = 0
	@patch('builtins.input', side_effect=['q0', 'q3', ''])
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
			"Etats_initiaux": ["q3"],
			"Etats_finaux": ["q2"],
			"Nom" : "test"
		}
		self.assertEqual(liste[indice], automate2)


class testChangeStatesInitFinal2(unittest.TestCase):  # test of function changeStatesInitFinal, with 3rd parameter = 1
	@patch('builtins.input', side_effect=['q3', 'q1', 'q2', ''])
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

##########################################################################  functions from minimal.py ##########################################################################

print(MAGENTA+"TEST minimal"+ENDC)
import unitTest.testminimal
##########################################################################  functions from concat.py ##########################################################################

print(MAGENTA+"TEST concaténation de 2 automates"+ENDC)
import unitTest.testconcat
##########################################################################  functions from produit.py ##########################################################################

print(MAGENTA+"TEST produits de 2 automates"+ENDC)
import unitTest.testproduit


##########################################################################  functions from testermot.py ##########################################################################

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


##################################################################  test of functions interractions  ##############################################################

class Test_main(unittest.TestCase):																																																																																																		# ici, mettre les générations d'AEF complément, miroir, produit, et concaténation
	@patch('builtins.input', side_effect=['2', 'test', 'q0,a,q1', 'q0,a,q0', 'q1,b,q2', 'q2,c,q1', '', 'q0', '', 'q2', '', '1', '3', '2', '3', '4', '1', 'test1', '2', '1', 'q2,c,q3', 'q3,a,q0', '', '2', 'q3', 'q2', '1', '3', 'q0', '1', 'q1', '', '4', '3', 'q1', '', 'q1', '', '4', 'q2', 'q2', '', '5', '5', 'test_unitaire', '6', '1', 'b', 'c', 'c', 'b', 'c', '', '2', '3', '4', '5', '6', '7', '7', '1', '2', '3', '4', '5', '8', '1',                                                                                  '6', '9', '1', '1', 'test_unitaire', '10'])
	def test_main(self, mock_inputs):
		result = main.main()
		if(platform.system() == 'Linux'):
			sleep(0.5)
			subprocess.run(['rm', '../file/test_unitaire.json', '../file/image_automate.dot', '../file/image_automate.png'])
		if(platform.system() == 'Windows'):
			sleep(0.5)
			subprocess.run(['del', '../file/test_unitaire.json', '../file/image_automate.dot', '../file/image_automate.png'], shell=True)
		self.assertEqual(result, 0)

##########################################################################  end of tests ##########################################################################

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

#testermot.tester(automate)
unittest.main()
