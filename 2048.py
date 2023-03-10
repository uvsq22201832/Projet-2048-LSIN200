# Créé par ys000, le 19/02/2023 en Python 3.7

#Projet 2048

#Interface graphique

#Calcul du tableau

def calcul(tabl, move):

    if move == 'R':
        for i in range(len(tabl)):
                for j in range(len(tabl[0])-1,-1,-1):
                    if tabl[i][j] != 0:
                        k = 1
                        while j+k < len(tabl) and tabl[i][j+k]== 0:
                            x = 0
                            y = tabl[i][j+k-1]
                            tabl[i][j+k] = y
                            tabl[i][j+k-1] = x
                            k += 1


    elif move == 'L':
        for i in range(len(tabl)):
                for j in range(1,len(tabl[0])):
                    if tabl[i][j] != 0:
                        k = 1
                        while j-k < len(tabl) and tabl[i][j-k]== 0:
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
                        while i-k < len(tabl) and tabl[i-k][j]== 0:
                            x = 0
                            y = tabl[i-k+1][j]
                            tabl[i-k][j] = y
                            tabl[i-k+1][j] = x
                            k += 1



    print(tabl[0])
    print(tabl[1])
    print(tabl[2])
    print(tabl[3])






tabltest = [[4,2,2,0],[0,2,2,4],[2,0,0,4],[2,0,0,8]]
move = 'U'

print(tabltest[0])
print(tabltest[1])
print(tabltest[2])
print(tabltest[3])
print("")

calcul(tabltest,move)