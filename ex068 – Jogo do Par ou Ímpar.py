from random import randint
print('-='*10, 'VAMOS JOGAR PAR OU ÍMPAR', '-='*10)
v = 0
while True:
    num = int(input("Escolha um valor: "))
    numPC = randint(0, 100)
    total = num + numPC
    jogador = ' '
    while jogador not in 'PpIi':
        jogador = str(input("Par ou Impar [P/I]: ")).strip()[0].upper()
    print(f"Você jogou {num} e o computador {numPC}. Total de {total}")
    if jogador == 'P':
        if total % 2 == 0:
             print("Você VENCEU!")
             v += 1
        else:
            print("Você PERDEU!")
            break
    elif jogador == 'I':
        if total % 3 == 0:
            print("Você VENCEU!")
            v +=1
        else:
            print("Você PERDEU!")
            break
    print("=**=*=*=*=**= Vamos jogar novamente! =**=*=*=*=**=")
print(f"GAME OVER! Você venceu {v} vezes.")

