""" représentation de la grille 

[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]

0 r l
90 u d

"""


""" valeurs initiales """


droite = 0     
haut = 90   -1
gauche = 180    
bas = 270  1

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
        if case_fourmi == 0:
            orientation_fourmi = (orientation_fourmi - 90) % 360                 
            
            if orientation_fourmi % 180 == 0:
                 case_fourmi = grille[i][j - (orientation_fourmi % 90) + 1]
                 grille[i][j] = 1
                 j -= (orientation_fourmi % 90) - 1
            
            else:
                 case_fourmi = grille[i - (orientation_fourmi % 135) + 1][j]
                 grille[i][j] = 1
                 i -= (orientation_fourmi % 135) - 1    
        
        if case_fourmi == 1:
            orientation_fourmi = (orientation_fourmi + 90) % 360

            if orientation_fourmi % 180 == 0:
                 case_fourmi = grille[i][j - (orientation_fourmi % 90) + 1]
                 grille[i][j] = 0
                 j -= (orientation_fourmi % 90) - 1
            
            else:
                 case_fourmi = grille[i - (orientation_fourmi % 135) + 1][j]
                 grille[i][j] += (-1) ** grille[i][j]
                 i -= (orientation_fourmi % 135) - 1 



if event_bouton_play:
    while not event_bouton_pause:
         etape()    






print(grille)



