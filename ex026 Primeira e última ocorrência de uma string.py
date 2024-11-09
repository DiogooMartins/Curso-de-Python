#Faça um programa que leia uma frase pelo teclado e mostre:
#quantas letras A tem, primeira e ultima posição da letra A.

frase = str(input('Digite uma frase: ')).lower().strip()
print("A letra 'A' aparece {} vezes".format(frase.count('a')))
print("A primeira letra 'A' apareceu na posição: {}".format(frase.find('a')))
print("A última letra 'A' apareceu na posição: {}".format(frase.rfind('a')))

