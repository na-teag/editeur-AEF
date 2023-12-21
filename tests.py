

from unittest.mock import patch
import unittest

import fonctions
import fonctions2

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


##########################################################################  fonctions from fonctions2.py ##########################################################################


class Test_creer_automate_vide(unittest.TestCase): # test of fonction creer_automate_vide
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


class Test_alphabet(unittest.TestCase): # test of fonction alphabet
	@patch('builtins.input', side_effect=[])
	def test_alphabet(self, mock_inputs):
		result = fonctions2.alphabet(automate)
		result2 = ['a','b','c','d']
		self.assertEqual(result.sort(), result2.sort())


##########################################################################  fonctions from fonctions.py ##########################################################################

class Test_editer_etats(unittest.TestCase):  # test of fonction editer_etats
	@patch('builtins.input', side_effect=['test', 'q0,a,q0', 'q0,a,q1', 'q1,c,q0', 'q1,c,q2', 'q1,d,q1', 'q2,a,q0', 'q2,b,q1', '', 'q0', '', 'q2', ''])
	def test_editer_etats(self, mock_inputs):
		liste = []
		indice = 0
		liste.append(fonctions2.creer_automate_vide())
		liste, indice = fonctions.editer_etats(liste, indice)
		self.assertEqual(liste[indice], automate)



##########################################################################  end of tests ##########################################################################

global automate
automate = {
	"Etats": {
		"q0": {"a": ["q0","q1"]},
		"q1": {"c": ["q0","q2"], "d": ["q1"]},
		"q2": {"a": ["q0"], "b": ["q1"]}
	},
	"Etats_initiaux": ["q0"],
	"Etats_finaux": ["q2"],
	"Nom" : "test"
}



unittest.main()