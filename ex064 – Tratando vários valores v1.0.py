num = int(input("Digite um número: "))
soma = num
cont = 1
while num != 999:
    print("Para finalizar: 999")
    num = int(input("Digite outro número: "))
    if num == 999:
        print("Programa finalizado!")
    else:
        soma += num
        cont += 1
print("Você digitou {} números e a soma desses números é: {}". format(cont, soma))
