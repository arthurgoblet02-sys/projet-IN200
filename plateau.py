"creer une fonction Plateau pour creer le plateau pour que je puisse le mettre dans interface graphique   "
from valeurs_initiales import grille, side
from tkinter import *

def Plateau (window):
    nbr_ligne = len(grille)
    nbr_colonne = len(grille[0])
    taille_case = 500 / side
    colonne = nbr_colonne * taille_case
    ligne = nbr_ligne * taille_case
    canvas = Canvas(window,width=colonne,height=ligne, bg="white")
    for i in range(nbr_ligne):
        for j in range(nbr_colonne):
            couleur = "white"
            x1 = j* taille_case
            y1 = i * taille_case
            x2 = x1 + taille_case
            y2 = y1 + taille_case
            if grille[i][j] == 1:
                couleur = "blue"
            elif grille[i][j] == 0:
                couleur = "white"
            elif grille[i][j] == 2:
                couleur = "green"
            else : 
                couleur ="yellow"
            canvas.create_rectangle (x1,y1,x2,y2 , fill= couleur, outline= "white" ) 
    return canvas