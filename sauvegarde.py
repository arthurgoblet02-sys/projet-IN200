import json 

def sauvegarde(grille, case_fourmi, orientation_fourmi, i, j, nb_etape, side, speed):
    # 1. On stocke toutes tes variables dans un dictionnaire
    donnees = {"case_fourmi": case_fourmi,"orientation_fourmi": orientation_fourmi,"i": i,
        "j": j,"nb_etape": nb_etape,"side": side,"speed": speed,"grille": grille}