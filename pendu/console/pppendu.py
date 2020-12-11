#Header
"""
lien : https://github.com/Hoboyllz/DevLogiciel
but : jeu du pendu, programme principale
auteur : Ankou Pierre-Olivier
date de maj : 06/12/2020
"""

from ftxt import ftxt as ft
from fafficher import fafficher as faff
from fproposition import fproposition as fprop
from fscore import fscore

choix = "oui"
suite = 0

while choix!="non":
    print("Nouveau Mot !!! ")
    #initialisation
    vie = 8
    L = []
    mot,mot_caché=ft()

    #suite
    while mot_caché != mot and vie > 0:
        faff(mot,mot_caché,vie)
        var = str(input("Proposition : "))
        mot_caché,vie = fprop(mot,mot_caché,vie,L,var)
    #fin
    if vie == 0:
        print("Vie restantes : 0")
        print("Game Over :)")

    if vie == 8:
        suite += 1
        fscore(suite)
        
    choix = str(input("voulez-vous rejouer (oui/non) :"))
    print("\n")
