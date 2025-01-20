
num = int(input("Digite um número para calcular o Fatorial: "))
fatorial = 1
print('{}! = '.format(num), end='')
while num > 0:
    print(num, end='')
    print(" x " if num > 1 else " = ", end='')
    fatorial *= num
    num -= 1
print(fatorial)