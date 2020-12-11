#Header
"""
but : récolter les entrée du joueur et les traiter
auteur : Ankou Pierre-Olivier
date de maj 06/12/2020
"""

from factualiser import factualiser as factu

"""
fproposition est une fonction qui prend 2 paramètres en entrée:
    1- le mot
    2- le nombre de tentatives restante
La fonction retourne le mot caché actualisé si c'est juste,
enlève une vie si c'est faux
finie si il n'y a plus de tentatives
"""
def fproposition(pmot,pmot_caché,pvie,pL,pvar):

    if pvar in pL:
        print("lettre déjà donnée")
        return(pmot_caché, pvie)
    
    elif len(pvar) == 1:
        pL.append(pvar)
        if pvar in pmot:
            print("Cette lettre est présente dans le mot")
            return(factu(pmot,pmot_caché,pvar),pvie)

        else:   
            pvie -= 1
            print("Cette lettre n'est pas présente dans le mot",
                   "vous perdez une tentatives")
            return(pmot_caché, pvie)

    elif len(pvar) > 1:
        if pvar == pmot:
            print("C'est le bon mot, vous avez gagné :)")
            return(pmot, pvie)
        else:
            pvie -= 1
            print("Ce n'est pas ce mot, vous venez de perdre une tentatives")
            return(pmot_caché, pvie)
            
    elif len(pvar) == 0:
        #Récursif
        var = str(input("Proposition : "))
        return(fproposition(pmot,pmot_caché,pvie,pL,var))
