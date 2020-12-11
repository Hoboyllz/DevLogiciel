#Header
"""
but: actualiser le mot caché
auteur: Ankou Pierre-Olivier
date de maj: 27/11/2020
"""

def factualiser(pmot,pmot_caché,plettre):
    #initialisation
    if plettre == pmot[0]:
        mot_caché = plettre
    else:
        mot_caché = pmot_caché[0]

    #suite
    for i in range(len(pmot[1:])):
        if pmot[1:][i] == plettre:
            mot_caché = mot_caché + " " + plettre 
        else:
            mot_caché = mot_caché + " " + pmot_caché[2*(i+1)]

    return(mot_caché)
