" creation du fond du jeu avec le bouton jouer au milieu de l'ecran."
"IL MANQUE JUSTE DE RAJOUTER LE PLATEAU QUAND ON CLIQUE SUR LE BOUTON A LA LIGNE 17 "


from tkinter import * 
from plateau import *
#from bouton import *
from valeurs_initiales import speed 
from time import sleep 

window = Tk()
window.title("Jeu de la fourmi de Langton")
window.geometry("850x600")

fond = PhotoImage(file = "fond.png",master=window)
arriere_plan = Label(window ,image =fond) 
arriere_plan.grid(row=0, column=0, rowspan=15, columnspan=15)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1,weight=1)
frame=Frame(window)     "trouver sur internet comment utiliser frame"



def button_play():
    bouton_play.destroy()
<<<<<<< HEAD
    frame.grid(row=0,column=4,sticky="ne", padx=10,pady=10)
    plateau = Plateau (window)
    plateau.grid(row=3, column= 1 ,columnspan=5)

    
=======
    bouton_moins_10.grid(row=2, column=0, padx=100)
    bouton_moins_1.grid(row=2, column=0, padx=150)
    bouton_moins_0_25.grid(row=2, column=1, padx=50)
    texte_vitesse.grid(row=1, column=3)
    bouton_reset.grid(row=2, column=3)
    bouton_plus_0_25.grid(row=2, column=4, padx=10)
    bouton_plus_1.grid(row=2, column=5, padx=10)
    bouton_plus_10.grid(row=2, column=6, padx=10)

    #bouton_play2.grid(row=2, column=1, ipady=5, ipadx=5)
    #bouton_stop.grid(row=2, column=1, ipady=5, ipadx=5)
    #bouton_next.grid(row=2, column=1, ipady=5, ipadx=5)
    #while not on_button_pause_click:
         #(grille, case_fourmi, orientation_fourmi, i, j, nb_etape, side) = step(grille, case_fourmi, orientation_fourmi, i, j, nb_etape, side)
         #sleep(1 / speed)
    return Plateau (window), #bouton_Play, bouton_Pause, bouton_Next,#bouton_stop 
>>>>>>> 8abf1bb17ece465551c92b44d636c0a20e7cf313

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



























#bouton_moins_10.grid(row=2, column=2)
    #bouton_moins_1.grid(row=2, column=3)
    #bouton_moins_0_25.grid(row=2, column=4)
    #texte_vitesse.grid(row=1, column=5)
    #bouton_reset.grid(row=2, column=5)
    #bouton_plus_0_25.grid(row=2, column=6)
    #bouton_plus_1.grid(row=2, column=7)
    #bouton_plus_10.grid(row=2, column=8)

    #bouton_Play = Button(window, text = "Play",command=fonction_play)
    #bouton_Play.grid(row = 0,column=0,padx=20,pady=20)
    #" creer le bouton, il faut qu'il s'appelle comme ca car il est appeler comme ca dans interface graphique il ce place a gauche donc mettre row=0 ,column=0,padx=20,pady=20 quand vous le placer   "
    #bouton_Pause = Button(window, text="Pause",command=fonction_pause)
    #bouton_Pause.grid( row=1,column=0,padx=20)
    #" creer le bouton, il faut qu'il s'appelle comme ca car il est appeler comme ca dans interface graphique lui c'est row=1 ,column=0,padx=20"
    #bouton_Next = Button(window ,text="Next",command=step)
    #bouton_Next.grid(row=2, column=0, padx=20,pady=20)

"""test pour voir où sont les colonnes"""
"""l = ["bouton" + str(i) for i in range(15)]
for b in l:
n = int(b[-1])
b = Button(window, text=b[-1])
b.grid(row=2, column=n)"""
    
    #bouton_play2.grid(row=2, column=1, ipady=5, ipadx=5)
    #bouton_stop.grid(row=2, column=1, ipady=5, ipadx=5)
    #bouton_next.grid(row=2, column=1, ipady=5, ipadx=5)
    #while not on_button_pause_click:
         #(grille, case_fourmi, orientation_fourmi, i, j, nb_etape, side) = step(grille, case_fourmi, orientation_fourmi, i, j, nb_etape, side)
         #sleep(1 / speed)
    #return Plateau (window), bouton_Play, bouton_Pause, bouton_Next,#bouton_stop 