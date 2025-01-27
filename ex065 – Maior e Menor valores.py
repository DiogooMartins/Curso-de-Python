resp = ''
cont = media = maior = menor = 0
while resp != 'N':
    num = int(input("Digite um número: "))
    media += num
    cont += 1
    if cont == 1:
            maior = num
            menor = num
    else:
        if num > maior:
                maior = num
        if  num < menor:
                menor = num
    resp = str(input("Deseja digitar outro número? [S/N] ")).strip()[0].upper()
    while resp != 'S' and resp != 'N':
        print("Resposta Invalida!")
        resp = str(input("Deseja digitar outro número? [S/N] ")).strip()[0].upper()
media /= cont
print("\nA média entre os {} números informados é: {:.2f}".format(cont, media))
print("O maior número foi {} e o menor foi {}".format(maior, menor))
