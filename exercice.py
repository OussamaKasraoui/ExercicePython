import random

# function pour afficher la moyenne Q-10
def moyenne(tableau):
	moyenne = 1

	print '\n# les moyennes de ', len(tableau),' tableau ', tableau
	for valeur in tableau:

		print moyenne, ' x ', valeur, ' = ', moyenne * valeur, '\n'
		
		moyenne *= valeur



# function pour faciliter la tache de la Question numero 1
def functionPourRemplirTableNfois(N, debut, fin):
	tableau_N_a_retourner = []
	
	i = 1
	while i <= N:
		i += 1
		tableau_N_a_retourner.append(random.uniform(debut, fin)) 
		pass

	print '\n ', len(tableau_N_a_retourner),' valeurs flottantes genere : ', tableau_N_a_retourner

	# Q-10
	# Q-12
	moyenne(tableau_N_a_retourner)

	print 'tapper sur Entrer ...'
	raw_input()

	return tableau_N_a_retourner



# DEBUT du programmme
print '\n le programme va commencer ...'


# Q-9

N = 5
debut = 8
fin = 12

tableau_N = functionPourRemplirTableNfois(N, debut, fin)
 

# Q-11
for N in [5, 10, 50, 100, 1000]:
	# en utilisant les deux operations precedentes
	tableau_N = functionPourRemplirTableNfois(N, debut, fin)


# Q-13 
# les valeurs depassent les limites autorise de stackage 
