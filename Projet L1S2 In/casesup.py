# Créé par ys000, le 19/02/2023 en Python 3.7
from random import *

#Là, ça va vérifier s'il y a des cases vides
#Puis si c'est le cas, tiré un chiffre au hasard pour déterminer si c'est 4 ou 2
#Puis le placé dans une case au pif

def casebonus(table):
    vide = []
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] == 0:
                vide.append([i,j])

    if vide:                                    #Si la liste renvoie True, c'est que la liste n'est pas vide, donc au moins 1 case est vide
        a = randint(0,len(vide)-1)              #Sinon on touche a rien
        b = randint(1,10)                       #Le b c'est pour gerer la chance d'obtenir 2 ou 4
        if b <= 9:
            table[vide[a][0]][vide[a][1]] = 2
        else:
            table[vide[a][0]][vide[a][1]] = 4

    return table


"""
#Les test
tabltest = [[4,2,2,0],[0,2,2,4],[2,0,0,4],[2,0,0,8]]


print(tabltest[0])
print(tabltest[1])
print(tabltest[2])
print(tabltest[3])
print("")

print(casebonus(tabltest))"""