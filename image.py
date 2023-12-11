def image(liste_automate, automate_selected):

	message_erreur = "Veuillez installer la bibliothèque graphviz" # check all the conditions for using graphviz, and help to install it
	try:
		import graphviz
		import shutil
		import subprocess
		import platform
		if shutil.which('dot') is None:
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
						print("Veuillez ajouter graphviz dans le PATH")
						return 1
					if result.stderr:
						print("Erreur lors de l'installation de graphviz :")
						print(result.stderr)
						print("\n\nEssayez d'installer graphviz manuellement, et ajoutez le au PATH")
						return 1
					else:
						print(result.stdout)

					print("\n\nInstallation de graphviz réussie")
					return image(liste_automate, automate_selected)
			elif(platform.system() == 'Windows' and "File Not Found" not in resultat2.stdout): # if the OS is Windows, the program must be added to the PATH with admin rights
				print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nimpossible d'ajouter {dossier} au path, les droits d'administrateurs sont nécéssaires")
				print(f'\n\npour ajouter le programme au path, ouvrer l\'invité de commande en tant qu\'administrateur et lancer la commande : setx /M PATH "%PATH%;{dossier}"')
				print(f'\nSinon, pour le faire manuellement, tapez dans les réglages "modifier les variables d\'environnement système" puis séléctionnez "variables d\'environnement système" puis dans les variables système (fenêtre du bas) double cliquez sur "path" et ajoutez {dossier} avant d\'appuyer sur "ok" dans toute les fenêtres ouvertes')
				print(f"\nensuite, fermer cette console, puis réouvrez là et relancez ce programme")
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
					result = subprocess.run(['pip', 'install', 'graphviz'])
					if result.stderr:
						print("Erreur lors de l'installation de graphviz :")
						print(result.stderr)
						print("\n\nEssayez d'installer la bibliothèque graphviz manuellement")
						return 1
					else:
						print(result.stdout)
						return image(liste_automate, automate_selected)
				else:
					print(message_erreur)
					return 1
			else:
				print(message_erreur)
				return 1
		except ImportError:
			print(message_erreur)
			return 1
	
	automate = liste_automate[automate_selected]
	with open("image_automate.dot", 'w') as fichier: # write the .dot file
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

	graph = graphviz.Source.from_file("image_automate.dot")
	graph.render("image_automate", format='png', cleanup=True)

	print("\n\nL'image à été générée")
	
	if(platform.system() == 'Windows'):
		subprocess.run(["explorer", "image_automate.png"])
	elif(platform.system() == 'Linux'):
		subprocess.run(["xdg-open", "image_automate.png"])
	else:
		print("veuillez ouvrir l'image manuellement")
			