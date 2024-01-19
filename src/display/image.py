def image(list_automate, automate_selected):

	message_erreur = "Le programme ne parvient pas à faire l'installation, veuillez installer la graphviz et sa bibliothèque python manuellemnt" # check all the conditions for using graphviz, and help to install it
	try:
		import graphviz # try import graphviz to see if installed
		import shutil
		import subprocess
		import platform
		import os
		if shutil.which('dot') is None: # check that graphviz is registered as a program (different from the library installation)
			dossier = r'C:\Program Files\Graphviz\bin'
			resultat2 = subprocess.run(f'dir "{dossier}"', shell=True, capture_output=True, text=True)
			if(platform.system() == 'Linux' or (platform.system() == 'Windows' and resultat2.stderr != "")):
				choix = input("\n\nVeuillez installer le logiciel graphviz, voulez vous essayer de lancer l'installation ?\n1 : oui\n2 : non\n\n")
				if(choix == "1"):
					print("\n\n\nInstalation du logiciel graphviz en cours...")
					if(platform.system() == 'Linux'):
						print("\n\nsudo apt install graphviz")
						result = subprocess.run(['sudo', 'apt', 'install', 'graphviz']) # install the program for both windows and linux OS
					elif(platform.system() == 'Windows'):
						result = subprocess.run(['winget', 'install', 'graphviz'])
					else:
						print(message_erreur)
						return 1
					if result.stderr:
						print("Erreur lors de l'installation de graphviz :")
						print(result.stderr)
						print("\n\nEssayez d'installer graphviz manuellement, et ajoutez le au PATH")
						return 1
					else:
						print(result.stdout)

					print("\n\nInstallation de graphviz réussie.\n\n\nPour utiliser Graphviz, cette interface doit être relancée, veuillez sauvegarder vos fichiers puis fermer la fenêtre avant de relancer le programme")
					print("\n\n\n\n\n\n\n\n\n\n\n")
					return 0
			elif(platform.system() == 'Windows' and "File Not Found" not in resultat2.stdout): # if the OS is Windows, the program must be added to the PATH with admin rights (not possible with this script, no "sudo" command)
				print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nimpossible d'ajouter {dossier} au path, les droits d'administrateurs sont nécéssaires") # explaining how to add to the PATH
				print(f'\n\npour ajouter le programme au path, ouvrer l\'invité de commande (cmd) en tant qu\'administrateur et lancer la commande : setx /M PATH "%PATH%;{dossier}"')
				print(f'\nSinon, pour le faire manuellement, tapez dans les réglages "modifier les variables d\'environnement système" puis séléctionnez "variables d\'environnement système" puis dans les variables système (fenêtre du bas) double cliquez sur "path" et ajoutez {dossier} avant d\'appuyer sur "ok" dans toute les fenêtres ouvertes')
				print(f"\nensuite, fermer cette console, puis réouvrez là et relancez ce programme (n'oubliez pas de sauvegarder vos fichiers)")
				return 0
			else:
				print("\n\n\n\nVeuillez installer graphviz et ajoutez le programme aux variables d\'environnement système (PATH)")
				return 1
		
	except ImportError: # if the library isn't installed
		try:
			import shutil
			import platform
			import subprocess
			if(platform.system() == 'Linux' or platform.system() == 'Windows'):
				choix = input("\n\nVeuillez installer la bibliothèque graphviz, voulez vous essayer de lancer l'installation ?\n1 : oui\n2 : non\n\n")
				if(choix == "1"):
					print("Installation de la bibliothèque python graphviz en cours...")
					try:
						result2 = subprocess.run(['python', '-m', 'ensurepip', '--upgrade'], check=True) # check if pip is installed
					except:
						print("", end='')
					try:
						result = subprocess.run(['pip', 'install', 'graphviz']) # install the graphviz library with pip
					except:
						print("Erreur lors de l'installation de graphviz :")
						print(result.stderr)
						print("\n\nVérifiez que vous êtes connecté à internet et que pip est bien installé et réessayez, ou essayez d'installer la bibliothèque graphviz manuellement")
						return 1
					print(result.stdout)
					return image(list_automate, automate_selected)
				else:
					print(message_erreur)
					return 1
			else:
				print(message_erreur)
				return 1
		except ImportError:
			print(message_erreur)
			return 1
	
	automate = list_automate[automate_selected]
	with open("../file/image_automate.dot", 'w') as fichier: # write the .dot file
		fichier.write('digraph {\n')
		
		
		for etat, transitions in automate['Etats'].items(): # declares the state and their shape on the image in function of their type
			if etat in automate['Etats_initiaux']:
				fichier.write(f'    "{etat}" [shape=circle];\n')
				fichier.write(f'    "start_node_{etat}" [shape=point, width=0];\n')
				fichier.write(f'    "start_node_{etat}" -> "{etat}" [label=""];\n')
			elif etat in automate['Etats_finaux']:
				fichier.write(f'    "{etat}" [shape=doublecircle];\n')
			else:
				fichier.write(f'    "{etat}" [shape=circle];\n')
			
		
		for etat, transitions in automate['Etats'].items(): # declares the links between the states, with the name of the transitions
			for transition, etats_suivants in transitions.items():
				for etat_suivant in etats_suivants:
					fichier.write(f'    "{etat}" -> "{etat_suivant}" [label="{transition}"];\n')
		
		fichier.write('}')

	'''
	graph = graphviz.Source.from_file("../file/image_automate.dot") # creates a graph
	graph.render("../file/image_automate", format='png') # generates the image

	print("\033[2J") # clear the screen
	print("\n\nL'image à été générée")'''
	
	dot_file_path = "../file/image_automate.dot"
	output_file_path = "../file/image_automate"
	output_file_path += "_" + automate["Nom"]

	try:
		graph = graphviz.Source.from_file(dot_file_path)
		subprocess.run(["dot", "-Tpng", dot_file_path, "-o", output_file_path + ".png"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	except subprocess.CalledProcessError as e:
		print("\033[2J") # clear the screen
		result = e.stderr.decode('utf-8')
		print(f"Erreur lors de la génération de l'image : {result}")
	else:
		print("\033[2J") # clear the screen
		print("Image générée avec succès.")


	try:
		if(platform.system() == 'Linux'): # delete the .dot file afterward, because if the file is corupted, it is impossible to generate a new one while the corupted one still exists
			subprocess.run(['rm', '../file/image_automate.dot'])
		if(platform.system() == 'Windows'):
			subprocess.run(['rm', '../file/image_automate.dot'], shell=True)
	except:
		print("", end='')

	output_file_path += ".png"
	if(platform.system() == 'Windows'): # opening the image with default software managing images
		chemin = os.path.abspath(output_file_path)
		subprocess.run(["explorer", chemin])
	elif(platform.system() == 'Linux'):
		subprocess.run(["xdg-open", output_file_path])
	else:
		print("\n\nveuillez ouvrir l'image du dossier \"file\" manuellement")
	print("\n\n\n\n\n\n\n\n\n\n\n")
			