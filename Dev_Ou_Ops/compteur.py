import os.path

file_compteur = "compteur"



def lire_compteur():

    if os.path.isfile(file_compteur):
        print("Compteur existe")
        fichier = open(file_compteur,'r')
#Lecture fichier compteur
        nb_visiteurs = int(fichier.read())
# "int" transforme le contenu en un nombre car on veut le nombre de visiteurs)

    else:
        print("Compteur existe pas ")
        nb_visiteurs = 0
#Le fichier n'existe pas / page jamais visitée
        fichier = open(file_compteur,'w')

    fichier = open(file_compteur,'w')
    fichier.write(str(nb_visiteurs+ 1))
    return nb_visiteurs+1





