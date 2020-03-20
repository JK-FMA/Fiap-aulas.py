#!/bin/python3
curso = int(input("Informe o tipo de graduacao voce esta fazendo \n(1)tecnologo\n(2)bacharelado\n"))

while curso != 1 and curso !=2:
	print("###################################")
	curso = int(input("escolha somente: \n(1)tecnologo\n(2)bachalerado \n"))
	print("##################################")

if curso == 1:
	print("---------------------------------")
	print("so vai terminar daqui 2 ou 3 anos")
	print("---------------------------------")

elif curso == 2:
	print("---------------------------------")
	print("so vai terminar daqui 4 ou 6 anos")
	print("---------------------------------")

