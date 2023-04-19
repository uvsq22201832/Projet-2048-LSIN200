#from condition import *

def somme_valeurs_grille(table):
    s=0
    for i in range(len(table)):
        for j in range(len(table)):
            s=s+table[i,j]
    return s



def sauvegarder():
    table = [[0]*4 for i in range(4)]
    t = [table]*4
    
    f =open('fichier_save.txt', 'wb') 
    pickle.dump(t, f)

def charger():
    t1=[]
    t2=[]
    t3=[]
    t4=[]
    table=[t1,t2,t3,t4]
    f=open('fichier_save.txt', 'rb')
    charge = pickle.load(f)
    
    for i in range(len(charge)):
        for row in charge[i]:
            table[i].append(row)
    return table
