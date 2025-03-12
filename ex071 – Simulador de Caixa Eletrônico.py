valor = int(input("Digite o valor você deseja sacar: R$"))
cedula = 100
totced = 0
while True:
    if valor >= cedula:
        valor -= cedula
        totced += 1
    else:
        if totced > 0:
            print(f"Total de {totced} cédulas de R${cedula}")
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        totced = 0
        if valor == 0:
            break