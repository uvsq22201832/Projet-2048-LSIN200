from possible import *

#Le programme suivant va déterminer si le jeu est gagné, perdu, ou en cours.
#Dans le ca d'une victoire, j'sais pas encore quoi faire
#Si c'est en cours, rien ne se passe
#Si c'est perdu, le jeu freeze et les scores doivent apparaître

def winlose(table):
    """
    print("")
    print(table[0])
    print(table[1])
    print(table[2])
    print(table[3])
    print("")"""
    for i in range(len(table)):
        if 2048 in table[i]:
            win = True
            print("Victoire !")
            break
            #Programme de gêle du jeu + écran de victoire
    a = possibility(table)  #On utilise sa pour verifier que y'ai pas de bug
    if len(a) == 5:         #Mais on pourrait l'utiliser pour vérifier si y a une defaite dans le cas où
        print("lose")       #la liste est vide 
        quit()
        #Programme de gêle du jeu + écran de défaite
    else:
        print("continue")
        #Continue le jeu
"""
tabl = [[2, 4, 8, 16]
    ,[32, 4, 2, 4]
    ,[64, 2, 8, 4]
    ,[8, 8, 32, 4]]
winlose(tabl)
"""
