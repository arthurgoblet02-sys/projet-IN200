" creation du fond du jeu avec le bouton jouer au milieu de l'ecran."
"IL MANQUE JUSTE DE RAJOUTER LE PLATEAU QUAND ON CLIQUE SUR LE BOUTON A LA LIGNE 17 "


from tkinter import * 
from plateau import *
from bouton import *

fenetre = Tk()
fenetre.title("Jeu de la fourmi de Langton")
fenetre.geometry("850x600")

fond = PhotoImage(file = "fond.png",master=fenetre)
arriere_plan = Label(fenetre ,image =fond) 
arriere_plan.grid(row=0, column=0, rowspan=3, columnspan=3)
fenetre.grid_rowconfigure(1, weight=1)
fenetre.grid_columnconfigure(1,weight=1)


def button_jouer():
    bouton_play.destroy()
    # bouton_stop.grid(row=2, column=1, ipady=5, ipadx=5)
    return Plateau (fenetre), bouton_Play, bouton_Pause, bouton_Next,#bouton_stop 
    

bouton_play = Button (fenetre , text="PLAY", bg="green",fg="white", command=button_jouer)
bouton_play.grid(row=1 ,column=1,ipady=10,ipadx=10)
# bouton_stop = Button(window, text="QUITTER & SAUVER", bg="red", fg="white", command=quitter)

fenetre.mainloop()

"il faudra qu'on rajoute la fourmi"

