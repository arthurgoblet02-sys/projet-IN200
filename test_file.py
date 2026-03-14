from tkinter import *
from projet_in200 import speed

window = Tk()
window.title("title")
window.geometry("100x100")

bouton_moins_10 = Button(window, text="<<<")
bouton_moins_10.pack(side=LEFT, pady=0, padx=0)

bouton_moins_1 = Button(window, text="<<")
bouton_moins_1.pack(side=LEFT, pady=10, padx=10)

bouton_moins_0_25 = Button(window, text="<")
bouton_moins_0_25.pack(side=LEFT, pady=10, padx=10)

texte_vitesse = Label(window, text="vitesse \n x" + str(speed))
texte_vitesse.pack(side=LEFT, pady=10, padx=0)

bouton_plus_0_25 = Button(window, text=">")
bouton_plus_0_25.pack(side=LEFT, pady=10, padx=10)

bouton_plus_1 = Button(window, text=">>")
bouton_plus_1.pack(side=LEFT, pady=10, padx=10)

bouton_plus_10 = Button(window, text=">>>")
bouton_plus_10.pack(side=LEFT, pady=10, padx=10)

bouton_x10 = Button(window, text="x10")
bouton_x10.pack(side=LEFT, pady=10, padx=0)

window.mainloop()
