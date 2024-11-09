#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.

numero = int(input("Digite um número de 0 a 9999: "))

#Caso tenha 4 digitos:
'''print("Unidade: {}".format(numero[3]))
print("Dezena: {}".format(numero[2]))
print("Centena: {}".format(numero[1]))
print("Milhar: {}".format(numero[0]))'''

#para poder ler números de com menos de 4 caracteres é melhor usarmos a forma matematica:

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print("Unidade: {}".format(unidade))
print("Dezena: {}".format(dezena))
print("Centena: {}".format(centena))
print("Milhar: {}".format(milhar))
