from tkinter import *
from projet_in200 import speed

window = Tk()
window.geometry("850x600")

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

bouton_moins_10 = Button(window, text="<<<", command=on_button_moins_10_click)

bouton_moins_1 = Button(window, text="<<", command=on_button_moins_1_click)

bouton_moins_0_25 = Button(window, text="<", command=on_button_moins_0_25_click)

texte_vitesse = Label(window, text="speed \n x" + str(speed))

bouton_reset = Button(window, text="reset", command=on_button_reset_click)

bouton_plus_0_25 = Button(window, text=">", command=on_button_plus_O_25_click)

bouton_plus_1 = Button(window, text=">>", command=on_button_plus_1_click)

bouton_plus_10 = Button(window, text=">>>", command=on_button_plus_10_click)

bouton_moins_10.pack(side=LEFT)
bouton_moins_1.pack(side=LEFT)
bouton_moins_0_25.pack(side=LEFT)
texte_vitesse.pack(side=LEFT)
bouton_reset.pack(side=LEFT)
bouton_plus_0_25.pack(side=LEFT)
bouton_plus_1.pack(side=LEFT)
bouton_plus_10.pack(side=LEFT)

window.mainloop()