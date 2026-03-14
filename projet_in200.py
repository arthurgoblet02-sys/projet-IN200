from fonctions import step, back_step
from time import time 

""" valeurs initiales """ 

start = time()

event_bouton_play = True
event_bouton_pause = False
event_bouton_next = None
(droite, haut, gauche, bas) = (0, 90, 180, 270)  

side = 25
grille = [side*[0] for _ in range (0, side)]  #numpy.array()
case_fourmi = grille[side // 2][side // 2] 
orientation_fourmi = droite
(i, j) = (side // 2, side // 2)      
nb_etape = 0

""" début du programme principal """

""" if event_bouton_play:
    while not event_bouton_pause:
         etape(grille, case_fourmi, orientation_fourmi, i, j, nb_etape) """


""" tests du programme """

t = 10

for _ in range(0,t):
      (grille, case_fourmi, orientation_fourmi, i, j, nb_etape, side) = step(grille, case_fourmi, orientation_fourmi, i, j, nb_etape, side)

for _ in range(0,t):
      (grille, case_fourmi, orientation_fourmi, i, j, nb_etape, side) = back_step(grille, case_fourmi, orientation_fourmi, i, j, nb_etape, side)



end = time()

print("time =", end - start, "s")