
#Le programme suivant détérmine toute les possibilités envisageable et renvoie une liste de toute les possibilités


def possibility(table):

    poss = []
    for i in range(len(table)):
        for j in range(len(table[0])):
            #print(i,j,table[i][j])
            if table[i][j] != 0:
                if j == 0:
                    if table[i][j+1] == 0 or table[i][j+1] == table[i][j]:  #Pour chaque mouvement possible, ça va vérifier si la case à coté
                        if 'R' not in poss:                                 #est soi vide, soi identique
                            poss.append('R')                                #Ensuite sa vérifie si le mouvement n'est pas déjà présent dans la liste
                elif j == len(table)-1:                                     #Sinon ça rajoute le mouvement
                    if table[i][j-1] == 0 or table[i][j-1] == table[i][j]:  #Note: Y a 3 if a chaque fois au cas où l'un des voisins est hors-tableau
                        if 'L' not in poss:
                            poss.append('L')
                else:
                    if table[i][j+1] == table[i][j] or table[i][j+1] == 0:
                        if 'R' not in poss:
                            poss.append('R')
                    if table[i][j-1] == 0 or table[i][j-1] == table[i][j]:
                        if 'L' not in poss:
                            poss.append('L')
                if i == 0:
                    if table[i+1][j] == 0 or table[i+1][j] == table[i][j]:
                        if 'D' not in poss:
                            poss.append('D')
                elif i == len(table)-1:
                    if table[i-1][j] == 0 or table[i-1][j] == table[i][j]:
                        if 'U' not in poss:
                            poss.append('U')
                else:
                    if table[i-1][j] == 0 or table[i-1][j] == table[i][j]:
                        if 'U' not in poss:
                            poss.append('U')
                    if table[i+1][j] == table[i][j] or table[i+1][j]==0:
                        if 'D' not in poss:
                            poss.append('D')
    if len(poss) == 0:  #Si y a aucune possibilité, ça renvoie Echec
        return 'echec'
    else:
        print(poss)     #Sinon il montre les possibilités dans le terminal pour l'instant
        return poss     #Je sais pas si on continue de l'afficher ou si on en fait un debug mode

"""
#Les test
tabltest = [[0, 0, 0, 0]
,[0, 0, 0, 0]
,[0, 2, 8, 4]
,[8, 8, 32, 4]]
#tabltest = [[4,0,0,0],[5,0,0,0],[3,0,0,0],[4,0,0,0]]


print(tabltest[0])
print(tabltest[1])
print(tabltest[2])
print(tabltest[3])
print("")

print(possibility(tabltest))
"""