import json 

def fonction_sauvegarde():
    global grille, liste_case_fourmi, liste_orientation_fourmi, nb_etape, side, speed, nb_fourmis, liste_etat_case_fourmi
    
    # on utilise dictionaire pour stocker les valeur du jeu
    donnees = {"liste_case_fourmi": liste_case_fourmi,"liste_orientation_fourmi": liste_orientation_fourmi,"nb_etape": nb_etape,
        "side": side,"speed": speed,"nb_fourmis": nb_fourmis,"liste_etat_case_fourmi": liste_etat_case_fourmi,"grille": grille}
    
    # 1. On ouvre en mode écriture grace a la commande "w"
    fichier = open("sauvegarde.json", "w")
     
    json.dump(donnees, fichier) #vu sur internet que on écrit dans le fichier a l'aide de .dump
    fichier.close()
    print("Partie sauvegardée avec succès !")

