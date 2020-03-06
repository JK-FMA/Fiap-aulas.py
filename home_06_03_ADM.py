#!/usr/bin/python3
user = input("Informe o seu nivel de usuario. (ADM, USR, GUEST) \n").upper()
sex = input("Informe o seu sexo \n (H)omem	(M)ulher \n").upper()
i = int(1)

while i >0 :
	if sex != "H" and sex != "M":
		sex = input("Informe somente H para homem ou M para mulher \n").upper()
	else:
		i = 0

if sex == "H":
	if user == "ADM":
		print ("Ola administrador")
	elif user == "USR" :
		print ("Ola usuario")
	elif user == "GUEST":
		print ("Ola convidado")
	else:
		print ("Ola desconhecido")
else:
	if user == "ADM":
                print ("Ola administrador")
	elif user == "USR" :
                print ("Ola usuario")
	elif user == "GUEST":
                print ("Ola convidado")
	else:
                print ("Ola desconhecido")
