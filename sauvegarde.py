import json 

def sauvegarde(grille, case_fourmi, orientation_fourmi, i, j, nb_etape, coté, vitesse):
    donnees = {"case_fourmi": case_fourmi,"orientation_fourmi": orientation_fourmi,"i": i,
        "j": j,"nb_etape": nb_etape,"coté": coté,"vitesse": vitesse,"grille": grille}
    fichier = open("sauvegarde.json", "w")
    json.dump(donnees, fichier)
    fichier.close()