preço = float(input("Qual o valor do produto? R$"))
print("\n{:=^40}".format(' Formas de pagamento '), '''
[ 1 ] À vista no Dinheiro / Cheque (\033[34m 10% de desconto \033[m)
[ 2 ] À vista no Cartão (\033[34m 5% de desconto \033[m)
[ 3 ] Até 2x no cartão (\033[34m sem juros \033[m)
[ 4 ] A partir de 3x no cartão (\033[34m 20% de juros \034[m)''')
forpag = int(input("\033[mEscolha a forma de pagamento: \033[m"))

if forpag == 1:
    valor = preço - (preço * 10 / 100)
    print("\nCom 10% de desconto o produto custurá: R${:.2f}".format(valor))
elif forpag == 2:
    valor = preço - (preço * 5 / 100)
    print("\nCom 5% de desconto o produto custurá: R${:.2f}".format(valor))
elif forpag == 3:
    valor = preço / 2
    print("\nVocê irá pagar 2x de R${:.2f}".format(valor))
elif forpag == 4:
    valor = preço + (preço * 20 / 100)
    parcela= int(input("Em quantas parcelas? "))
    parc = valor / parcela
    print("\nO produto custará R${:.2f}".format(valor))
    print("Dividindo irá custar {}x de R${:.2f}".format(parcela, parc))
else:
    print("Forma de pagamento invalida...")

