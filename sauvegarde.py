import json 

def fonction_sauvegarde():
    global grille, liste_case_fourmi, liste_orientation_fourmi, nb_etape, side, speed, nb_fourmis, liste_etat_case_fourmi
    
    # on utilise dictionaire pour stocker les valeur du jeu
    donnees = {"liste_case_fourmi": liste_case_fourmi,"liste_orientation_fourmi": liste_orientation_fourmi,"nb_etape": nb_etape,
        "side": side,"speed": speed,"nb_fourmis": nb_fourmis,"liste_etat_case_fourmi": liste_etat_case_fourmi,"grille": grille}
    
    # 1. On ouvre en mode écriture grace a la commande "w"
    fichier = open("sauvegarde.json", "w")
     
    json.dump(donnees, fichier) #vu sur internet que on écrit les données dans le fichier a l'aide de .dump
    fichier.close()
    print("Partie sauvegardée avec succès !")

    def fonction_charger():
        fichier = open("sauvegarde.json", "r")
        donnees = json.load(fichier)#lit le fichier json en mode lecture et le transforme en dictionnaire
    fichier.close()
    global grille, liste_case_fourmi, liste_orientation_fourmi, nb_etape, side, speed, nb_fourmis, liste_etat_case_fourmi
    # Ici manque à remplacer les valeurs par celles de la sauvegarde.
    # je pense a cela car c'est comme ca qu'on modifie les dictionnaires
    # Exemple : grille = donnees["grille"] 
    grille = donnees["grille"]
    liste_case_fourmi = donnees["liste_case_fourmi"]
    liste_orientation_fourmi = donnees["liste_orientation_fourmi"]
    nb_etape = donnees["nb_etape"]
    side = donnees["side"] 
    speed = donnees["speed"]
    nb_fourmis = donnees["nb_fourmis"]
    liste_etat_case_fourmi = donnees["liste_etat_case_fourmi"] #mais pas sur #