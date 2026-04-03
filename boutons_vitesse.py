from tkinter import *
from projet_in200 import speed

def on_button_x10_click():
        global speed 
        speed *= 10
        if speed - int(speed) == 0:
            texte_vitesse.config(text="vitesse \n x" + str(int(speed)))
        else:
            texte_vitesse.config(text="vitesse \n x" + str((speed)))
                

def on_button_plus_10_click():
        global speed 
        speed += 10
        if speed - int(speed) == 0:
            texte_vitesse.config(text="vitesse \n x" + str(int(speed)))
        else:
            texte_vitesse.config(text="vitesse \n x" + str((speed)))

def on_button_plus_1_click():
        global speed 
        speed += 1
        if speed - int(speed) == 0:
            texte_vitesse.config(text="vitesse \n x" + str(int(speed)))
        else:
            texte_vitesse.config(text="vitesse \n x" + str((speed)))

def on_button_plus_O_25_click():
        global speed 
        speed += 0.25
        if speed - int(speed) == 0:
            texte_vitesse.config(text="vitesse \n x" + str(int(speed)))
        else:
            texte_vitesse.config(text="vitesse \n x" + str((speed)))

def on_button_moins_10_click():
        global speed 
        speed -= 10
        if speed - int(speed) == 0:
            texte_vitesse.config(text="vitesse \n x" + str(int(speed)))
        else:
            texte_vitesse.config(text="vitesse \n x" + str((speed)))

def on_button_moins_1_click():
        global speed 
        speed -= 1
        if speed - int(speed) == 0:
            texte_vitesse.config(text="vitesse \n x" + str(int(speed)))
        else:
            texte_vitesse.config(text="vitesse \n x" + str((speed)))

def on_button_moins_0_25_click():
        global speed 
        speed -= 0.25
        if speed - int(speed) == 0:
            texte_vitesse.config(text="vitesse \n x" + str(int(speed)))
        else:
            texte_vitesse.config(text="vitesse \n x" + str((speed)))

def on_button_reset_click():
        global speed 
        speed = 1
        if speed - int(speed) == 0:
            texte_vitesse.config(text="vitesse \n x" + str(int(speed)))
        else:
            texte_vitesse.config(text="vitesse \n x" + str((speed)))

def on_button_div10_click():
        global speed 
        speed /= 10
        if speed - int(speed) == 0:
            texte_vitesse.config(text="vitesse \n x" + str(int(speed)))
        else:
            texte_vitesse.config(text="vitesse \n x" + str((speed)))

     


window = Tk()
window.title("title")
window.geometry("850x600")

bouton_div_10 = Button(window, text="/10", command=on_button_div10_click)

bouton_moins_10 = Button(window, text="<<<", command=on_button_moins_10_click)

bouton_moins_1 = Button(window, text="<<", command=on_button_moins_1_click)

bouton_moins_0_25 = Button(window, text="<", command=on_button_moins_0_25_click)

texte_vitesse = Label(window, text="vitesse \n x" + str(speed))

bouton_reset = Button(window, text="reset", command=on_button_reset_click)
bouton_reset.grid(row=3, column=35, padx=15, ipadx=10, ipady=5)

bouton_plus_0_25 = Button(window, text=">", command=on_button_plus_O_25_click)

bouton_plus_1 = Button(window, text=">>", command=on_button_plus_1_click)

bouton_plus_10 = Button(window, text=">>>", command=on_button_plus_10_click)

bouton_x10 = Button(window, text="x10", command=on_button_x10_click)

bouton_div_10.grid(row=3, column=15, padx=15, ipadx=10, ipady=5)
bouton_moins_10.grid(row=3, column=20, ipadx=10, ipady=5)
bouton_moins_1.grid(row=3, column=25, padx=15, ipadx=10, ipady=5)
bouton_moins_0_25.grid(row=3, column=30, ipadx=10, ipady=5)
texte_vitesse.grid(rowspan=1, columnspan=1, row=1, column=35, ipadx=10, ipady=5, padx=10)
bouton_plus_0_25.grid(row=3, column=40, ipadx=10, ipady=5)
bouton_plus_1.grid(row=3, column=45, padx=15, ipadx=10, ipady=5)
bouton_plus_10.grid(row=3, column=50, ipadx=10, ipady=5)
bouton_x10.grid(row=3, column=55, padx=15, ipadx=10, ipady=5)

window.mainloop()
