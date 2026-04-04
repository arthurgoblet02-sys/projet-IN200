from math import sin, cos, radians
#from projet_in200 import *

def step(grille, etat_case_fourmi, orientation_fourmi, i_j, nb_etape, side, nb_fourmis, modulo):
        etat_case_fourmi = grille[i_j[0]][i_j[1]]
        orientation_fourmi = ( orientation_fourmi + 270 - 180 * (etat_case_fourmi) ) % 360
        etat_case_fourmi = grille[(i_j[0] - int(sin(radians(orientation_fourmi)))) % side][(i_j[1] + int(cos(radians(orientation_fourmi)))) % side]
        grille[i_j[0]][i_j[1]] += (-1)**grille[i_j[0]][i_j[1]]
        (i_j[0], i_j[1]) = ((i_j[0] - int(sin(radians(orientation_fourmi))) ) % side, (i_j[1] + int(cos(radians(orientation_fourmi)))) % side)
        nb_etape += 1
        modulo = (modulo + 1) % nb_fourmis
        
        return (grille, etat_case_fourmi, orientation_fourmi, i_j, nb_etape, side, nb_fourmis, modulo)


def back_step(grille, etat_case_fourmi, orientation_fourmi, i_j, nb_etape, side, nb_fourmis, modulo):
        (i_j[0], i_j[1]) = ((i_j[0] + int(sin(radians(orientation_fourmi))) ) % side, (i_j[1] - int(cos(radians(orientation_fourmi)))) % side) 
        grille[i_j[0]][i_j[1]] += (-1)**grille[i_j[0]][i_j[1]]
        etat_case_fourmi = grille[i_j[0]][i_j[1]]
        orientation_fourmi = ( orientation_fourmi - 270 + 180 * (etat_case_fourmi) ) % 360
        nb_etape -= 1
        modulo = (modulo - 1) % nb_fourmis
        return (grille, etat_case_fourmi, orientation_fourmi, i_j, nb_etape, side, nb_fourmis, modulo)

 

en_pause =  True

def fonction_play():
        global en_pause
        en_pause = False
        print("Play")

def fonction_pause():
        global en_pause
        en_pause = True
        print("Pause")
