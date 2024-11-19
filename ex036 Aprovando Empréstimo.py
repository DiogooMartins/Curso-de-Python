valorc = float(input("Informe o valor da casa: "))
salario = float(input("Informe qual e o seu salário: "))
anos = int(input("Em quantos anos deseja pagar? "))

valormensal = valorc / (anos * 12)

if valormensal <= salario * 30/100:
    print("Empréstimo aprovado! Você pagará R${:.2f} por mês" .format(valormensal))
else:
    print("Empréstimo negado!")
