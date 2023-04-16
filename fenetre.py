import tkinter as tk
from bouttons import *

def score(): #pour le boutton exit, la fonction va donc montrer le score et la table sur une nouvelle fenetre (elle est pas finit)
    fenetre2=tk.Tk()
    fenetre2.title("votre partie est finie")
    label2=tk.Label(fenetre2,text="Votre score est de:",font = ("helvetica", "30"))
    label2.grid(column=0,row=0)
    label3=tk.Label(fenetre2,text=somme_valeur_grille(table))
    label3.grid(column=0,row=1)
    canvas2=tk.Canvas(fenetre2,bg="gray", height=500, width=500)

fenetre = tk.Tk() 
fenetre.title("2048") 

label1 = tk.Label(fenetre, text="2048", font = ("helvetica", "30")) 
label1.grid(column=0, row=0)


HEIGHT = 500
WIDTH = 500
largeur_case = WIDTH // 4
hauteur_case = HEIGHT // 4

canvas = tk.Canvas(fenetre, bg="gray", height=HEIGHT, width=WIDTH)
canvas.grid(column=0, row=1, rowspan=4)

for i in range(4):
    for j in range(4):
        color = "gray80"
        canvas.create_rectangle((i*largeur_case, j*hauteur_case),
        ((i+1)*largeur_case, (j+1)*hauteur_case), fill=color)
        canvas.create_text(i*largeur_case+62, j*hauteur_case+62, text="0", font=("helvetica", "30"), tags="hello")

m=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

bouton1 = tk.Button(fenetre, text="Nouvelle Partie", font=("helvetica", "10"),command=nouvelle_partie)
bouton1.grid(column=1, row=0)

bouton2 = tk.Button(fenetre, text="Exit", font=("helvetica", "10"),command=score)
bouton2.grid(column=1, row=1)

bouton3 = tk.Button(fenetre, text="Save", font=("helvetica", "10"),command=sauvegarder) 
bouton3.grid(column=1, row=2)

bouton4 = tk.Button(fenetre, text="Load", font=("helvetica", "10"),command=charger)
bouton4.grid(column=1, row=3)

fenetre.mainloop()
