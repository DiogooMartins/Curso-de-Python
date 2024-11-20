km = float(input("Qual a distância da viagem em Km? "))
ate = km * 0.50
acima = km * 0.45
if km <= 200:
    print("Rodando {}Km você pagará R${:.2f} na passagem".format(km, ate))
else:
    print("Radando {}Km você pagará R${:.2f} na passagem".format(km, acima))
print("Boa viagem!")

#preço = km * 0.50 if km <= 200 else km * 0.45
