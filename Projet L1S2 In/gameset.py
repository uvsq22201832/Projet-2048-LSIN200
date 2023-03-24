# Créé par ys000, le 20/02/2023 en Python 3.7
from casesup import *
from Fuz import *
from Mouvement import *

#On gère ici le mouvement du tableau.
#Le principe c'est que tout bouge, puis on fusionne, puis on rebouge pour tout mettre en ordre.

def game(table, move):
    table = mouvm(table,move)
    table = fusion(table,move)
    table = mouvm(table,move)
    return table

#print(game([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],'L'))