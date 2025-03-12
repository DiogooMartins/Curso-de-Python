totvalor = mais1000 = maisbarato = prodbarato = cont = 0
while True:
    nome = str(input("Nome do produto: "))
    preco = float(input("Preço: "))
    totvalor += preco
    cont += 1
    if preco >= 1000:
        mais1000 += 1
    if cont == 1 or preco < maisbarato:
        maisbarato = preco
        prodbarato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    if resp == 'N':
        break
print(f"O total da compra foi R${totvalor:.2f}")
print(f"Temos {mais1000} produto(s) custando mais de R$1000,00.")
print(f"{prodbarato} é o produto mais barato, custando R${maisbarato:.2f}.")

