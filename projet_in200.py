from math import cos, sin 



""" représentation de la grille 

[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]

"""

""" valeurs initiales """


droite = 0   
haut = 90            
gauche = 180    
bas = 270       

event_bouton_play = True
event_bouton_pause = False
event_bouton_next = None

grille = 5*[5*[0]]  #numpy
case_fourmi = grille[2][2] 
i = 2
j = 2        
orientation_fourmi = droite
nb_etape = 0

""" début du programme principal """

def etape():
        orientation_fourmi = ( orientation_fourmi + 270 - 180(case_fourmi) ) % 360
        case_fourmi = grille[( i-sin(orientation_fourmi) ) % 5][( j+cos(orientation_fourmi) ) % 5]
        grille[i][j] += (-1)**grille[i][j]
        (i, j) = (i-sin(orientation_fourmi), j+cos(orientation_fourmi))
        return grille



""" if event_bouton_play:
    while not event_bouton_pause:
         etape()    """



for _ in range (0, 10):
        etape


print(grille)



