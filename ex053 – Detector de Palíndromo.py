frase = str(input("Digite uma frase: ")).upper().strip()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
print("O inverso de {} é {}".format(frase, inverso))
if inverso == junto:
    print("A frase digitada é palíndromo")
else:
    print("A frase digitada não é um palíndromo")
