import json 

def fonction_sauvegarde():
    # On va chercher les variables globales directement dans le programme
    global grille, liste_case_fourmi, liste_orientation_fourmi, nb_etape, side, speed, nb_fourmis, liste_etat_case_fourmi
    
    # On stocke toutes les variables actuelles du jeu
    donnees = {"liste_case_fourmi": liste_case_fourmi,"liste_orientation_fourmi": liste_orientation_fourmi,"nb_etape": nb_etape,
        "side": side,"speed": speed,"nb_fourmis": nb_fourmis,"liste_etat_case_fourmi": liste_etat_case_fourmi,"grille": grille}
    
    # 1. On ouvre en mode écriture
    fichier = open("sauvegarde.json", "w")
    # 2. On écrit dans le fichier
    json.dump(donnees, fichier)
    # 3. On ferme le fichier
    fichier.close()
    print("Partie sauvegardée avec succès !")

