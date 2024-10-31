valor = float(input('Qual o valor do produto? '))
desconto = float(input('Qual a porcentagem de desconto? '))
porcentagem = (desconto * valor)/100
print("o produto que custava R${}, na promoção com desconto de {:.0f}% vai custar R${:.2f}" .format(valor, desconto, valor - porcentagem))