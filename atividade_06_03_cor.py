nome = input("Informe o nome do paciente \n")
idade = int(input("Informee a idade \n"))

gpr = input("O paciente eh de risco ? (S)im ou (N)ao")
if gpr != "S" and gpr != "N":
    gpr = input("O paciente eh de risco ? (S)im ou (N)ao \n Use SOMENTE S ou N")

#gpr = input("O paciente é ja teve ou tem alguma doença grave realiconada "
#                +"ao sistema respiratorio? se sim, qual? (informe N para não)")

nome = nome.title()
gpr = gpr.upper()

if idade <15:
    print("Pessoa prioritaria")
elif idade > 60:
     print("Pessoa prioritaria")
elif gpr != "N":
    print("Pessoa prioritaria")
else:
    print("Foi mal filhao, vc vai morrer na fila")

