maioridade = nhomens = nmulheres = 0
while True:
    print("-"*10, "CADASTRE UMA PESSOA", "-"*10)
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("Sexo [M/F]: ")).upper().strip()[0]
    parar = ' '
    while parar not in 'SN':
        parar = str(input("Deseja parar? [S/N] ")).upper().strip()[0]
    if idade >= 18:
        maioridade += 1
    if sexo == "M":
        nhomens += 1
    if sexo == 'F' and idade < 20:
        nmulheres += 1
    if parar == 'S':
        break
print(f"{maioridade} Pessoas possui mais de 18 anos.")
print(f"{nhomens} Homens foram cadastrados. ")
print(f"{nmulheres} Mulheres tem menos de 20 anos")