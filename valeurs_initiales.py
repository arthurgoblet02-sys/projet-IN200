from time import sleep
from random import randint
# from sauvegarde import charger # <-- Mis en COM (Désactivés car j'ai pas encore finit )

#pas sur encore 
# donnees = charger()
# if donnees != None:
#     (grille, case_fourmi, orientation_fourmi, i, j, nb_etape, side, speed) = donnees
# else:

#valeurs initiales mofifiables
nb_fourmis = 1
side = 11
liste_case_fourmi = [[side//2, side//2] for _ in range(nb_fourmis)]

#valeurs initiales fixées
grille = [side*[0] for _ in range(side)] 
nb_etape = 0
speed = 1
liste_orientation_fourmi = nb_fourmis * [0]
liste_etat_case_fourmi = nb_fourmis * [0]
