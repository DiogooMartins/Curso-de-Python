from random import randint

print(" " * 10, "VAMOS JOGAR PEDRA, PAPEL OU TESOURA")
itens = ('Pedra', 'Papel', 'Tesoura')
escpc = randint(0,2)
escolha = int(input("Opções: \n[ 0 ] Pedra \n[ 1 ]Papel \n[ 2 ]Tesoura \nQual a sua escolha? "))
print("=#=" * 10)
print("Você jogou {}".format(itens[escolha]))
print("O computador jogou {}".format(itens[escpc]))
print("=#=" * 10)
if escpc == escolha:
    print("Empatamos, Vamos jogar novamente!")
elif escpc == 0 and escolha == 2:
    print("VOCÊ PERDEU! Pedra amassa tesoura!")
elif escpc == 2 and escolha == 1:
    print("VOCÊ PERDEU! Tesoura corta papel!")
elif escpc == 1 and escolha == 0:
    print("VOCÊ PERDEU! Papel embrulha pedra!")
elif escolha == 0 and escpc == 2:
    print("VOCÊ GANHOU! Pedra amassa tesoura!")
elif escolha == 2 and escpc == 1:
    print("VOCÊ GANHOU! Tesoura corta papel!")
elif escolha == 1 and escpc == 0:
    print("VOCÊ GANHOU! Papel embrulha pedra!")
