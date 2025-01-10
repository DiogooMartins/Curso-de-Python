num = int(input("Digite um número: "))
total = 0
for c in range(1,num + 1 ):
    if num % c == 0:
        print("\033[34m", end=" ")
        total += 1
    else:
        print("\033[m", end=" ")
    print(c, end=' ')
print("\n\033[mO número {} foi divisível {} vezes". format(num, total))
if total == 2:
    print("Por isso é PRIMO")
else:
    print("Por isso não é PRIMO")