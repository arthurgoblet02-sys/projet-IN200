""" fichier où on écrira les fonctions nécéssaires pour le main """
" rajouter une fonction vitesse pour augmenter la vitesse d'execution des etape quand on clique sur play "
"rajouter une fonction permetant de revenir en arriere d'une etape " 

from math import sin, cos, radians
from projet_in200 import *

def step(grille, case_fourmi, orientation_fourmi, i, j, nb_etape, side):
        orientation_fourmi = ( orientation_fourmi + 270 - 180 * (case_fourmi) ) % 360
        case_fourmi = grille[(i-int(sin(radians(orientation_fourmi)))) % side][(j+int(cos(radians(orientation_fourmi)))) % side]
        grille[i][j] += (-1)**grille[i][j]
        (i, j) = ((i-int(sin(radians(orientation_fourmi))) ) % side, (j+int(cos(radians(orientation_fourmi)))) % side)
        nb_etape += 1
        return (grille, case_fourmi, orientation_fourmi, i, j, nb_etape, side)


def back_step(grille, case_fourmi, orientation_fourmi, i, j, nb_etape, side):
        (i, j) = ((i+int(sin(radians(orientation_fourmi))) ) % side, (j-int(cos(radians(orientation_fourmi)))) % side) 
        grille[i][j] += (-1)**grille[i][j]
        case_fourmi = grille[i][j]
        orientation_fourmi = ( orientation_fourmi - 270 + 180 * (case_fourmi) ) % 360
        nb_etape -= 1
        return (grille, case_fourmi, orientation_fourmi, i, j, nb_etape, side)

 

en_pause =  True

def fonction_play():
        global en_pause
        en_pause = False
        print("Play")

def fonction_pause():
        global en_pause
        en_pause = True
        print("Pause")
