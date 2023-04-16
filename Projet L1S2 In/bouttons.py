from condition import *

def nouvelle_partie():
    start()

def somme_valeurs_grille(table):
    s=0
    for i in range(len(table)):
        for j in range(len(table)):
            s=s+table[i,j]
    return s

def sauvegarder():
    f_input=(open('fichier_save'),"w")  #avec le fichier qui s'apelle 'fichier save'
    for e in table:
        f_input.readline()
    f_input.close()

def parse_line( ligne , sep, num_colonne, ty) :
        li = ligne.split(sep)
        if ty == "int" :
            return(int(li[num_colonne]))

def charger():
    f_input=open('fichier_save','r')
    for i in range(len(table)):
        for j in range(len(table)):
            table[i].append(parse_line(a,',',j,'int'))
        a=f_input.readline
    f_input.close()

