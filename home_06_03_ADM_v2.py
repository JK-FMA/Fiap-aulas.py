#!/usr/bin/python3
user = input("Informe o seu nivel de usuario. (ADM, USR, GUEST) \n").upper()
sex = input("Informe o seu sexo \n (H)omem	(M)ulher \n").upper()
i = int(1)

while sex != "H" and sex != "M" :
	
	sex = input("Informe somente H para homem ou M para mulher \n").upper()

if sex == "H":
	if user == "ADM":
		print ("Ola administrador")
	elif user == "USR" :
		print ("Ola usuario")
	elif user == "GUEST":
		print ("Ola convidado")
	else:
		print ("Ola desconhecida")
else:
	if user == "ADM":
                print ("Ola administradora")
	elif user == "USR" :
                print ("Ola usuaria")
	elif user == "GUEST":
                print ("Ola convidada")
	else:
                print ("Ola desconhecida")
