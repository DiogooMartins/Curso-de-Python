salario = float(input("Qual é o salário do funcionário? "))
porcentagem = float(input("Qual a porcentagem de aumento? "))
novosal = salario + (salario * porcentagem / 100)
print("Um funcionário que ganhava R${:.2f}, com {:.0f}% de aumento, passa a recber R${:.2f}" .format(salario, porcentagem, novosal))
