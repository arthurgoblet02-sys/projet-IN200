
"HELIO + ARTHUR (arthur a juste rajouter les val. )"


from valeurs_initiales import *
import valeurs_initiales as val 
from math import sin, cos, radians
from tkinter import *



#4 états : 0 (blanc), 1 (noir), 2 (blue), 3 (rouge) - orientation : D, G, G, D


def next_():
        
      global grille, nb_etape, side, liste_etat_case_fourmi, liste_orientation_fourmi, liste_case_fourmi

      for k in range(val.nb_fourmis):

                #actualisation de l'état de la case de la fourmi
                val.liste_etat_case_fourmi[k] = grille[val.liste_case_fourmi[k][0]][val.liste_case_fourmi[k][1]] 

                #changement de l'orientation selon l'état de la case
                if val.liste_etat_case_fourmi[k] % 3 == 0:
                        val.liste_orientation_fourmi[k] = (val.liste_orientation_fourmi[k] - 90) % 360
                else:
                        val.liste_orientation_fourmi[k] = (val.liste_orientation_fourmi[k] + 90) % 360

                #stockage des anciennes coordonnées et avancement d'une case (calcul des nouvelles coordonnées) 
                ancienne_ligne = val.liste_case_fourmi[k][0]
                ancienne_colonne = val.liste_case_fourmi[k][1]
                (val.liste_case_fourmi[k][0], val.liste_case_fourmi[k][1]) = ((val.liste_case_fourmi[k][0] - int(sin(radians(val.liste_orientation_fourmi[k]))) ) % side, (val.liste_case_fourmi[k][1] + int(cos(radians(val.liste_orientation_fourmi[k])))) % side)
                
                #changement de couleur de la case passée 
                grille[ancienne_ligne][ancienne_colonne] = (grille[ancienne_ligne][ancienne_colonne] + 1) % 4
        
      nb_etape += 1


def back_():

        global grille, nb_etape, side, liste_etat_case_fourmi, liste_orientation_fourmi, liste_case_fourmi
        
        for k in range(val.nb_fourmis):

                #calcul des anciennes coordonnées et recul d'une case
                (val.liste_case_fourmi[k][0], val.liste_case_fourmi[k][1]) = ((val.liste_case_fourmi[k][0] + int(sin(radians(val.liste_orientation_fourmi[k]))) ) % side, (val.liste_case_fourmi[k][1] - int(cos(radians(val.liste_orientation_fourmi[k])))) % side)

                #remise de la couleur d'origine de la case 
                grille[val.liste_case_fourmi[k][0]][val.liste_case_fourmi[k][1]] = (grille[val.liste_case_fourmi[k][0]][val.liste_case_fourmi[k][1]] - 1) % 4

                #actualisation de l'état de la case de la fourmi
                val.liste_etat_case_fourmi[k] = grille[val.liste_case_fourmi[k][0]][ val.liste_case_fourmi[k][1]] 

                #remise de l'orientation d'origine selon l'état de la case
                if val.liste_etat_case_fourmi[k] % 3 == 0:
                        val.liste_orientation_fourmi[k] = (val.liste_orientation_fourmi[k] + 90) % 360
                else:
                        val.liste_orientation_fourmi[k] = (val.liste_orientation_fourmi[k] - 90) % 360
        
        nb_etape -= 1




