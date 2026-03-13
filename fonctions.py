""" fichier où on écrira les fonctions nécéssaires pour le main """
" rajouter une fonction vitesse pour augmenter la vitesse d'execution des etape quand on clique sur play "
"rajouter une fonction permetant de revenir en arriere d'une etape " 

from math import sin, cos, radians

def etape(grille, case_fourmi, orientation_fourmi, i, j, nb_etape):
        orientation_fourmi = ( orientation_fourmi + 270 - 180 * (case_fourmi) ) % 360
        case_fourmi = grille[( i-int(sin(orientation_fourmi)) ) % 5][( j+int(cos(orientation_fourmi)) ) % 5]
        grille[i][j] += (-1)**grille[i][j]
        nb_etape += 1
        (i, j) = ((i-int(sin(radians(orientation_fourmi))) ) % 5, (j+int(cos(radians(orientation_fourmi)))) % 5)
        return (grille, case_fourmi, orientation_fourmi, i, j, nb_etape)