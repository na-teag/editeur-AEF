

from unittest.mock import patch
import unittest
import copy

import fonctions
import fonctions2
import testermot

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


##########################################################################  functions from fonctions2.py ##########################################################################


class Test_creer_automate_vide(unittest.TestCase): # test of function creer_automate_vide
	@patch('builtins.input', side_effect=[])
	def test_creer_automate_vide(self, mock_inputs):
		result = fonctions2.creer_automate_vide()
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
		result = fonctions2.alphabet(automate)
		result2 = ['a','b','c','d']
		self.assertEqual(result.sort(), result2.sort())


##########################################################################  functions from fonctions.py ##########################################################################

class Test_editer_etats(unittest.TestCase):  # test of function editer_etats
	@patch('builtins.input', side_effect=['test', 'q0,a,q0', 'q0,a,q1', 'q1,c,q0', 'q1,c,q2', 'q1,d,q1', 'q2,a,q0', 'q2,b,q1', 'q3,b,q2', '', 'q0', '', 'q2', ''])
	def test_editer_etats(self, mock_inputs):
		liste = []
		indice = 0
		liste.append(fonctions2.creer_automate_vide())
		liste, indice = fonctions.editer_etats(liste, indice)
		self.assertEqual(liste[indice], automate)


class Test_test_transition_entrante(unittest.TestCase):  # test of function test_transition_entrante
	@patch('builtins.input', side_effect=[])
	def test_test_transition_entrante(self, mock_inputs):
		liste = []
		liste.append(copy.deepcopy(automate))
		result = fonctions.test_transition_entrante(liste, 0, "q0")
		self.assertEqual(result, 1)
		result = fonctions.test_transition_entrante(liste, 0, "q3")
		self.assertEqual(result, 0)
		result = fonctions.test_transition_entrante(liste, 0, "q4")
		self.assertEqual(result, 0)


class Test_renommer_etats(unittest.TestCase):  # test of function renommer_etats
	@patch('builtins.input', side_effect=['q3', 'q0', '1'])
	def test_renommer_etats(self, mock_inputs):
		liste = []
		indice = 0
		liste.append(copy.deepcopy(automate))
		liste, indice = fonctions.renommer_etats(liste, indice)
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


class Test_changer_etats_ini_fin(unittest.TestCase):  # test of function changer_etats_ini_fin, with 3rd parameter = 0
	@patch('builtins.input', side_effect=['q0', 'q3', ''])
	def test_changer_etats_ini_fin(self, mock_inputs):
		liste = []
		indice = 0
		liste.append(copy.deepcopy(automate))
		liste, indice = fonctions.changer_etats_ini_fin(liste, indice, 0)
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


class Test_changer_etats_ini_fin2(unittest.TestCase):  # test of function changer_etats_ini_fin, with 3rd parameter = 1
	@patch('builtins.input', side_effect=['q3', 'q1', 'q2', ''])
	def test_changer_etats_ini_fin2(self, mock_inputs):
		liste = []
		indice = 0
		liste.append(copy.deepcopy(automate))
		liste, indice = fonctions.changer_etats_ini_fin(liste, indice, 1)
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


class Test_suppr_etat(unittest.TestCase):  # test of function suppr_etat
	@patch('builtins.input', side_effect=['q2', '1', 'q1', ''])
	def test_suppr_etat(self, mock_inputs):
		liste = []
		indice = 0
		liste.append(copy.deepcopy(automate))
		liste, indice = fonctions.suppr_etat(liste, indice)
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


class Test_demande_suppr(unittest.TestCase):  # test of function demande_suppr, and thus function suppr, and thus function select
	@patch('builtins.input', side_effect=['1', '2', 'test', 'q0,a,q1', '', 'q0', '', 'q1', ''])
	def test_demande_suppr(self, mock_inputs):
		liste = []
		indice = 0
		liste.append(copy.deepcopy(automate))
		liste, indice = fonctions.demande_suppr(liste, indice)
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
