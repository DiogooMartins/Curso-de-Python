numero = int(input("Escreve um número inteiro: "))
print("Escolha a base de conversão: \n [ 1 ] Binário\n [ 2 ] Octal\n [ 3 ] Hexadecimal ")
base = int(input("Qual a base de conversão? "))

if base == 1:
    print("O número {} convertido para binário ficará: {:}".format(numero, bin(numero)[2:]))

elif base == 2:
    print("o número {} convertido para octal ficará: {:}".format(numero, oct(numero)[2:]))

elif base == 3:
    print("O numero {} convertido para hexadecimal ficará: {:}".format(numero, hex(numero)[2:]))

else:
    print("Opção invalida...")

