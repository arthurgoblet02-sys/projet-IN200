from tkinter import *
from projet_in200 import speed

window = Tk()
window.title("title")
window.geometry("850x600")

y = 100
x = 0

bouton_moins_10 = Button(window, text="<<<")
bouton_moins_10.pack(pady=y, padx=x, expand=True)

bouton_moins_1 = Button(window, text="<<")
bouton_moins_1.pack(pady=y, padx=x, expand=True)

bouton_moins_0_25 = Button(window, text="<")
bouton_moins_0_25.pack(pady=y, padx=x, expand=True)

texte_vitesse = Label(window, text="vitesse \n x" + str(speed))
texte_vitesse.pack(pady=y, padx=x, expand=True)

bouton_plus_0_25 = Button(window, text=">")
bouton_plus_0_25.pack(pady=y, padx=x, expand=True)

bouton_plus_1 = Button(window, text=">>")
bouton_plus_1.pack(pady=y, padx=x, expand=True)

bouton_plus_10 = Button(window, text=">>>")
bouton_plus_10.pack(pady=y, padx=x, expand=True)

bouton_x10 = Button(window, text="x10")
bouton_x10.pack(pady=y, padx=x, expand=True)

window.mainloop()
