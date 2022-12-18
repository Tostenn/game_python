
from random import randint
from os import system
# effter()
system('cls')

def verch(choix='',info="",erro = 'valeur innatendu!', deb = 0,fin = 3):
    l= list(range(deb,fin+1))
    veri = True
    while veri:
        choix = input(info)
        if choix.isdigit():
            choix = int(choix)
            if choix in l: veri = False
            else: print(erro)
        else:print(erro)
    return choix
# nombre de joueur
nj = verch(choix='',info='Nombre de participant : ')

# recuperation des noms de joueur
def name(n):
    nom_j = {}
    for i in range(n):
        nm =''
        while 1:    
            nm = input(f'username du participant {i+1} : ')
            if len(nm) == 0:
                nm = f'joueur {i}'
            if nm in nom_j:continue
            else:break
        nom_j[nm] = 0
    return nom_j
nom_j = name(nj)
def de():
    return randint(1,6)

# affichage du score
# def aff():

def aff():
    system('cls')
    print(f'======================il reste {f"{arr} parties" if arr>1 else f"{arr} partie"} =================')
    f = '='
    print(f"{'==':{f}^50}")
    print('==\t',end='')
    for i,j in nom_j.items():
        print(f'{i} : {j} \t',end='')
    print('==')
    print(f"{'==':{f}^50}\n")
    pass

arr = verch(info='entrer le nombre de round : ',fin=15)
while True:
    aff()
    x = 0;nl = ''
    for i,n in nom_j.items():

        input(i+' appuyer la touche zntrer pour valider : ')
        d = de()
        print(i,'votre score est',d)
        if x < d:
            x = d
            nl = i
    nom_j[nl] =nom_j[nl]+1 
    input(f'{nl} gagnant de cette partie avec un scorede {x}')
    arr -=1
    if arr ==0:
        aff()
        exit()

    pass