print("=="*5, "Digite 3 números", "=="*5)
primeiro = int(input("Primeiro número: "))
segundo = int(input("Segundo número: "))
terceiro = int(input("Terceiro número: "))

menor = primeiro
if segundo < primeiro and segundo < terceiro:
    menor = segundo
if terceiro < primeiro and terceiro < segundo:
    menor = terceiro
print("O menor número é {}".format(menor))

maior = primeiro
if segundo > primeiro and segundo > terceiro:
    maior = segundo
if terceiro> primeiro and terceiro > segundo:
    maior = terceiro
print("O maior número é {}".format(maior))
