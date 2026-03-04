from math import sin, cos, radians
#  from fonctions.py import etape

""" valeurs initiales """ 

event_bouton_play = True
event_bouton_pause = False
event_bouton_next = None
(droite, haut, gauche, bas) = (0, 90, 180, 270)  

grille = [5*[0] for _ in range (0, 5)]  #  numpy.array()
case_fourmi = grille[2][2] 
orientation_fourmi = droite
(i, j) = (2, 2)      
nb_etape = 0

""" début du programme principal """

def etape(grille, case_fourmi, orientation_fourmi, i, j, nb_etape):
        orientation_fourmi = ( orientation_fourmi + 270 - 180 * (case_fourmi) ) % 360
        case_fourmi = grille[( i-int(sin(orientation_fourmi)) ) % 5][( j+int(cos(orientation_fourmi)) ) % 5]
        grille[i][j] += (-1)**grille[i][j]
        nb_etape += 1
        (i, j) = ((i-int(sin(radians(orientation_fourmi))) ) % 5, (j+int(cos(radians(orientation_fourmi)))) % 5)
        return (grille, case_fourmi, orientation_fourmi, i, j, nb_etape)  #  delete 

""" if event_bouton_play:
    while not event_bouton_pause:
         etape(grille, case_fourmi, orientation_fourmi, i, j, nb_etape) """




""" tests du programme """

print("\n initialisation", (grille, case_fourmi, orientation_fourmi, i, j, nb_etape), "\n")

for k in range (1,10):
        (grille, case_fourmi, orientation_fourmi, i, j, nb_etape) = etape(grille, case_fourmi, orientation_fourmi, i, j, nb_etape)

        print("matrice etape", k)
        for p in range (0, 5):
               print(grille[p])

        print("\n resultat", ("grille:", grille, "couleur case fourmi:", case_fourmi, "orientation fourmi:", orientation_fourmi, 
                           "ligne:", i+1, "colonne:", j+1, "etape:", nb_etape), "\n ") 
