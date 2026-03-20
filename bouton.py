" il faut creer tout les bouton demander dans le sujet donc le bouton play, pause et etapes. lire le sujet pour savoir ce que font ces bouton."
"les fonction que vous aller mettre dans command a la creation du bouton faut les rajouter dans le fichier fonction "

from fonctions import *
from tkinter import *
bouton_Play = Button(text = "Play",command=fonction_play)
bouton_Play.grid(row = 0,column=0,padx=20,pady=20)
" creer le bouton, il faut qu'il s'appelle comme ca car il est appeler comme ca dans interface graphique il ce place a gauche donc mettre row=0 ,column=0,padx=20,pady=20 quand vous le placer   "
bouton_Pause = Button(text="Pause",command=fonction_pause)
bouton_Pause.grid(row=1,column=0,padx=20)
" creer le bouton, il faut qu'il s'appelle comme ca car il est appeler comme ca dans interface graphique lui c'est row=1 ,column=0,padx=20"
bouton_Next = Button(text="Next",command=etape)
bouton_Next.grid(row=2, column=0, padx=20,pady=20)

