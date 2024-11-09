valor = float(input('Quanto dinheiro você tem na carteira?'))
dolar = 3.27
print('Você possui R${:.2f} e pode comprar US${:.2f}'.format(valor, valor/dolar))
