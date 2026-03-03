from math import sin, cos, radians


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


grille = [5*[0] for _ in range (0, 5)]  #numpy
case_fourmi = grille[2][2] 
orientation_fourmi = droite
i = 2
j = 2        
nb_etape = 0

""" début du programme principal """

print(( i-int(sin(orientation_fourmi)) ) % 5, type(( i-int(sin(orientation_fourmi)) ) % 5))

def etape(grille, case_fourmi, orientation_fourmi, i, j, nb_etape):
        orientation_fourmi = ( orientation_fourmi + 270 - 180 * (case_fourmi) ) % 360
        case_fourmi = grille[( i-int(sin(orientation_fourmi)) ) % 5][( j+int(cos(orientation_fourmi)) ) % 5]
        print(i, j, grille[i][j])
        grille[i][j] += (-1)**grille[i][j]
        print(case_fourmi)
        nb_etape += 1
        (i, j) = ((i-int(sin(orientation_fourmi)) ) % 5, (j+int(cos(orientation_fourmi))) % 5)
        return (grille, case_fourmi, orientation_fourmi, i, j, nb_etape)


print((grille, case_fourmi, orientation_fourmi, i, j, nb_etape), "initialisation")

for k in range (0,1):
        (grille, case_fourmi, orientation_fourmi, i, j, nb_etape) = etape(grille, case_fourmi, orientation_fourmi, i, j, nb_etape)
        print((grille, case_fourmi, orientation_fourmi, i, j, nb_etape)) 

  



""" if event_bouton_play:
    while not event_bouton_pause:
         etape()    """