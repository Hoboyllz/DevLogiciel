#Header
"""
but : choisir un mot dans un fichier texte et le retourner
auteur : Ankou Pierre-Olivier
date de maj : 27/11/2020
To do : Rien
"""

from random import random

"""
ftxt est une fonction ne prenant aucun paramètre.
Cependant la fonction retourne 2 paramètres:
    1- le mot en str()
    2- le mot caché en str() sour la forme "_ _ _"
-1 indique un erreur imprévue
"""
def ftxt():
    taille = 5 + int(5*random())
    ligne_correct = taille - 5
    dico = open("dico", "r")

    c=0
    for ligne in dico:
        if c == ligne_correct:
            L = ligne.split(",")
            indice = len(L)*int(random())-1    
            mot = L[indice]

            "pour enlever le \n a la fin du mot"
            mot = mot[:len(mot)-1]
            mot_caché = "_"

            for i in mot[1:]:
                mot_caché = mot_caché + " _" 
            return(mot,mot_caché)
        c += 1
    return(print(-1))

