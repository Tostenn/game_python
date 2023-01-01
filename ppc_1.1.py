from time import sleep
from os import system
from random import randint
def cls(): system('cls')
def t(x) : sleep(x)
nom = input("entrer votre nom : ")
if len(nom) == 0:
    nom = 'joueur'
t(0.2)
print('preparation du jeux')
# t(0.2)
for i in range(10):
    x= randint(1,3)
    print('veullez patienter'+'.'*x)
    t(0.2)
    cls()
verrify = True
option = '''liste des options
1-parti à 10 points gagnant
2-partir libre
3-infomationrmation sur les différents parties
4-Quitter
-> '''
infomation = '''bienvenu dans la section infomation
    - L'option 1 consiste à jouer des partir de 10 contre notre IA
    - L'option 2 comme sont nom l'indique est une parti libre
        cette partir a etait créer dans le but de vous entrainez a affronter 
        notre IA
    - Vous pouvez jouer avec les chiffre 1, 2 et 3 qui corresponde aux (pierre, papier et ciseau)
        ou simplement ecrire les mots mots clés 
'''
choix_op = ''
ppc = ['pierre','papier','ciseaeu']
ppc_n = ['1','2','3']
root = ppc[randint(0,2)]
def socre():
    cls()
    print(f'''==============================
==   socre : {sj} - {sr}         ==
==============================''')

def aff_g():
    cls()
    print(f'''==============================
==   socre : {sj} - {sr}          ==
==============================
vous avez gagnez
    {nom} : {choix_ppc}
    root : {root}
    ''')
def aff_p():
    cls()
    print(f'''==============================
==   socre : {sj} - {sr}          ==
==============================
vous avez perdu
    {nom} : {choix_ppc}
    root : {root}
    ''')

while verrify:
    ppc_n.append('4')
    while True:
        choix_op = input(option)
        choix_op = str(choix_op)
        if choix_op.isdigit() and choix_op in ppc_n:
            choix_op = int(choix_op)
            break
        else:
            print('value Error!')
            continue
    ppc_n.pop()
    cls()
    if choix_op == 1:
        print('parti a 10 point')
        choix_ppc = ''
        sj = 0; sr = 0
        verrify1 = True
        while verrify1:
            while True:
                choix_ppc = input('entrer votre choix : ')
                if choix_ppc.isalpha() and choix_ppc in ppc:
                    break
                elif choix_ppc.isdigit() and choix_ppc in ppc_n:
                    choix_ppc = ppc[int(choix_ppc)-1]
                    break
                else :
                    print('value Error!')
                    continue
            root = ppc[randint(0,2)]
            if choix_ppc == root:
                print('----------egalite')
            elif choix_ppc == ppc[0] and root == ppc[2]:
                sj +=1
                aff_g()
            elif choix_ppc == ppc[1] and root == ppc[0]:
                sj +=1
                aff_g()
            elif choix_ppc == ppc[2] and root == ppc[1]:
                sj +=1
                aff_g()
            elif root == ppc[2] and choix_ppc == ppc[1]:
                sr +=1
                aff_p()
            elif root == ppc[1] and choix_ppc == ppc[0]:
                sr +=1
                aff_p()
            elif root == ppc[0] and choix_ppc == ppc[2]:
                sr +=1
                aff_p()
            if (sj == 10 or sr == 10):
                verrify1 = False
                cls()
        if sj > sr:
            socre()
            input(f'{"victoire":-^31}')
        if sj < sr:
            socre()
            input(f'{"defaite":-^31}')
        cls()
    elif choix_op == 2:
        print('parti libre ')
        choix_ppc = ''
        sj = 7; sr = 8
        verrify1 = True
        while verrify1:
            while True:
                choix_ppc = input('entrer votre choix : ')
                if choix_ppc.isalpha() and choix_ppc in ppc:
                    break
                elif choix_ppc.isdigit() and choix_ppc in ppc_n:
                    choix_ppc = ppc[int(choix_ppc)-1]
                    break
                else :
                    print('value Error!')
                    continue

            root = ppc[randint(0,2)]
            if choix_ppc == root:
                print('----------egalite')
            elif choix_ppc == ppc[0] and root == ppc[2]:
                sj +=1
                aff_g()
            elif choix_ppc == ppc[1] and root == ppc[0]:
                sj +=1
                aff_g()
            elif choix_ppc == ppc[2] and root == ppc[1]:
                sj +=1
                aff_g()
            elif root == ppc[2] and choix_ppc == ppc[1]:
                sr +=1
                aff_p()
            elif root == ppc[1] and choix_ppc == ppc[0]:
                sr +=1
                aff_p()
            elif root == ppc[0] and choix_ppc == ppc[2]:
                sr +=1
                aff_p()
            if (sj % 10 == 0):
                c = input("voulais contunuer o/n : ")
                if c == 'o':
                    pass
                else :
                    verrify1 = False
        if sj > sr:
            socre()
            input(f'{"victoire":-^31}')
        if sj < sr:
            socre()
            input(f'{"defaite":-^31}')
        cls()
    elif choix_op == 3:
        input(infomation)
        cls()
    elif choix_op == 4:
        print('fin')
        verrify = False
