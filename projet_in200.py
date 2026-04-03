from fonctions import step, back_step
from time import sleep

""" valeurs initiales """ 

event_bouton_play = True
event_bouton_pause = False
event_bouton_next = False
(droite, haut, gauche, bas) = (0, 90, 180, 270)  

side = 25
orientation_fourmi = droite
(i, j) = (side // 2, side // 2) 

grille = [side*[0] for _ in range (side)]  #numpy.array()
case_fourmi = grille[i][j]      
nb_etape = 0
speed = 100

""" début du programme principal """

""" if event_bouton_play:
    while not event_bouton_pause:
         etape(grille, case_fourmi, orientation_fourmi, i, j, nb_etape) """


""" tests du programme """

t = 10

for p in range(t):
      (grille, case_fourmi, orientation_fourmi, i, j, nb_etape, side) = step(grille, case_fourmi, orientation_fourmi, i, j, nb_etape, side)
      sleep(1 / speed)
      print("\n", "step", p+1, "\n")
      for k in grille:
            print(k) 
