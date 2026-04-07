from valeurs_initiales import *
from fonctions import next_, back_
from time import sleep


"""                          -  tests du programme  -                         """

steps = 10

for k in range(steps):
      next_()
      sleep(1 / speed)
      print("\n", "step", k+1, "\n")
      for k in grille:
            print(k) 
      print("\n", liste_orientation_fourmi, liste_case_fourmi)