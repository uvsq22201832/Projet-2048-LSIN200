
# Créé par ys000, le 19/02/2023 en Python 3.7

#Ce programme fait déplacer les cases selon un mouvement indiqué sans les fusionner.

def mouvm(tabl, move):

    if move == 'R':
        for i in range(len(tabl)):                      #Axe Y
                for j in range(len(tabl[0])-1,-1,-1):   #Axe X
                    if tabl[i][j] != 0:                 #Quasiment la même chose que Fuz
                        k = 1                           #Si la case est 0, on déplace la case avant jusqu'à ce que se soit pas 0
                        while j+k < len(tabl) and tabl[i][j+k]== 0:
                            x = 0
                            y = tabl[i][j+k-1]          #Tout ça c'est la base du déplacement dans une Matrice donc j'explique pas trop
                            tabl[i][j+k] = y
                            tabl[i][j+k-1] = x
                            k += 1


    elif move == 'L':
        for i in range(len(tabl)):
                for j in range(1,len(tabl[0])):
                    if tabl[i][j] != 0:
                        k = 1

                        while j-k > -1 and tabl[i][j-k]== 0:

                            x = 0
                            y = tabl[i][j-k+1]
                            tabl[i][j-k] = y
                            tabl[i][j-k+1] = x
                            k += 1

    elif move == 'D':
        for j in range(len(tabl[0])):
                for i in range(len(tabl)-2,-1,-1):
                    if tabl[i][j] != 0:
                        k = 1
                        while i+k < len(tabl) and tabl[i+k][j]== 0:
                            x = 0
                            y = tabl[i+k-1][j]
                            tabl[i+k][j] = y
                            tabl[i+k-1][j] = x
                            k += 1

    elif move == 'U':
        for j in range(len(tabl[0])):
                for i in range(1,len(tabl[0])):
                    if tabl[i][j] != 0:
                        k = 1
                        while i-k > -1 and tabl[i-k][j]== 0:
                            x = 0
                            y = tabl[i-k+1][j]
                            tabl[i-k][j] = y
                            tabl[i-k+1][j] = x
                            k += 1


    """
    print(tabl[0])
    print(tabl[1])
    print(tabl[2])
    print(tabl[3])"""
    return tabl





"""
                                #Les test
#tabltest = [[4,2,2,0],[0,2,2,4],[2,0,0,4],[0,0,0,8]]
tabltest = [[0,0,0,2],[0,0,0,2],[0,0,0,2],[0,0,0,2]]
move = 'L'

print(tabltest[0])
print(tabltest[1])
print(tabltest[2])
print(tabltest[3])
print("")

print(mouvm(tabltest,move)) #Prend le tableau + le mouvement fait entre U, D, L, R"""