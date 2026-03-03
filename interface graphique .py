" creation du fond du jeu avec le bouton jouer au milieu de l'ecran "


from tkinter import *

window = Tk()
window.title("Jeu de la fourmi de Langton")
window.geometry("800x600")

fond = PhotoImage(file = "fond.png")
arriere_plan = Label(window ,image =fond) 
arriere_plan.grid(row=0, column=0, rowspan=3, columnspan=3)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1,weight=1)
def on_button_click():
    bouton_jouer.config(text="rajouter le plateau")

bouton_jouer = Button (window , text="JOUER", bg="green", command=on_button_click)
bouton_jouer.grid(row=1 ,column=1)

window.mainloop()

