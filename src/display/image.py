def image(list_automate, automate_selected):

	message_erreur = "Le programme ne parvient pas à faire l'installation, veuillez installer la graphviz et sa bibliothèque python manuellemnt" # check all the conditions for using graphviz, and help to install it
	try:
		import graphviz
		import shutil
		import subprocess
		import platform
		if shutil.which('dot') is None: # vérifier que graphviz est installé
			dossier = r'C:\Program Files\Graphviz\bin'
			resultat2 = subprocess.run(f'dir "{dossier}"', shell=True, capture_output=True, text=True)
			if(platform.system() == 'Linux' or (platform.system() == 'Windows' and resultat2.stderr != "")):
				choix = input("\n\nVeuillez installer le logiciel graphviz, voulez vous essayer de lancer l'installation ?\n1 : oui\n2 : non\n\n")
				if(choix == "1"):
					print("\n\n\nInstalation du logiciel graphviz en cours...")
					if(platform.system() == 'Linux'):
						print("\n\nsudo apt install graphviz")
						result = subprocess.run(['sudo', 'apt', 'install', 'graphviz'])
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
			elif(platform.system() == 'Windows' and "File Not Found" not in resultat2.stdout): # if the OS is Windows, the program must be added to the PATH with admin rights
				print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nimpossible d'ajouter {dossier} au path, les droits d'administrateurs sont nécéssaires")
				print(f'\n\npour ajouter le programme au path, ouvrer l\'invité de commande (cmd) en tant qu\'administrateur et lancer la commande : setx /M PATH "%PATH%;{dossier}"')
				print(f'\nSinon, pour le faire manuellement, tapez dans les réglages "modifier les variables d\'environnement système" puis séléctionnez "variables d\'environnement système" puis dans les variables système (fenêtre du bas) double cliquez sur "path" et ajoutez {dossier} avant d\'appuyer sur "ok" dans toute les fenêtres ouvertes')
				print(f"\nensuite, fermer cette console, puis réouvrez là et relancez ce programme (n'oubliez pas de sauvegarder vos fichiers)")
				return 0
			else:
				print("\n\n\n\nVeuillez installer graphviz et ajoutez le programme aux variables d\'environnement système (PATH)")
				return 1
		
	except ImportError:
		try:
			import shutil
			import platform
			import subprocess
			if(platform.system() == 'Linux' or platform.system() == 'Windows'):
				choix = input("\n\nVeuillez installer la bibliothèque graphviz, voulez vous essayer de lancer l'installation ?\n1 : oui\n2 : non\n\n")
				if(choix == "1"):
					print("Installation de la bibliothèque python graphviz en cours...")
					try:
						result2 = subprocess.run(['python', '-m', 'ensurepip', '--upgrade'], check=True)
					except:
						print("", end='')
					try:
						result = subprocess.run(['pip', 'install', 'graphviz'])
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
		
		
		for etat, transitions in automate['Etats'].items():
			if etat in automate['Etats_initiaux']:
				fichier.write(f'    {etat} [shape=circle];\n')
				fichier.write(f'    start_node_{etat} [shape=point, width=0];\n')
				fichier.write(f'    start_node_{etat} -> {etat} [label=""];\n')
			elif etat in automate['Etats_finaux']:
				fichier.write(f'    {etat} [shape=doublecircle];\n')
			else:
				fichier.write(f'    {etat} [shape=circle];\n')
			
		
		for etat, transitions in automate['Etats'].items():
			for transition, etats_suivants in transitions.items():
				for etat_suivant in etats_suivants:
					fichier.write(f'    {etat} -> {etat_suivant} [label="{transition}"];\n')
		
		fichier.write('}')

	graph = graphviz.Source.from_file("../file/image_automate.dot")
	graph.render("../file/image_automate", format='png', cleanup=True)

	print("\033[2J") # clear the screen
	print("\n\nL'image à été générée")
	
	
	if(platform.system() == 'Windows'):
		import os
		chemin = os.path.abspath("../file/image_automate.png")
		subprocess.run(["explorer", chemin])
	elif(platform.system() == 'Linux'):
		subprocess.run(["xdg-open", "../file/image_automate.png"])
	else:
		print("\n\nveuillez ouvrir l'image du dossier \"file\" manuellement")
	print("\n\n\n\n\n\n\n\n\n\n\n")
			