import tkinter as tk

fenetre = tk.Tk() 
fenetre.title("2048") 

label1 = tk.Label(fenetre, text="2048", font = ("helvetica", "30")) 
label1.grid(column=0, row=0,rowspan=4)


HEIGHT = 500
WIDTH = 500
largeur_case = WIDTH // 4
hauteur_case = HEIGHT // 4

canvas = tk.Canvas(fenetre, bg="gray", height=HEIGHT, width=WIDTH)
canvas.grid()

for i in range(4):
    for j in range(4):
        color = "gray80"
        canvas.create_rectangle((i*largeur_case, j*hauteur_case),
        ((i+1)*largeur_case, (j+1)*hauteur_case), fill=color)

bouton1 = tk.Button(fenetre, text="Nouveau Partie", font=("helvetica", "10"))
bouton1.grid(column=1, row=0)

bouton2 = tk.Button(fenetre, text="Exit", font=("helvetica", "10"))
bouton2.grid(column=1, row=1)

bouton3 = tk.Button(fenetre, text="Save", font=("helvetica", "10"))
bouton3.grid(column=1, row=2)

bouton4 = tk.Button(fenetre, text="Load", font=("helvetica", "10"))
bouton4.grid(column=1, row=3)

fenetre.mainloop()