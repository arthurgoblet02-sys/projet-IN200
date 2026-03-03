""" représentation de la grille 

[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]

0 0 
1 0 
2 1 
3 1 

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
orientation_fourmi = droite
nb_etape = 0

""" début du programme principal """

def etape():
        if case_fourmi == 0:
            orientation_fourmi = (orientation_fourmi - 90) % 360
            case_fourmi = None 
        if case_fourmi == 1:
            orientation_fourmi = (orientation_fourmi + 90) % 360

if event_bouton_play:
    while not event_bouton_pause:
         etape()    






print(grille)



