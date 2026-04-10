" creation du fond du jeu avec le bouton jouer au milieu de l'ecran."
"IL MANQUE JUSTE DE RAJOUTER LE PLATEAU QUAND ON CLIQUE SUR LE BOUTON A LA LIGNE 17 "


from tkinter import * 
import plateau
#from bouton import *
from valeurs_initiales import speed 
from time import sleep 
from fonctions import *
from PIL import Image, ImageTk

window = Tk()
window.title("Jeu de la fourmi de Langton")
window.geometry("850x600")

img = Image.open("image_jeu.png")
img = img.resize((850, 600))  
fond = ImageTk.PhotoImage(img)

arriere_plan = Label(window ,image =fond) 
arriere_plan.grid(row=0, column=0, rowspan=15, columnspan=15)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1,weight=1)
frame=Frame(window)   #"trouver sur internet comment utiliser frame"

def button_play():
    global plateau1
    bouton_play.destroy()
    frame.grid(row=0,column=4,sticky="ne", padx=10,pady=10)
    plateau1 = plateau.Plateau (window)
    plateau1.grid(row=1, column= 1 ,columnspan=5)
    bouton_Play.grid(row = 0,column=0,padx=20,pady=20)
    bouton_Pause.grid( row=1,column=0,padx=20)
    bouton_Next.grid(row=2, column=0, padx=20)

def on_button_plus_10_click():
        global speed 
        speed += 10
        if speed - int(speed) == 0:
            texte_vitesse.config(text="speed \n x" + str(int(speed)))
        else:
            texte_vitesse.config(text="speed \n x" + str((speed)))

def on_button_plus_1_click():
        global speed 
        speed += 1
        if speed - int(speed) == 0:
            texte_vitesse.config(text="speed \n x" + str(int(speed)))
        else:
            texte_vitesse.config(text="speed \n x" + str((speed)))

def on_button_plus_O_25_click():
        global speed 
        speed += 0.25
        if speed - int(speed) == 0:
            texte_vitesse.config(text="speed \n x" + str(int(speed)))
        else:
            texte_vitesse.config(text="speed \n x" + str((speed)))

def on_button_moins_10_click():
        global speed 
        if speed > 10:
            speed -= 10
        if speed - int(speed) == 0:
            texte_vitesse.config(text="speed \n x" + str(int(speed)))
        else:
            texte_vitesse.config(text="speed \n x" + str((speed)))

def on_button_moins_1_click():
        global speed 
        if speed > 1:
            speed -= 1
        if speed - int(speed) == 0:
            texte_vitesse.config(text="speed \n x" + str(int(speed)))
        else:
            texte_vitesse.config(text="speed \n x" + str((speed)))

def on_button_moins_0_25_click():
        global speed 
        if speed > 0.25:
            speed -= 0.25
        if speed - int(speed) == 0:
            texte_vitesse.config(text="speed \n x" + str(int(speed)))
        else:
            texte_vitesse.config(text="speed \n x" + str((speed)))

def on_button_reset_click():
        global speed 
        speed = 1
        if speed - int(speed) == 0:
            texte_vitesse.config(text="speed \n x" + str(int(speed)))
        else:
            texte_vitesse.config(text="speed \n x" + str((speed)))
#Bouton next play pause zayd (fonctions)



def lancer_play():
    global en_pause
    en_pause = False 
    boucle_jeu()

def mettre_pause():
    global en_pause  
    en_pause = True

def faire_un_pas():
    mettre_pause()
    next_()            
    actualiser_affichage()

def boucle_jeu(): # execute en boucle les fonctions avec un  delais de vitesse
    if not en_pause:
        next_()  
        actualiser_affichage()
        delai = int(1000 / speed) if speed > 0 else 1000
        window.after(delai, boucle_jeu) # rela,ce la boucle 
#


def actualiser_affichage():

    idx = 1
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            couleur = "black" if grille[i][j] == 1 else "white" # change une case de couleur si 1 noir sinon blanc (visuelle)
            plateau1.itemconfig(idx, fill=couleur) #color le canva 
            idx += 1 


bouton_Play = Button(window, text="Play",background="green",foreground="white", command=lancer_play)
#bouton_Play.grid(row = 0,column=0,padx=20,pady=20)
bouton_Pause = Button(window, text="Pause", background="green",foreground="white",command=mettre_pause)
bouton_Next = Button(window, text="Next",background="green",foreground="white", command=faire_un_pas)


#bouton_Play.grid(row = 0,column=0,padx=20,pady=20)
#bouton_Pause.grid( row=1,column=0,padx=20)
    #" creer le bouton, il faut qu'il s'appelle comme ca car il est appeler comme ca dans interface graphique lui c'est row=1 ,column=0,padx=20"
#bouton_Next.grid(row=2, column=0, padx=20,pady=20)
    
#


bouton_play = Button (window , text="PLAY", bg="green",fg="white", command=button_play)
bouton_play.grid(row=1 ,column=1,ipady=10,ipadx=10)
#bouton_stop = Button(window, text="QUITTER & SAUVEGARDER", bg="red", fg="white", command=quitter)
#frame=Frame(window)

bouton_moins_10 = Button(frame, text="<<<", command=on_button_moins_10_click)

bouton_moins_1 = Button(frame, text="<<", command=on_button_moins_1_click)

bouton_moins_0_25 = Button(frame, text="<", command=on_button_moins_0_25_click)

texte_vitesse = Label(frame, text="speed \n x" + str(speed))

bouton_reset = Button(frame, text="reset", command=on_button_reset_click)

bouton_plus_0_25 = Button(frame, text=">", command=on_button_plus_O_25_click)
bouton_plus_1 = Button(frame, text=">>", command=on_button_plus_1_click)

bouton_plus_10 = Button(frame, text=">>>", command=on_button_plus_10_click)
bouton_plus_10.bind("Button<1>")



bouton_moins_10.grid(row=0, column=0)
bouton_moins_1.grid(row=0, column=1)
bouton_moins_0_25.grid(row=0, column=2)
texte_vitesse.grid(row=0, column=3)
bouton_reset.grid(row=0, column=4)
bouton_plus_0_25.grid(row=0, column=5)
bouton_plus_1.grid(row=0, column=6)
bouton_plus_10.grid(row=0, column=7)


window.mainloop()

"il faudra qu'on rajoute la fourmi"




























    #bouton_Play = Button(window, text = "Play",command=fonction_play)
    #bouton_Play.grid(row = 0,column=0,padx=20,pady=20)
    #" creer le bouton, il faut qu'il s'appelle comme ca car il est appeler comme ca dans interface graphique il ce place a gauche donc mettre row=0 ,column=0,padx=20,pady=20 quand vous le placer   "
    #bouton_Pause = Button(window, text="Pause",command=fonction_pause)
    #bouton_Pause.grid( row=1,column=0,padx=20)
    #" creer le bouton, il faut qu'il s'appelle comme ca car il est appeler comme ca dans interface graphique lui c'est row=1 ,column=0,padx=20"
    #bouton_Next = Button(window ,text="Next",command=step)
    #bouton_Next.grid(row=2, column=0, padx=20,pady=20)
    
    #bouton_play2.grid(row=2, column=1, ipady=5, ipadx=5)
    #bouton_stop.grid(row=2, column=1, ipady=5, ipadx=5)
    #bouton_next.grid(row=2, column=1, ipady=5, ipadx=5)
    #while not on_button_pause_click:
         #(grille, case_fourmi, orientation_fourmi, i, j, nb_etape, side) = step(grille, case_fourmi, orientation_fourmi, i, j, nb_etape, side)
         #sleep(1 / speed)
    #return Plateau (window), bouton_Play, bouton_Pause, bouton_Next,#bouton_stop 