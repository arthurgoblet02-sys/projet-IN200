""" fichier où on écrira les fonctions nécéssaires pour le main """
" rajouter une fonction vitesse pour augmenter la vitesse d'execution des etape quand on clique sur play "
"rajouter une fonction permetant de revenir en arriere d'une etape " 

from math import sin, cos, radians

def step(grille, case_fourmi, orientation_fourmi, i, j, nb_etape, side):
        orientation_fourmi = ( orientation_fourmi + 270 - 180 * (case_fourmi) ) % 360
        case_fourmi = grille[(i-int(sin(radians(orientation_fourmi)))) % side][(j+int(cos(radians(orientation_fourmi)))) % side]
        grille[i][j] += (-1)**grille[i][j]
        nb_etape += 1
        (i, j) = ((i-int(sin(radians(orientation_fourmi))) ) % side, (j+int(cos(radians(orientation_fourmi)))) % side)
        return (grille, case_fourmi, orientation_fourmi, i, j, nb_etape, side)


def back_step(grille, case_fourmi, orientation_fourmi, i, j, nb_etape, side):
        (i, j) = ((i+int(sin(radians(orientation_fourmi))) ) % side, (j-int(cos(radians(orientation_fourmi)))) % side)      
        nb_etape -= 1
        grille[i][j] += (-1)**grille[i][j]
        case_fourmi = grille[i][j]
        orientation_fourmi = ( orientation_fourmi - 270 + 180 * (case_fourmi) ) % 360
        return (grille, case_fourmi, orientation_fourmi, i, j, nb_etape, side)



