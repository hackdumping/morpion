import os

def affiche(p):
	os.system('printf "\033[00;01m"')
	print ("\n\t\t",p[0]," | ",p[1]," | ",p[2])
	print ("\t\t----+-----+----")
	print ("\t\t",p[3]," | ",p[4]," | ",p[5])
	print ("\t\t----+-----+----")
	print ("\t\t",p[6]," | ",p[7]," | ",p[8])
	os.system('printf "\033[00;33m"')
def decision(p,cpt):
	if ((p[0]==p[1]==p[2]=='X') or (p[0]==p[3]==p[6]=='X') or (p[6]==p[7]==p[8]=='X') or (p[8]==p[5]==p[2]=='X') or (p[0]==p[4]==p[8]=='X') or (p[2]==p[4]==p[6]=='X') or (p[2]==p[5]==p[8]=='X') or (p[1]==p[4]==p[7]=='X') or (p[3]==p[4]==p[5]=='O')) :
		cpt=1
	else :
		if ((p[0]==p[1]==p[2]=='O') or (p[0]==p[3]==p[6]=='O') or (p[6]==p[7]==p[8]=='O') or (p[8]==p[5]==p[2]=='O') or (p[0]==p[4]==p[8]=='O') or (p[2]==p[4]==p[6]=='O') or (p[2]==p[5]==p[8]=='O') or (p[2]==p[5]==p[8]=='O') or (p[1]==p[4]==p[7]=='O') or (p[3]==p[4]==p[5]=='O')) :
			cpt=2
	return cpt

def position(i,f):
	v=False
	if (i==1 and (f==2 or f==5 or f==4)) or (i==2 and (f==1 or f==3 or f==5)) or (i==3 and (f==2 or f==5 or f==6)) or (i==4 and (f==1 or f==5 or f==7)) or (i==5 and (f==1 or f==2 or f==3 or f==4 or f==6 or f==7 or f==8 or f==9)) or (i==6 and (f==3 or f==5 or f==9)) or (i==7 and (f==4 or f==5 or f==8)) or (i==8 and (f==5 or f==7 or f==9)) or (i==9 and (f==8 or f==6 or f==5)) :
		v= True
	return v

os.system('clear')
os.system('toilet -t --metal "    MORPION"')
print ("\n\n\n\n")
#print ("\n\n\t\t\t~~~~~~~~~~~~~~~~~~~« JEU DU MORPION »~~~~~~~~~~~~~~~~~~~\n\n\n\n")
os.system('printf "\033[00;32m"')
print ("\tPRINCIPE : Le jeu consiste à aligner 03 'X' ou 03 'O' horizontalement, verticalement ou en diagonale pour gagner...")
print ("\t\tChaque chiffre (de 1 à 9) entrer représentera la position de la case")
print ("\t\tVous disposer de 03 pions au départ ..Puis vous allez tentrer d'aligner ces pions pour gagner..(*-*)")
print ("\t\t--> «Initial» representera la position initial du pion à déplacer ..")
print ("\t\t--> «Final» representera la position final  du pion..\n\n")
os.system('printf "\033[00;33m"')

nom1= input("\tNom du joueur 1 : ")
nom1= nom1.upper()
nom2= input("\tNom du jour 2 : ")
nom2=nom2.upper()
print ("\n\t{} sera 'X' et {} sera 'O'.\n\n".format(nom1,nom2))

tour = True
while tour :
	os.system('clear')
	p=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
	os.system('printf "\033[00;01m"')
	os.system('figlet -t -c "le  jeu  peux  commencer.."')
	os.system('printf "\033[00;33m"')
	print ("\n\n")
	cpt=0

	print ("\n\n\t\tPlacer vos 03 pions..\n\n")
	for i in range (3):
		while True :
			n1= int(input ("\t{} >>>  Entrer un chiffre de 1 à 9 : ".format(nom1))) 
			while n1<=0 or n1>9 :
				print("\t\tValeur hors plage,,")
				n1= int(input ("\t{} >>>  Entrer un chiffre de 1 à 9 : ".format(nom1)))
			if (p[n1-1]!= ' ') :
				print ("\t\tLa case {} est déjà occupée ..".format(n1))
			else :
				break
		p[n1-1]= 'X'
		affiche(p)
		print ("")
		if decision(p,cpt)==1 :
			print ("\n\n\t*****************Bravo {} vous avez gagner !*****************\n\n\t\t\t\t(^-^)\n\n\n".format(nom1))
			break
		else :
			if decision(p,cpt)==2 :
				print ("\n\n\t****************Bravo {} vous avez gagner !****************\n\n\t\t\t\t(^-^)\n\n\n".format(nom2))
				break
		print ("")

		while True :
			n2= int(input ("\t{} >>>  Entrer un chiffre de 1 à 9 : ".format(nom2)))
			while n2<=0 or n2>9 :
				print("\t\tValeur hors plage,,")
				n2= int(input ("\t{} >>>  Entrer un chiffre de 1 à 9 : ".format(nom2)))
			if (p[n2-1]!= ' ' ):
				print ("\t\tLa case {} est dàja occupée ..".format(n2))
			else :
				break
		p[n2-1]= 'O'
		affiche(p)
		print ("")
		if decision(p,cpt)==1 :
			print ("\n\n\t*****************Bravo {} vous avez gagner !*****************\n\n\t\t\t\t(^-^)\n\n\n".format(nom1))
			continue
		else :
			if decision(p,cpt)==2 :
				print ("\n\n\t****************Bravo {} vous avez gagner !****************\n\n\t\t\t\t(^-^)\n\n\n".format(nom2))
				break

		if(i==2):
			print ("\n\n\t\tVous pouvez commencer à déplacer vos pions\n\n\n")
		print ("")
	if (decision(p,cpt)==1 or decision(p,cpt)==2):
		print ("\n\tVoulez vous continuez ? \n\t\t1-OUI\n\t\t2-NON")
		dec=int(input("\n\t~> "))
		while dec<=0 or dec>2 :
			print ("\n\tValeur hors plage..")
			dec=int(input("\n\t~> "))
		if dec==1 :
			print ("\n\n\tSuper! allons-y\n\n\n\n")
			tour = True
			continue
		else :
			print ("\n\n\n\tMerci . À bientôt !\n\n\n\n\n\n\n\n\n\n\n\t« By Dumping »\n\n\n\n\n")
			tour = False
			continue

	while True :

		#joueur 1

		print ("\n\t{} >>\n".format(nom1))
		init= int(input ("\t\tInitial : "))
		while init<=0 or init>9 :
			print("\t\t\tValeur hors plage,,")
			init= int(input ("\t\tInitial : "))

		fin= int(input ("\t\tFinal : "))
		while fin<=0 or fin>9 :
			print("\t\t\tValeur hors plage,,")
			fin= int(input ("\t\tFinal : "))

		while True :
			if (position(init,fin)==False) :
				print ("\n\t\tDéplacement Inconu..\n")
				print ("\n\t{} >>\n".format(nom1))
				init= int(input ("\t\tInitial : "))
				while init<=0 or init>9 :
					print("\t\t\tValeur hors plage,,")
					init= int(input ("\t\tInitial : "))
				while True:
					if (p[init-1]!= 'X' ):
						print ("\t\t\tPions 'X' non détecté à la case {} ..".format(init))
						init= int(input ("\t\tInitial : "))
						while init<=0 or init>9 :
							print("\t\t\tValeur hors plage,,")
							init= int(input ("\t\tInitial : "))
					else :
						break

				fin= int(input ("\t\tFinal : "))
				while fin<=0 or fin>9 :
					print("\t\t\tValeur hors plage,,")
					fin= int(input ("\t\tFinal : "))
				while True :
					if (p[fin-1]!= ' ' ):
						print ("\t\t\tEspace vide non détecté à la case {} ..".format(fin))
						fin= int(input ("\t\tFinal : "))
						while fin<=0 or fin>9 :
							print("\t\t\tValeur hors plage,,")
							fin= int(input ("\t\tFinal : "))
					else :
						break

			elif (position(init,fin)==True and p[fin-1]!= ' '):
				print ("\n\t\tErreur lors du déplacement..\n")
				print ("\n\t{} >>\n".format(nom1))
				init= int(input ("\t\tInitial : "))
				while init<=0 or init>9 :
					print("\t\t\tValeur hors plage,,")
					init= int(input ("\t\tInitial : "))
				while True:
					if (p[init-1]!= 'X' ):
						print ("\t\t\tPions 'X' non détecté à la case {} ..".format(init))
						init= int(input ("\t\tInitial : "))
						while init<=0 or init>9 :
							print("\t\t\tValeur hors plage,,")
							init= int(input ("\t\tInitial : "))
					else :
						break

				fin= int(input ("\t\tFinal : "))
				while fin<=0 or fin>9 :
					print("\t\t\tValeur hors plage,,")
					fin= int(input ("\t\tFinal : "))
				while True :
					if (p[fin-1]!= ' ' ):
						print ("\t\t\tEspace vide non détecté à la case {} ..".format(fin))
						fin= int(input ("\t\tFinal : "))
						while fin<=0 or fin>9 :
							print("\t\t\tValeur hors plage,,")
							fin= int(input ("\t\tFinal : "))
					else :
						break

			elif (position(init,fin)==True and p[init-1]== ' '):
				print ("\n\t\tDépart vide..\n")
				print ("\n\t{} >>\n".format(nom1))
				init= int(input ("\t\tInitial : "))
				while init<=0 or init>9 :
					print("\t\t\tValeur hors plage,,")
					init= int(input ("\t\tInitial : "))
				while True:
					if (p[init-1]!= 'X' ):
						print ("\t\t\tPions 'X' non détecté à la case {} ..".format(init))
						init= int(input ("\t\tInitial : "))
						while init<=0 or init>9 :
							print("\t\t\tValeur hors plage,,")
							init= int(input ("\t\tInitial : "))
					else :
						break

				fin= int(input ("\t\tFinal : "))
				while fin<=0 or fin>9 :
					print("\t\t\tValeur hors plage,,")
					fin= int(input ("\t\tFinal : "))
				while True :
					if (p[fin-1]!= ' ' ):
						print ("\t\t\tEspace vide non détecté à la case {} ..".format(fin))
						fin= int(input ("\t\tFinal : "))
						while fin<=0 or fin>9 :
							print("\t\t\tValeur hors plage,,")
							fin= int(input ("\t\tFinal : "))
					else :
						break

			else :
				while True:
					if (p[init-1]!= 'X' ):
						print ("\t\t\tPions 'X' non détecté à la case {} ..".format(init))
						init= int(input ("\t\tInitial : "))
						while init<=0 or init>9 :
							print("\t\t\tValeur hors plage,,")
							init= int(input ("\t\tInitial : "))
					else :
						break

				while True :
					if (p[fin-1]!= ' ' ):
						print ("\t\t\tEspace vide non détecté à la case {} ..".format(fin))
						fin= int(input ("\t\tFinal : "))
						while fin<=0 or fin>9 :
							print("\t\t\tValeur hors plage,,")
							fin= int(input ("\t\tFinal : "))
					else :
						break

				break

		tmp=p[fin-1]
		p[fin-1]=p[init-1]
		p[init-1]=tmp
		cpt=0
		print ("")
		affiche(p)
		print ("")
		if decision(p,cpt)==1 :
			print ("\n\n\t*****************Bravo {} vous avez gagner !*****************\n\n\t\t\t\t(^-^)\n\n\n".format(nom1))
			break
		else :
			if decision(p,cpt)==2 :
				print ("\n\n\t****************Bravo {} vous avez gagner !****************\n\n\t\t\t\t(^-^)\n\n\n".format(nom2))
				break

		print ("")

		#joueur 2

		print ("\n\t{} >>\n".format(nom2))
		init2= int(input ("\t\tInitial : "))
		while init2<=0 or init2>9 :
			print("\t\t\tValeur hors plage,,")
			init2= int(input ("\t\tInitial : "))

		fin2= int(input ("\t\tFinal : "))
		while fin2<=0 or fin2>9 :
			print("\t\t\tValeur hors plage,,")
			fin2= int(input ("\t\tFinal : "))


		while True :
			if position(init2,fin2)==False :
				print ("\n\t\tDéplacement Inconu..\n")
				print ("\n\t{} >>\n".format(nom2))
				init2= int(input ("\t\tInitial : "))
				while init2<=0 or init2>9 :
					print("\t\t\tValeur hors plage,,")
					init2= int(input ("\t\tInitial : "))
				while True :
					if (p[init2-1]!= 'O' ):
						print ("\t\t\tPions 'O' non détecté à la case {} ..".format(init2))
						init2= int(input ("\t\tInitial : "))
						while init2<=0 or init2>9 :
							print("\t\t\tValeur hors plage,,")
							init2= int(input ("\t\tInitial : "))
					else :
						break

				fin2= int(input ("\t\tFinal : "))
				while fin2<=0 or fin2>9 :
					print("\t\t\tValeur hors plage,,")
					fin2= int(input ("\t\tFinal : "))
				while True :
					if (p[fin2-1]!= ' ' ):
						print ("\t\t\tEspace vide non détecté à la case {} ..".format(fin2))
						fin2= int(input ("\t\tFinal : "))
						while fin2<=0 or fin2>9 :
							print("\t\t\tValeur hors plage,,")
							fin2= int(input ("\t\tFinal : "))
					else :
						break


			elif (position(init2,fin2)==True and p[fin2-1]!= ' '):
				print ("\n\t\tErreur lors du déplacement..\n")
				print ("\n\t{} >>".format(nom2))
				init2= int(input ("\t\tInitial : "))
				while init2<=0 or init2>9 :
					print("\t\t\tValeur hors plage,,")
					init2= int(input ("\t\tInitial : "))
				while True :
					if (p[init2-1]!= 'O' ):
						print ("\t\t\tPions 'O' non détecté à la case {} ..".format(init2))
						init2= int(input ("\t\tInitial : "))
						while init2<=0 or init2>9 :
							print("\t\t\tValeur hors plage,,")
							init2= int(input ("\t\tInitial : "))
					else :
						break

				fin2= int(input ("\t\tFinal : "))
				while fin2<=0 or fin2>9 :
					print("\t\t\tValeur hors plage,,")
					fin2= int(input ("\t\tFinal : "))
				while True :
					if (p[fin2-1]!= ' ' ):
						print ("\t\t\tEspace vide non détecté à la case {} ..".format(fin2))
						fin2= int(input ("\t\tFinal : "))
						while fin2<=0 or fin2>9 :
							print("\t\t\tValeur hors plage,,")
							fin2= int(input ("\t\tFinal : "))
					else :
						break

			elif (position(init2,fin2)==True and p[init2-1]== ' ') :
				print ("\n\t\tDépart vide..\n")
				print ("\n\t{} >>".format(nom2))
				init2= int(input ("\t\tInitial : "))
				while init2<=0 or init2>9 :
					print("\t\t\tValeur hors plage,,")
					init2= int(input ("\t\tInitial : "))
				while True :
					if (p[init2-1]!= 'O' ):
						print ("\t\t\tPions 'O' non détecté à la case {} ..".format(init2))
						init2= int(input ("\t\tInitial : "))
						while init2<=0 or init2>9 :
							print("\t\t\tValeur hors plage,,")
							init2= int(input ("\t\tInitial : "))
					else :
						break

				fin2= int(input ("\t\tFinal : "))
				while fin2<=0 or fin2>9 :
					print("\t\t\tValeur hors plage,,")
					fin2= int(input ("\t\tFinal : "))
				while True :
					if (p[fin2-1]!= ' ' ):
						print ("\t\t\tEspace vide non détecté à la case {} ..".format(fin2))
						fin2= int(input ("\t\tFinal : "))
						while fin2<=0 or fin2>9 :
							print("\t\t\tValeur hors plage,,")
							fin2= int(input ("\t\tFinal : "))
					else :
						break


			else :
				while True :
					if (p[init2-1]!= 'O' ):
						print ("\t\t\tPions 'O' non détecté à la case {} ..".format(init2))
						init2= int(input ("\t\tInitial : "))
						while init2<=0 or init2>9 :
							print("\t\t\tValeur hors plage,,")
							init2= int(input ("\t\tInitial : "))
					else :
						break

				while True :
					if (p[fin2-1]!= ' ' ):
						print ("\t\t\tEspace vide non détecté à la case {} ..".format(fin2))
						fin2= int(input ("\t\tFinal : "))
						while fin2<=0 or fin2>9 :
							print("\t\t\tValeur hors plage,,")
							fin2= int(input ("\t\tFinal : "))
					else :
						break

				break

		tmp=p[fin2-1]
		p[fin2-1]=p[init2-1]
		p[init2-1]= tmp
		cpt=0
		print ("")
		affiche(p)
		print ("")
		if decision(p,cpt)==1 :
			print ("\n\n\t*****************Bravo {} vous avez gagner !*****************\n\n\t\t\t\t(^-^)\n\n\n".format(nom1))
			break
		else :
			if decision(p,cpt)==2 :
				print ("\n\n\t****************Bravo {} vous avez gagner !****************\n\n\t\t\t\t(^-^)\n\n\n".format(nom2))
				break

		print ("")

	print ("\n\tVoulez vous continuez ? \n\t\t1-OUI\n\t\t2-NON")
	dec=int(input("\n\t~> "))
	while dec<=0 or dec>2 :
		print ("\n\tValeur hors plage..")
		dec=int(input("\n\t~> "))
	if dec==1 :
		print ("\n\n\tSuper! allons-y\n\n\n\n")
		tour = True
		continue
	else :
		print ("\n\n\n\tMerci . À bientôt !\n\n\n\n\n\n\n\n\n\n\n\t« By Dumping »\n\n\n\n\n")
		tour = False
		continue



