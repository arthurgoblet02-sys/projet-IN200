" creation du fond du jeu avec le bouton jouer au milieu de l'ecran."
"IL MANQUE JUSTE DE RAJOUTER LE PLATEAU QUAND ON CLIQUE SUR LE BOUTON A LA LIGNE 17 "


from tkinter import * 
from plateau import *
#from bouton import *
from projet_in200 import speed 
from time import sleep 

window = Tk()
window.title("Jeu de la fourmi de Langton")
window.geometry("850x600")

fond = PhotoImage(file = "fond.png",master=window)
arriere_plan = Label(window ,image =fond) 
arriere_plan.grid(row=0, column=0, rowspan=15, columnspan=15)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1,weight=1)


def button_play():
    bouton_play.destroy()
    bouton_moins_10.grid(row=2, column=0)
    bouton_moins_1.grid(row=2, column=1)
    bouton_moins_0_25.grid(row=2, column=2)
    texte_vitesse.grid(row=1, column=3)
    bouton_reset.grid(row=2, column=4)
    bouton_plus_0_25.grid(row=2, column=5)
    bouton_plus_1.grid(row=2, column=6)
    bouton_plus_10.grid(row=2, column=7)

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
    return Plateau (window), #bouton_Play, bouton_Pause, bouton_Next,#bouton_stop 

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
# bouton_stop = Button(window, text="QUITTER & SAUVEGARDER", bg="red", fg="white", command=quitter)

bouton_moins_10 = Button(window, text="<<<", command=on_button_moins_10_click)

bouton_moins_1 = Button(window, text="<<", command=on_button_moins_1_click)

bouton_moins_0_25 = Button(window, text="<", command=on_button_moins_0_25_click)

texte_vitesse = Label(window, text="speed \n x" + str(speed))

bouton_reset = Button(window, text="reset", command=on_button_reset_click)

bouton_plus_0_25 = Button(window, text=">", command=on_button_plus_O_25_click)

bouton_plus_1 = Button(window, text=">>", command=on_button_plus_1_click)

bouton_plus_10 = Button(window, text=">>>", command=on_button_plus_10_click)

window.mainloop()

"il faudra qu'on rajoute la fourmi"






