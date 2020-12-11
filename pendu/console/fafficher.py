#Header
"""
but : afficher dans la console le jeu
auteur : Ankou Pierre-Olivier
date de maj : 06/12/2020
"""

"""
fafficher prend 2 paramètres (le mot en str, le mot caché par des "_" en str,
le nombre de vie en int().
La fonction ne retourne rien
"""
def fafficher(pmot,pproposition,pvie):
    print("Jeu du pendu")
    print("Vous avez encore ", pvie, " tentatives")
    print(pproposition)
    print("proposez un mot ou une lettre")
    print("\n")


