"creer une fonction Plateau pour creer le plateau pour que je puisse le mettre dans interface graphique   "
from projet_in200 import grille
from tkinter import *

def Plateau (window):
    nbr_colonne = len(grille)
    nbr_ligne = len(grille[0])
    taille_case = 10
    colonne = nbr_colonne * taille_case
    ligne = nbr_ligne * taille_case
    canva = Canvas (window,width=colonne,height=ligne, bg="white" )
    canva.grid(row=1,column= 1 )
    for i in range(nbr_colonne):
        for j in range(nbr_ligne):
            x1 = i* taille_case
            y1 = j * taille_case
            if grille[i][j] == 1:
                couleur = "black"
            else:
                couleur = "white"
            canva.create_rectangle ((x1,x1),(y1,y1) ,fill= couleur, outline= "green" ) 
    return canva 