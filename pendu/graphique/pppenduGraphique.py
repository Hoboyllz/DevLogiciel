#Header
"""
but: reproduire le pendu mais en version graphique
auteur: Ankou Pierre-Olivier
date de maj: 11/12/2020
Todo: afficher le mot caché
"""

from tkinter import Tk,Label,Button,Entry,StringVar,Frame,PhotoImage,Canvas

from ftxt import ftxt as ft
from fgestion import fgestion

suite = 0
vie = 8
L = []
mot,mot_caché = ft()
#photo = PhotoImage(file = "../image/bonhomme1.gif")
#item = mw.create_image(0,0,anchor = NW,image = photo)
#Canevas.pack(side = "right")
#printt(photo)


mw = Tk()
mw.title("Jeu du pendu 3055Junior")
mw.geometry("700x400")

labelmot = Label(mw, text = mot_caché)
labelmot.pack(side = "top")

buttonQuit = Button(mw, text = "Quitter" , fg = "black", command = mw.destroy)
buttonQuit.pack(side = "bottom")

var = StringVar()
champ = Entry(mw, textvariable = var)
champ.focus_set()
champ.pack(side = "left")

buttonValider = Button(mw, text = "valider la proposition", fg = "black",
                       command = lambda:fgestion(mot,mot_caché,vie,L,var,suite))
buttonValider.pack(side = "left")

mw.mainloop()
