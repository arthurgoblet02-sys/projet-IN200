"creer une fonction Plateau pour creer le plateau pour que je puisse le mettre dans interface graphique   "
from projet_in200 import grille, side
from tkinter import *

def Plateau (window):
    nbr_ligne = len(grille)
    nbr_colonne = len(grille[0])
    taille_case = 100
    colonne = nbr_colonne * taille_case
    ligne = nbr_ligne * taille_case
    canva = Canvas (window,width=colonne,height=ligne, bg="white" )
    canva.grid(row=3, columnspan=13)
    for i in range(nbr_ligne):
        for j in range(nbr_colonne):
            couleur = "white"
            x1 = j* taille_case
            y1 = i * taille_case
            x2 = x1 + taille_case
            y2 = y1 + taille_case
            if grille[i][j] == 1:
                couleur = "black"
            canva.create_rectangle (x1,y1,x2,y2 , fill= couleur, outline= "black" ) 
    return canva 