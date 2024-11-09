#Crie um programa que leia o nome completo de uma pessoa e mostre:
#Nome com letras maiúsculas, minúsculas, numero de letras(sem considerar espaços) e quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome completo: "))
print("Seu nome em maiúsculo é: {}".format(nome.upper()))
print("Seu nome em minúsculo é: {}".format(nome.lower()))
print("Seu nome completo tem {} letras".format(len(nome)-nome.count(" ")))
#print("Seu primeiro nome tem {} letras".format(nome.find(" ")))
separa = nome.split()
print("Seu primeiro nome tem {} letras".format(len(separa[0])))
