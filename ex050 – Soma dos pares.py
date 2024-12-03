soma = 0
cont = 0
for c in range(0, 6):
    n = int(input("Digite o {} nùmero: ".format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print("Você informou {} números pares é a soma deles é {}".format(cont, soma))