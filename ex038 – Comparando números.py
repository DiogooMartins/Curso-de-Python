numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

if numero1 > numero2:
    print("O primeiro número ({}) é o maior!".format(numero1))
elif numero2 > numero1:
    print("O segundo número ({}) é o maior!".format(numero2))
else:
    print("Não existe valor maior. Os dois são iguais!")