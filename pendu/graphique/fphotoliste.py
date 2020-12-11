#Header
"""
but: remplir la liste de photo
auteur: Ankou Pierre-Olivier
date de maj: 11/12/2020
"""
from tkinter import PhotoImage

def fphotoliste():
    for i in range(8):
    photo = PhotoImage(file = "../image/bonhomme"+str(i+1)+".gif")
    photoL.append(photo)
    return(photoL)
