from random import randint
numpc = randint (0,10)
numero = int(input("Em qual número de 0 a 10 eu estou pensando? "))
tentativastotal = 1
while numero != numpc:
    numero = int(input("Escolha outro número: "))
    tentativastotal += 1
    if numero < numpc:
        print("Mais...")
    elif numero > numpc:
        print("Menos...")
    elif numero == numpc:
        print("Parabéns, Você precisou de {} tentativas para descobrir que eu pensei no numero {}".format(tentativastotal, numpc))