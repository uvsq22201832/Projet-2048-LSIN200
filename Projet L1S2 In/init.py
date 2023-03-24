# Créé par ys000, le 20/02/2023 en Python 3.7
from casesup import *

#On initialise le tableau de base, composé de 0 puis de 2 cases au hasard.

def ini():
    table = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    table = casebonus(table)
    table = casebonus(table)
    return table

