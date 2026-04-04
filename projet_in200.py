from fonctions import step, back_step
from time import sleep
# from sauvegarde import charger # <-- Mis en COM (Désactivés car j'ai pas encore finit )

""" valeurs initiales """ 

#pas sur encore 
# donnees = charger()
# if donnees != None:
#     (grille, case_fourmi, orientation_fourmi, i, j, nb_etape, side, speed) = donnees
# else:

nb_fourmis = 2
liste_fourmis = ["fourmi" + str(i) for i in range(nb_fourmis)]

side = 5
grille = [side*[0] for _ in range (side)]  #numpy.array()
(droite, haut, gauche, bas) = (0, 90, 180, 270) 
nb_etape = 0
modulo = nb_etape % nb_fourmis
speed = 1.5

liste_orientation_fourmi = nb_fourmis * [droite]
liste_case_fourmi = [[side//2, side//2] for _ in range(nb_fourmis)]
liste_etat_case_fourmi = nb_fourmis * [0]

""" tests du programme """

t = 2

for p in range(t):
      (grille, liste_etat_case_fourmi[modulo], liste_orientation_fourmi[modulo], liste_case_fourmi[modulo], nb_etape, side) = step(grille, liste_etat_case_fourmi[modulo], liste_orientation_fourmi[modulo], liste_case_fourmi[modulo], nb_etape, side)
      print(liste_etat_case_fourmi, liste_orientation_fourmi, liste_case_fourmi)
      sleep(1 / speed)
      print("\n", "step", p+1, "\n")
      for k in grille:
            print(k) 
