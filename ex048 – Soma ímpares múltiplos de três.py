print("A soma dos números ímpares de 1 a 500, múltiplos de 3 é:")
soma = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        soma  = soma + c
print(soma)