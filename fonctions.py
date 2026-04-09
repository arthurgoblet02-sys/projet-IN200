from valeurs_initiales import *
from math import sin, cos, radians
from time import sleep

# 4 états : 0 (blanc), 1 (noir), 2 (vert), 3 (rouge) - orientation : D, G, G, D


def next_():
        
      global grille, nb_etape, nb_fourmis, side, liste_etat_case_fourmi, liste_orientation_fourmi, liste_case_fourmi

      for k in range(nb_fourmis):

                #actualisation de l'état de la case de la fourmi
                liste_etat_case_fourmi[k] = grille[liste_case_fourmi[k][0]][ liste_case_fourmi[k][1]] 

                #changement de l'orientation selon l'état de la case
                if liste_etat_case_fourmi[k] % 3 == 0:
                        liste_orientation_fourmi[k] = (liste_orientation_fourmi[k] - 90) % 360
                else:
                        liste_orientation_fourmi[k] = (liste_orientation_fourmi[k] + 90) % 360

                #stockage des anciennes coordonnées et avancement d'une case (calcul des nouvelles coordonnées) 
                ancienne_ligne = liste_case_fourmi[k][0]
                ancienne_colonne = liste_case_fourmi[k][1]
                (liste_case_fourmi[k][0], liste_case_fourmi[k][1]) = ((liste_case_fourmi[k][0] - int(sin(radians(liste_orientation_fourmi[k]))) ) % side, (liste_case_fourmi[k][1] + int(cos(radians(liste_orientation_fourmi[k])))) % side)
                
                #changement de couleur de la case passée 
                grille[ancienne_ligne][ancienne_colonne] = (grille[ancienne_ligne][ancienne_colonne] + 1) % 4
        
      nb_etape += 1


def back_():

        global grille, nb_etape, nb_fourmis, side, liste_etat_case_fourmi, liste_orientation_fourmi, liste_case_fourmi
        
        for k in range(nb_fourmis):

                #calcul des anciennes coordonnées et recul d'une case
                (liste_case_fourmi[k][0], liste_case_fourmi[k][1]) = ((liste_case_fourmi[k][0] + int(sin(radians(liste_orientation_fourmi[k]))) ) % side, (liste_case_fourmi[k][1] - int(cos(radians(liste_orientation_fourmi[k])))) % side)

                #remise de la couleur d'origine de la case 
                grille[liste_case_fourmi[k][0]][liste_case_fourmi[k][1]] = (grille[liste_case_fourmi[k][0]][liste_case_fourmi[k][1]] - 1) % 4

                #actualisation de l'état de la case de la fourmi
                liste_etat_case_fourmi[k] = grille[liste_case_fourmi[k][0]][ liste_case_fourmi[k][1]] 

                #remise de l'orientation d'origine selon l'état de la case
                if liste_etat_case_fourmi[k] % 3 == 0:
                        liste_orientation_fourmi[k] = (liste_orientation_fourmi[k] + 90) % 360
                else:
                        liste_orientation_fourmi[k] = (liste_orientation_fourmi[k] - 90) % 360
        
        nb_etape -= 1




