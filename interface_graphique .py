" creation du fond du jeu avec le bouton jouer au milieu de l'ecran."
"IL MANQUE JUSTE DE RAJOUTER LE PLATEAU QUAND ON CLIQUE SUR LE BOUTON A LA LIGNE 17 "


from tkinter import * 
from plateau import *
from bouton import *

window = Tk()
window.title("Jeu de la fourmi de Langton")
window.geometry("850x600")

fond = PhotoImage(file = "fond.png")
arriere_plan = Label(window ,image =fond) 
arriere_plan.grid(row=0, column=0, rowspan=3, columnspan=3)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1,weight=1)



def on_button_click():
    bouton_play.destroy()
    return Plateau (window), bouton_Play, bouton_Pause, bouton_Next
    

bouton_play = Button (window , text="PLAY", bg="green",fg="white", command=on_button_click)
bouton_play.grid(row=1 ,column=1,ipady=10,ipadx=10)

window.mainloop()

"il faudra qu'on rajoute la fourmi"

