import os 

def sauvegarde(grille, case_fourmi, orientation_fourmi, i, j, nb_etape, side, speed):
    fichier = open("sauvegarde.txt", "w")
    parametres_jeu = str(case_fourmi) + " " + str(orientation_fourmi) + " " + str(i) + " " + str(j) + " " + str(nb_etape) + " " + str(side) + " " + str(speed) + "\n"
    fichier.write(parametres_jeu)
    
    for ligne in grille:
        txt = ""
        for case in ligne:
            txt = txt + str(case) + " "
        fichier.write(txt + "\n")
    fichier.close() 

def charger():
    if os.path.exists("sauvegarde.txt"):
        fichier = open("sauvegarde.txt", "r") 
        ligne_variables = fichier.readline()
        mots = ligne_variables.split() 
            
        case_fourmi = int(mots[0])
        orientation_fourmi = int(mots[1])
        i = int(mots[2])
        j = int(mots[3])
        nb_etape = int(mots[4])
        speed = int(mots[6])
        grille = []
        for ligne in fichier:
            ligne_chiffres = []
            mots_ligne = ligne.split() 
            for case in mots_ligne:
                ligne_chiffres.append(int(case))
            if len(ligne_chiffres) > 0:
                grille.append(ligne_chiffres)
                    
        fichier.close()
        return grille, case_fourmi, orientation_fourmi, i, j, nb_etape, side, speed
        
    else:
        return None
    
    #pas encore trouvé de test. 