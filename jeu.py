import random,sys

d1 = random.randint(1,6)
d2 = random.randint(1,6)
m = ""
y = "-"
x =""
af = print("bienvenu au jeux de dés!!")
while True:
    m = input("indiquer votre montant avant de commencer la partir : ")
    if not m.isdigit():
        print(f"{'veullez entrez un montant valable ':{y}^50}")
        print(f"{'K-C-B-T':{y}^50s}")
        continue
    m = int(m)
    if 1 >= m:
        print(f"{'veuillez entrez un montant supérieur ou egal à 2 ':{y}^50}")
        print(f"{'K-C-B-T':{y}^50s}")
        continue
    else :
        print(f"{'montan valable!':{y}^50s}")
        print(f"{'K-C-B-T':{y}^50s}")
    while m >= 2:
        x = input("entrez votre mise en euro : ")
        if not x.isdigit():
            print(f"{'veuillez entrez une mise valable':{y}^50}")
            print(f"{'K-C-B-T':{y}^50s}")
            continue
        x = int(x)
        if x > m :
            print(f"{'votre montant est inferieur a votre mise':{y}^50}")
            print(f"{'K-C-B-T':{y}^50s}")
            continue
        if not x >= 2  :
            print(f"{'montant inférieur':{y}^50}")
            print(f"{'K-C-B-T':{y}^50s}")
            continue
        elif d1 == d2 :
            mo = d1 + d2 + x
            m = m + mo
            print(f"vous avez gagner avec un score de {d1} et {d2} \nvotre mise vous a faire gagner {mo} votre mise montant actuel est de {m} ")
            print(f"{'K-C-B-T':{y}^50s}")
        else :
            m = m - x
            print(f"vous avez perdu avec un score de {d1} et {d2} \n montant actuel est {m}")
            print(f"{'K-C-B-T':{y}^50s}")
        c = input("voulez vous continuez o/n : ")
        if c == "o" or c == "O" or c == "OUI" or c == "oui" or len(c) ==0:
            m = m
            if m < 2 :
                print(f"{'votre montant est inférieur à 2':{y}^50}")
                print(f"{'fin de la partit!':{y}^50}")
                print(f"{'K-C-B-T':{y}^50s}")
                break
            elif m >= 2 :
                print(f"{'bonne chance pour la prochaine partir!':{y}^50}")
                print(f"{'K-C-B-T':{y}^50s}")
                d1 = random.randint(1,6)
                d2 = random.randint(1,6)
                continue
        break    
    break