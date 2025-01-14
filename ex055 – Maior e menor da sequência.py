maior = 0
menor = 0
for p in range(1,6):
    peso: float = float(input("Digite o peso em kg da {}° pessoa: ".format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print("\nO maior peso foi {}kg e o menor foi {}kg".format(maior, menor))
