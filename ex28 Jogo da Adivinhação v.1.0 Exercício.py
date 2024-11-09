from random import randint
from time import sleep

print("=#=" * 20)
print(" " * 20, "TENTE ADIVINHAR")
print("=#=" * 20)
numpc = randint(0, 5)
numero = int(input("\nEm qual número de 0 a 5 eu estou pensando? "))
print("PROCESSANDO....")
sleep(2)
if numpc == numero:
    print("Incrível, Você acertou!!")
else:
    print("Você errou, eu pensei no número {} tente novamente!".format(numpc))
