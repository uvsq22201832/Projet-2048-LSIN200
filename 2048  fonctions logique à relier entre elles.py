#1 On met en place notre environnement de travail
import tkinter as tk  

#transposer
#compresser la grille
#grille de fusion
#cellule aléatoire
 
###BROUILLON###

#Les couleurs des différentes cases en fonction du nombre écrit sur celle-ci à l'aide de 2 dictionnaires:

bg_color={'2': '#eee4da','4': '#ede0c8','8': '#edc850',
          '16': '#edc53f','32': '#f67c5f','64': '#f65e3b','128': '#edcf72',
          '256': '#edcc61','512': '#f2b179',
        '1024': '#f59563','2048': '#edc22e',}

color={ '2': '#776e65', '4': '#f9f6f2','8': '#f9f6f2','16': '#f9f6f2',
       '32': '#f9f6f2','64': '#f9f6f2','128': '#f9f6f2',
        '256': '#f9f6f2','512': '#776e65','1024': '#f9f6f2','2048': '#f9f6f2',}

tableau=tk.Tk()
tableau.title("2048")
label=tk.Label(tableau,text="Test",fg='red',bg='pink')
label.grid()

def score():
    pass

def transposition():
    pass

tableau.mainloop()

###FIN BROUILLON###

# Partie "Logistique"
import random

def debut_2048(): # Fonction pour initialiser/commencer le jeu.
    
  mat=[[0]*4 for i in range(4)] # On créer notre grille 4x4
  
  # Affichage des commandes
  
  print("Liste des commandes : ")
  print("'Z': Haut")
  print("'S': Bas")
  print("'Q': Gauche")
  print("'D': Droite")

  ajout_2(mat)
  return mat
 
# fonction d'ajout d'un 2 dans une case vide la grille 4x4

def ajout_2(mat):
 
   # choix d'un chiffre aléatoire
   # Pour le choix de la ligne et de la colonne
    l = random.randint(0, 3)
    c = random.randint(0, 3)
 
  # On créer une boucle qui s'arrete lorsque la cellule aléatoire choisie est vide
  # Ou contient zero
    while(mat[l] != 0):
        l= random.randint(0, 3)
        c = random.randint(0, 3)
    
    # on ajoute un 2 à cette case vide
    mat[l] = 2
 
# On créer une fonction pour savoir si on a gagné
def état_de_la_partie(mat):
 
    # Si une case contient 2048, on a gagné
    for i in range(4):
        for j in range(4):
            if(mat[i][j]== 2048):
                return 'Tu as gagné !'
 
    # s'il reste au moins une case vide
    # le jeu n'est pas encore terminé
    for i in range(4):
        for j in range(4):
            if(mat[i][j]== 0):
                return 'Ce n est pas fini !'
 
    # si aucune case n'est vide 
    # mais qu'après un déplacement à gauche, à droite, vers le haut ou vers le bas, si deux cases
    # fusionnent et créent une case vide alors le jeu n'est pas encore terminé
    for i in range(3):
        for j in range(3):
            if(mat[i][j]== mat[i + 1][j] or mat[i][j]== mat[i][j + 1]):
                return 'Ce n est pas fini !'
 
    for j in range(3):
        if(mat[3][j]== mat[3][j + 1]):
            return 'Ce n est pas fini !'
 
    for i in range(3):
        if(mat[i][3]== mat[i + 1][3]):
            return 'Ce n est pas fini !'
 
    # Sinon si toute aucunes cases n'est vide et qu'aucun déplacement n'est possible alors
    return 'Tu as perdu !'

 
# fonction de compression de la grille après chaque étapes avant et après la fusion des cellules.
# (on utilisera le mot"cellule" je trouve que c'est plus approprié)
def compress(mat):
 
    # variable bool pour déterminer si un changement s'est produit ou non
    change = False
 
    # grille vide avec toute les cellules vides
    nouvelle_mat =[[0]*4 for i in range(4)]
    #for i in range(4):
    #    nouvelle_mat.append([0] * 4)
         
    # avec toutes les cellules vides ici nous allons décaler les entrées
    # de chaque cellule vers son extrémité gauche, rangée par rangée
    
    # Boucle pour parcourir les lignes
    for i in range(4):
        position = 0
 
        # boucle pour parcourir chaque colonne dans la ligne correspondante
        for j in range(4):
            if(mat[i][j] != 0):
                 
                # si la cellule n'est pas vide alors nous déplaçons son numéro vers
                # la cellule vide précédente de cette ligne marqué par la variable position
                nouvelle_mat[i][position] = mat[i][j]
                 
                if(j != position):
                    change = True
                position += 1
 
    # retour de la nouvelle matrice compressée et la variable de changement.
    return nouvelle_mat, change
#fonction pour fusionner les cellules dans la matrice après compression
def fusion(mat):
     
    change = False
     
    for i in range(4):
        for j in range(3):
 
            # si la cellule actuelle a la même valeur que la cellule suivante de la ligne et qu'elles
            # ne sont pas vides, alors
            if(mat[i][j] == mat[i][j + 1] and mat[i][j] != 0):
 
                # double la valeur de la cellule actuelle et vide la cellule suivante
                mat[i][j] = mat[i][j] * 2
                mat[i][j + 1] = 0
 
                # Mettre true à la variable booléenne indiquant que la nouvelle grille après la fusion est
                # différente.
                change = True
 
    return mat, change


# fonction permettant d'inverser la matrice signifie inverser le contenu de
# chaque ligne 
def reverse(mat):
    nouvelle_mat =[]
    for i in range(4):
        nouvelle_mat.append([])
        for j in range(4):
            nouvelle_mat[i].append(mat[i][3 - j])
    return nouvelle_mat
 
#fonction pour obtenir la transpositiondela matrice signifie qu'il faut interchanger
# lignes et colonnes
def transposition(mat):
    nouv_mat = []
    for i in range(4):
        nouv_mat.append([])
        for j in range(4):
            nouv_mat[i].append(mat[j][i])
    return nouv_mat

#Il reste à faire les foncions de mise à jour de la matrice lorsque l'on bouge haut/bas/gauche/droite

#def move_up
#def move_down
#def move_left
#def move_right

#def score
#def savegame
#ef exit
#def nouv_partie

#Il restera à relier les fonctions entre elles et à faire la partie visuelle/tkinter
#
 