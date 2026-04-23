import json
from valeurs_initiales import *

def fonction_sauvegarde():
    donnees = {"liste_case_fourmi": liste_case_fourmi,"liste_orientation_fourmi": liste_orientation_fourmi,"nb_etape": nb_etape,"side": side,
        "speed": speed,"nb_fourmis": nb_fourmis,"liste_etat_case_fourmi": liste_etat_case_fourmi,"grille": grille}
    
    nom_partie = input("\nNom de la sauvegarde : ")
    nom_fichier = nom_partie + ".json"
    
    fichier = open(nom_fichier, "w")
    json.dump(donnees, fichier)
    fichier.close()
    
    print("Super ! Partie sauvegardée sous le nom :", nom_fichier)

def fonction_charger():
    nom_partie = input("\n Fichier a charger : ")
    nom_fichier = nom_partie + ".json"
    # J'ai  essaye avec un if/else, mais la fonction open() fait planter
    # le jeu plantae  direct si le joueur se trompe de nom de fichier. 
    # J'ai trouve cette methode (try/except) sur internet pour eviter le crash 
    #via https://www.w3schools.com/python/python_try_except.asp:
    
    try:
        fichier = open(nom_fichier, "r")
        donnees = json.load(fichier)
        fichier.close()
        grille.clear()
        grille.extend(donnees["grille"])
        
        liste_case_fourmi.clear()
        liste_case_fourmi.extend(donnees["liste_case_fourmi"])
        
        liste_orientation_fourmi.clear()
        liste_orientation_fourmi.extend(donnees["liste_orientation_fourmi"])
        
        liste_etat_case_fourmi.clear()
        liste_etat_case_fourmi.extend(donnees["liste_etat_case_fourmi"])
        
        # Pour les variables simples (les nombres)
        global nb_etape, side, speed, nb_fourmis
        nb_etape = donnees["nb_etape"]
        side = donnees["side"]
        speed = donnees["speed"]
        nb_fourmis = donnees["nb_fourmis"]
        
        print("C'est bon, la partie", nom_fichier, "a été chargée !")
        
    except FileNotFoundError:
        print("Erreur : Aucune sauvegarde trouvée avec ce nom (" + nom_fichier + ").")