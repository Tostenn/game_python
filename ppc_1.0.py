import os,random,sys,time,json

# import  bot
nom = input("entrer votre nom : ")

if len(nom)== 0 :
	nom = "joueur"

sj = 0;sr=0
if os.path.isfile('data.json'):
	with open('data.json') as file:
		data = json.load(file)
		if f'user-{nom}' in data:
			sv = input(f'\x1b[38;5;{240}mil y a une sauvegarde en votre nom \nvoulais vous contuner avec elle ? o/n : ')
			if sv == "o":
				print('tres bon choix')
				sj = data[f'user-{nom}']['sj']
				sr = data[f'user-{nom}']['root']

os.system("cls")
# bot.couleur_1()
e = f"{'K-C-B-T':-^64}"
ver = "\x1b[37m";bl = "\x1b[37m";j = "\x1b[36m"

info = f"""{bl}{e}\nbienvenue dans le jeu pierre papier ciseaux\n
\t-vous devez choisir entre 
\t	\x1b[33m1- pierre 
\t	2- papier	{bl}score : {nom}{j} {sj}{bl} : {j}{sr} {bl}root
\t	\x1b[33m3- ciseaux
\x1b[31mNB: choisir avec les  chiffres ou les nom\x1b[37m
\t- vous jouez contre le root alors bonne chance
{e}"""
print(info)

l = ["pierre","papier","ciseaux"];n = [ "1","2","3"]

root = random.randint(0,2)


while True :
#	choix = input(bl+"entrer votre choix :")
	while True : 
		choix = input(bl+"entrer votre choix : ")
		if choix.islower() and choix in l:
			choix = l.index(choix)
#			print (choix)
			break 
		elif choix == "tosten":
			break 
		elif choix.islower() and not choix in l and choix != "tosten":
			time.sleep(1.5)
			print(f"\x1b[38;5;{240}m{'vous devez choisir entre pierre, papier,  ciseaux':<64}\n{e}")
			continue 
		elif choix.isdigit() and  not choix in n :
					print(f"\x1b[38;5;{240}m{'vous devez choisir entre 1, 2, 3':^64}\n{e}")
		elif choix.isdigit and choix in n :
			choix = int(choix)
			choix -=1
			break 
	if choix == root :
		time.sleep(1)
		print(f"\x1b[38;5;{240}mbravo vous êtes à égalité")
		sj+=1
		sr+=1
	elif choix == "tosten":
		sj +=5
		print(f"\t\x1b[38;5;{153}m{nom} vous avez gagné 5 ponts de plus avec ce code\n{e}{bl}" )
	elif (choix == 0 or choix == "pierre") and root == 2:
		time.sleep(1)
		print(f"""vous avez gagné
	{j}  	{nom} : {l[choix] }
	{bl}	root : {l[root]} """)
		sj+=1
	elif (choix == 1 or choix == "papier") and root == 0:
		time.sleep(1)
		print(f"""vous avez gagné
{j}  		{nom} : {l[choix] }
{bl}		root : {l[root]} """)
		sj+=1
	elif (choix == 2 or choix == "ciseaux") and root == 1:
		time.sleep(1)
		print(f"""vous avez gagné
{j}	  	{nom} : {l[choix] }
{bl}		root : {l[root]} """)
		sj+=1
	elif root == 0 and (choix == 2 or choix == "ciseaux"):
		time.sleep(1)
		sr+=1
		print(f"""vous avez perdu 
{bl} 	{nom} : {l[choix] }
{j}	root : {l[root]} """)
	elif root == 1 and (choix == 0 or choix == "pierre"):
		time.sleep(1)
		sr+=1
		print(f"""vous avez perdu 
{bl} 	{nom} : {l[choix] }
{j}	root : {l[root]} """)
	elif root == 2 and (choix == 1 or choix == "papier"):
		time.sleep(1)
		sr+=1
		print(f"""vous avez perdu 
{bl} 	{nom} : {l[choix] }
{j}	root : {l[root]} """)
	c = input(bl+"voulez vous continuer o/n : ")
	if c == "o" or len(c) == 0 :
		os.system('cls')
		root = random.randint(0,2)
		print(f"""{bl}{e}\nbienvenue dans le jeu pierre papier ciseaux\n
\t-vous devez choisir entre 
\t	\x1b[33m1- pierre 
\t	2- papier	{bl}score : {nom}{j} {sj}{bl} : {j}{sr} {bl}root
\t	\x1b[33m3- ciseaux
\x1b[31mNB: choisir avec les  chiffres ou les nom\x1b[37m
\t- vous jouez contre le root alors bonne chance
{e}""")
	else :
		saver = input(bl+"voulez vous sauvegarder cette partir o/n : ")
		if saver == 'o':
			compteur = 1
			if os.path.isfile('data.json'):
				data[f'user-{nom}'] = {
						'sj':sj,
						'root':sr
					}
				with open('data.json', 'w') as file:
					json.dump(data,file)
			else:
				data = {f'user-{nom}':{
						'sj':sj,
						'root':sr
					}}
				with open('data.json', 'w') as file:
					json.dump(data,file)

		if sj > sr:
			# bot.couleur()
			os.system('cls')
			print(f"""{bl}{e}\nfin du jeu pierre papier ciseaux \n\n\t{bl}score finale : {j}{nom} {sj}{bl} : {sr} root\n\n\t\t victoire de {j}{nom}{bl}\n{e}""")
		elif sr > sj:
			# bot.couleur_1()
			os.system('cls')
			print(f"""{bl}{e}\nfin du jeu pierre papier ciseaux \n\n\t{bl}score finale : {nom} {sj} : {j}{sr} root{bl}\n\n\t\tvictoire du {j}root {bl}
{e}""")
		elif sr == sj:
			# bot.couleur_1()
			os.system('cls')
			print(f"""{bl}{e}\nfin du jeu pierre papier ciseaux \n\n\t{bl}score finale : {nom} {sj} : {sr} root{bl}\n\n\t\t\t \x1b[38;5;{184}mégalite {bl}
{e}""")
		print(f"\x1b[38;5;{240}m{nom} à bientôt")
		sys.exit()
