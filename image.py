def image(liste_automate, automate_selected):

	message_erreur = "Veuillez installer la bibliothèque graphviz" # check all the conditions for using graphviz, and help to install it
	try:
		import graphviz
		import shutil
		import subprocess
		import platform
		if shutil.which('dot') is None:
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
					print("\n\nEssayez d'installer graphviz manuellement, et ajouter le au PATH")
					return 1
				else:
					print(result.stdout)

				print("\n\nInstallation de graphviz réussie")
		
	except ImportError:
		try:
			import shutil
			import platform
			try:
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
						if shutil.which('dot') is None:
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
								print("\n\nEssayez d'installer graphviz manuellement, et ajouter le au PATH")
								return 1
							else:
								print(result.stdout)
							print("\n\nInstallation de graphviz réussie")						
					else:
						print(message_erreur)
						return 1
				else:
					print(message_erreur)
					return 1
			except ImportError:
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

	try:
		from PIL import Image
	except ImportError:
		if(platform.system() == 'Linux' or platform.system() == 'Windows'):
			choix = input("\n\nVeuillez installer la bibliothèque PIL pour afficher l'image, voulez vous essayer de lancer l'installation ?\n1 : oui\n2 : non\n\n")
			if(choix == "1"):
				print("Installation de la bibliothèque python PIL en cours...")
				result = subprocess.run(['pip', 'install', 'Pillow'])
				if result.stderr:
					print("Erreur lors de l'installation de PIL :")
					print(result.stderr)
					print("\n\nEssayez d'installer la bibliothèque PIL manuellement")
					return 1
				else:
					print(result.stdout)
			else:
				print("Veuillez ouvrir l'image manuellement")
	image_automate = Image.open("image_automate.png")
	image_automate.show()
	return 0