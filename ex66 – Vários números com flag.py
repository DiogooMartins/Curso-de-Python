totalnum = soma = 0
while True:
    num = int(input("Digite um numero [999 para parar]: "))
    if num == 999:
        break
    totalnum += 1
    soma += num

print(f"Você digitou {totalnum} números e o resultado da soma entre eles é {soma}!")