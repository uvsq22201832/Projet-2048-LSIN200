# Créé par ys000, le 19/02/2023 en Python 3.7

#Ici, les cases fusionnent avec leur voisin selon le mouvement indiqué.
#Attention, le programme ne détecte pas sur quel coté la case fusionné doit se placer, tout est déplacé plus tard.
#C'est pour éviter les bug

def fusion(table,mouv):

    if mouv == 'R':                                 #Déjà y a 1 function pour chaque mouvement
        for i in range(len(table)):                 #Ca c'est la ligne en Y
            for j in range(len(table[0])-1,-1,-1):  #Ca c'est les X, on les parcours à l'envers pour éviter les bug
                if table[i][j] == table[i][j-1]:
                    table[i][j] *= 2                #L'évolution des cases ce fait par addition de 2 cases identiques
                    table[i][j-1] = 0               #Donc c'est une multiplication par 2, pour pas mettre une conditon pour chaque nombre

    elif mouv == 'L':                               #Repeat chaque explication frérot
        for i in range(len(table)):
            for j in range(len(table[0])-1):

                if table[i][j] == table[i][j+1]:
                    table[i][j] *= 2
                    table[i][j+1] = 0

    elif mouv == 'D':
        for i in range(len(table)-1,-1,-1):
            for j in range(len(table[0])):
                if table[i][j] == table[i-1][j]:
                    table[i][j] *= 2
                    table[i-1][j] = 0

    elif mouv == 'U':
        for i in range(len(table)-1):
            for j in range(len(table[0])):
                if table[i][j] == table[i+1][j]:
                    table[i][j] *= 2
                    table[i+1][j] = 0



    """
    print(table[0])
    print(table[1])
    print(table[2])
    print(table[3])
    print("")
    """
    return table









"""
#Les test
tabltest = [[4,2,2,0],[0,2,2,4],[2,0,0,4],[2,0,0,8]]


print(tabltest[0])
print(tabltest[1])
print(tabltest[2])
print(tabltest[3])
print("")

"""
#print(fusion(mouvm(tabltest,"R"), 'R'))


#fusion(mouvm(tabltest,"L"), 'L')


#fusion(mouvm(tabltest,"D"), 'D')


#fusion(mouvm(tabltest,"U"), 'U')