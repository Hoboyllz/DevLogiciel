#Header
"""
but: contenir le meilleur score
auteur: Ankou Pierre-Olivier
date de maj: 02/12/2020
"""

"""
Cette fonction prend la suite de partie gagner sans erreur du joueur en paramètre
et ne retourne rien
"""
def fscore(pscore):
    fichier = open("score.txt","r")
    contenu = str(fichier.read())
    fichier.close()

    L = contenu.split(":")

    if pscore>int(L[1]):
        fichier = open("score.txt","w")
        fichier.write("suite de mot sans perdre de vie :" + str(pscore))
        print("Nouveau Record ! " + str(pscore) + " mots à la suite sans perdre de vies !")
        return()
    
    else:
        return()
