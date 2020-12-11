#Header
"""
but: faire une fonction de command qui gère le déroulement des fonctions
auteur: Ankou Pierre-Olivier
date de maj: 11/12/2020
"""
from tkinter import Tk,Label
from tkinter import messagebox

from fproposition import fproposition as fprop
from fscore import fscore

def fgestion(mot,mot_caché,vie,L,pvar,suite):
    var = pvar.get()
    new_mot_caché,new_vie = fprop(mot,mot_caché,vie,L,var)
    
    #top = Tk.Toplevel()
    #top.overrideredirect(1)
    #labelmot = Label(top, text = new_mot_caché)
    #labelmot.pack()
    
    #btn = Tk.Button(top, text = "Quitter", command = top.destroy)
    #btn.pack(side = "bottom")
    
    if new_mot_caché == mot:
        messagebox.showwarning("Résultat","Bon mot !\n Vous avez gagné ! :)")

    elif new_vie < vie:
        messagebox.showwarning("Résultat","Mauvaise proposition.\nTentez autre chose")

    elif new_vie == vie and new_mot_caché != mot:
        messagebox.showwarning("Résultat","Proposition correcte")
        
    elif vie == 0:
        messagebox.showwarning("Résultat","Vie restantes : 0\nGame Over")

    messagebox.showinfo("Mot",new_mot_caché)
    return()
