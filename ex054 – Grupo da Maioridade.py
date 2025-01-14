#from _datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for c in range (1, 8):
    ano = int(input("Digite o ano de nascimento da {}ª pessoa: ".format(c)))
    idade = atual - ano
    print("Essa pesoa fez ou irá fazer {} anos este ano\n". format(idade))
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print("\033[34m{}\033[m pessoas são maiores de idade e \033[34m{}\033[m pessoas são menores de idade!".format(totalmaior, totalmenor))