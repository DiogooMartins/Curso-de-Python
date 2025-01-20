from time import sleep

valor1 = int(input("Digite o 1º valor: "))
valor2 = int(input("Digite o 2º valor: "))
res = 1
while res != 5:
    res = int(input('''\nO que deseja fazer agora: 
    [1] Somar 
    [2] Multiplicar 
    [3] Qual o maior 
    [4] Digitar novos numeros 
    [5] Sair do programa \n'''))
    if res == 1:
        print("A soma dos valores é: {}".format(valor1 + valor2))
        sleep(2)
    elif res == 2:
        print("A multiplicação dos valores é: {}".format(valor1 * valor2))
        sleep(2)
    elif res == 3:
        if valor1 > valor2:
            print("O maior valor é: {}".format(valor1))
            sleep(2)
        if valor2 > valor1:
            print("O maior valor é: {}".format(valor2))
            sleep(2)
    elif res == 4:
        valor1 = int(input("Digite novamente o 1º valor: "))
        valor2 = int(input("Digite novamente o 2º valor: "))
    elif res >= 6:
        res = int(input("Invalido, Escolha uma das opções acima: "))
print("Programa finalizado!")
