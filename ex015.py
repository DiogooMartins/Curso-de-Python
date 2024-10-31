km = float(input("Quantidade de Km rodados: "))
dias = int(input("Quantidade de dias alugados: "))
print("O preço a pagar por {} dias e {}Km é de R${:.2f}" .format(dias, km, (dias*60 + km*0.15)))
