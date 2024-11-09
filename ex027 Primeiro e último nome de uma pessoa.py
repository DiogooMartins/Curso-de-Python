#Faça um programa que leia o nome completo de uma pessoa e mostre em o primeiro e ultimo nome.

nome = str(input("Digite seu nome completo: ")).strip().lower()
separar = nome.split()
print("O seu primeiro nome é: {}".format(separar[0].title()))
print("O seu último nome é: {}".format(separar[len(separar)-1].title()))
