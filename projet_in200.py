from fonctions import step, back_step
from time import sleep
from random import randint
# from sauvegarde import charger # <-- Mis en COM (Désactivés car j'ai pas encore finit )

""" valeurs initiales """ 

#pas sur encore 
# donnees = charger()
# if donnees != None:
#     (grille, case_fourmi, orientation_fourmi, i, j, nb_etape, side, speed) = donnees
# else:

#mettre des numpy.array() partout au lieu des lists

#valeurs initiales à déterminer
nb_fourmis = 1
side = 5
#liste_case_fourmi = [[side//2, side//2] for _ in range(nb_fourmis)]
liste_case_fourmi = [[randint(0,side-1), randint(0,side-1)] for _ in range(nb_fourmis)]

#valeurs initiales fixées
liste_fourmis = ["fourmi" + str(i) for i in range(nb_fourmis)]
grille = [side*[0] for _ in range (side)] 
(droite, haut, gauche, bas) = (0, 90, 180, 270) 
nb_etape = 0
modulo = 0
speed = 1000
liste_orientation_fourmi = nb_fourmis * [droite]
liste_etat_case_fourmi = nb_fourmis * [0]

""" tests du programme """

steps = 10

for k in range(steps):
      (grille, liste_etat_case_fourmi[modulo], liste_orientation_fourmi[modulo], liste_case_fourmi[modulo], nb_etape, side, nb_fourmis, modulo) = step(grille, liste_etat_case_fourmi[modulo], liste_orientation_fourmi[modulo], liste_case_fourmi[modulo], nb_etape, side, nb_fourmis, modulo)
      print(liste_etat_case_fourmi, liste_orientation_fourmi, liste_case_fourmi)
      sleep(1 / speed)
      print("\n", "step", k+1, "\n")
      for k in grille:
            print(k) 
