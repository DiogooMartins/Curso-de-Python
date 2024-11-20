salario = float(input("Qual o seu salário? "))
if salario <= 1250:
    salnovo = salario * (1.15) #ou salario * (salario * 15/100)
    print("Com base no salário de {}, o seu salario aumentará 15% e ficará: {:.2f}". format(salario, salnovo))
else:
    salnovo = salario * (1.1)
    print("Com base no salário de R${}, o seu salario aumentará 10% e ficará: R${:.2f}".format(salario, salnovo))
