
"lien de la doc utiliser par ARTHUR : https://tkdocs.com/tutorial/index.html "


from tkinter import * 
from random import randint
import plateau
from valeurs_initiales import speed
import valeurs_initiales as val
from fonctions import *
from sauvegarde import* #seydou
from PIL import Image, ImageTk
from math import cos, sin, radians

"ARTHUR" + "ZAYD"

window = Tk()
window.title("Jeu de la fourmi de Langton")
window.geometry("850x600")
dessins_fourmis = []
en_pause = True

"HELIO"

menubar = Menu(window)
menu_settings  = Menu(menubar, tearoff=0)
menubar.add_cascade(label="settings", menu=menu_settings)

"ARTHUR"

img = Image.open("cycle-vie-fourmis.jpeg")
img = img.resize((850, 600))  
fond = ImageTk.PhotoImage(img)

arriere_plan = Label(window ,image =fond) 
arriere_plan.grid(row=0, column=0, rowspan=15, columnspan=15)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1,weight=1)
frame=Frame(window,bg="green") 
frame2 = Frame(window)  
frame3 = Frame(window,bg="green")
frame4 = Frame(window,bg="red")

def ok ():
    frame4.grid_forget()
    frame3.grid(row=0,column=1)

def nombre (val):
    if val =="":
          return False
    for c in val :
        if ord(c) < ord("0") or ord(c) > ord("9"):
            return False
    return True


def recuperer ():
    global champs_nb_fourmis
    valeur = champs_nb_fourmis.get()
    if nombre(valeur) : 
        val.nb_fourmis = int(valeur)
        val.liste_case_fourmi = [[side//2, side//2] for _ in range(val.nb_fourmis)]
        val.liste_orientation_fourmi = val.nb_fourmis * [0]
        val.liste_etat_case_fourmi = val.nb_fourmis * [0]
        frame3.grid_forget()    
    else:
        frame3.grid_forget()
        frame4.grid(row=0,column=1)


def nb_fourmi():
    frame3.grid(row=0,column=1)



def button_play():
    global plateau1
    bouton_play.destroy()
    bouton_Charger.destroy()
    texte.destroy()
    frame.grid(row=0,column=4,sticky="ne", padx=10,pady=10)
    frame2.grid(row=1,column=5,padx=10,pady=10)
    plateau1 = plateau.Plateau (window)
    plateau1.grid(row=1, column= 1 ,columnspan=5)
    bouton_Play.grid(row = 0,column=0,padx=20,pady=20)
    bouton_Pause.grid( row=1,column=0,padx=20)
    bouton_Next.grid(row=2, column=0, padx=20)
    plateau1.bind("<Button-1>", gestion_clic)
    

"HELIO"


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


"ZAYD"

def gestion_clic(event):
    if en_pause:
        taille_case = 500/val.side
        j = int(event.x /taille_case)
        i = int(event.y /taille_case)
        if 0<=i < val.side and 0 <= j < val.side:
            if grille[i][j]==0:
                grille[i][j] = 1 
            else:
                grille[i][j]=0
            actualiser_affichage()

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
        delai = int(1000 / speed)
        window.after(delai, boucle_jeu) # relance la boucle 

#compteur de pas 
compteur_de_pas = Label(frame,text= "Pas:0",bg="green",fg="white",font=("Arial",12,"bold"))
compteur_de_pas.grid(row=1,column=3,columnspan=2)

def actualiser_affichage():
    global dessins_fourmis
    idx = 1
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j]==1:
                couleur = "black"
            elif grille[i][j] == 0:
                couleur = "white"
            elif grille[i][j] == 2:
                couleur = "blue"
            else : 
                couleur ="red" 
            plateau1.itemconfig(idx, fill=couleur) #color le canva 
            idx += 1 
    #maj du compteur 
    compteur_de_pas.config(text="Pas : " + str(val.nb_etape))
    
    # on dessine lafourmi 

    for d in dessins_fourmis:
        plateau1.delete(d)
    dessins_fourmis = []

    taille_case = 500/ val.side #sert a avoir les mesures de la case

    for k in range(val.nb_fourmis):
        i = val.liste_case_fourmi[k][0]
        j = val.liste_case_fourmi[k][1]

        angle = val.liste_orientation_fourmi[k]
        x_centre =  j * taille_case +   (taille_case/2)
        y_centre= i * taille_case + (taille_case/2)
        
        longeur = taille_case*0.4   
        x1= x_centre + longeur *cos(radians(angle))
        y1 = y_centre - longeur * sin(radians(angle))

        x2 = x_centre + longeur *cos(radians(angle +140))
        y2 =y_centre - longeur * sin(radians(angle +140))

        x3 = x_centre + longeur *cos(radians(angle -140))
        y3 =y_centre - longeur * sin(radians(angle -140))
        
        fourmi_triangle = plateau1.create_polygon(x1,y1,x2,y2,x3,y3,fill='red',outline='black')

        dessins_fourmis.append(fourmi_triangle)

# Bouton reset
def on_button_reset():
    global grille
    val.nb_etape = 0
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            grille[i][j] = 0
            actualiser_affichage()

bouton_reset = Button(frame2,text="Reset", background="red", foreground="white", command=on_button_reset)
bouton_reset.grid(row=0,column=2)

#bouton back
def backbutton():
    mettre_pause()
    back_()
    actualiser_affichage()
    
bouton_back = Button(frame2,text = "Back",background="green",foreground="white",command=backbutton)
bouton_back.grid(row=0,column=1)



bouton_Play = Button(window, text="Play",background="green",foreground="white", command=lancer_play)

bouton_Pause = Button(window, text="Pause", background="green",foreground="white",command=mettre_pause)
bouton_Next = Button(window, text="Next",background="green",foreground="white", command=faire_un_pas)

def afficher_credit():
    mettre_pause()

    plateau1.grid_forget()
    frame.grid_forget()
    frame2.grid_forget()
    bouton_Play.grid_forget()
    bouton_Pause.grid_forget()
    bouton_Next.grid_forget()

    frame_credit = Frame(window,bg="green",bd = 5,relief='ridge')
    frame_credit.grid(row=1,column=1,padx=20,pady=20)

    textedefin = "GAME OVER\n\nCreated By :\n\nArthur Goblet\nHelio Lancon\nZayd Hmadounacer\nSeydou Sylla "
    label_credits = Label(frame_credit,text=textedefin,font=("Arial",18,"bold"),bg ='green',fg='white',justify="center")
    label_credits.pack(padx=20,pady=20)

    bouton_quitter = Button(frame_credit,text="Quitter",command=window.quit,bg="red",fg="white",font=("Arial",12,"bold"))
    bouton_quitter.pack(pady=20)

    
bouton_fin = Button(frame2, text="FIN", background="blue", foreground="white", command=afficher_credit)
bouton_fin.grid(row=0, column=3, padx=1) 





"HELIO + ARTHUR pour le frame "


bouton_moins_10 = Button(frame, text="<<<",bg="green",fg="white", command=on_button_moins_10_click)

bouton_moins_1 = Button(frame, text="<<",bg="green",fg="white", command=on_button_moins_1_click)

bouton_moins_0_25 = Button(frame, text="<",bg="green",fg="white", command=on_button_moins_0_25_click)

texte_vitesse = Label(frame, text="speed \n x" + str(speed),bg="green",fg="white")

bouton_reset_vitesse = Button(frame, text="reset",bg="green",fg="white", command=on_button_reset_click)

bouton_plus_0_25 = Button(frame, text=">",bg="green",fg="white", command=on_button_plus_O_25_click)
bouton_plus_1 = Button(frame, text=">>",bg="green",fg="white", command=on_button_plus_1_click)

bouton_plus_10 = Button(frame, text=">>>",bg="green",fg="white", command=on_button_plus_10_click)
bouton_plus_10.bind("Button<1>")
"ARTHUR"

bouton_moins_10.grid(row=0, column=0)
bouton_moins_1.grid(row=0, column=1)
bouton_moins_0_25.grid(row=0, column=2)
texte_vitesse.grid(row=0, column=3)
bouton_reset_vitesse.grid(row=0, column=4)
bouton_plus_0_25.grid(row=0, column=5)
bouton_plus_1.grid(row=0, column=6)
bouton_plus_10.grid(row=0, column=7)

bouton_play = Button (window , text="PLAY", bg="green",fg="white", command=button_play,font=("Arial", 15))
bouton_play.grid(row=1 ,column=1)

texte= Label(window,text="LA FOURMI DE LANGTON !!",bg='green',fg= "black",font=("Arial", 30))
texte.grid(row=0 ,column=1)


champs_nb_fourmis = Entry(frame3)
champs_nb_fourmis.grid(row=0,column=1)

bouton_valider= Button(frame3,text="valider",bg="green",fg="white",command= recuperer)
bouton_valider.grid(row=0, column=0 )

message = Label(frame4, text= "Ce n'est pas un nombre. Entrez un nombre s'il vous plaît.",fg="black",bg="red")
message.grid(row=0,column=1)

bouton_ok=Button(frame4,text="ok",bg="red",fg="black",command= ok)
bouton_ok.grid(row=1,column=1)


"SEYDOU + ARTHUR"
    

bouton_Charger = Button(window, text="Charger",bg="green",fg="black", command=fonction_charger)
bouton_Charger.grid(row=1 ,column=0)



"ARTHUR"
menu_settings.add_command(label="nb_fourmi", command=nb_fourmi)
menu_settings.add_command(label="SAUVEGARDER", command=fonction_sauvegarde)


window.config(menu=menubar)





window.mainloop()

"FIN"
