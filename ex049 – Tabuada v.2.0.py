n = int(input("Digite um número: "))
print('=' * 35)
for c in range(1, 11):
 print('{} + {:2} = {:3}          {} - {:2} = {}'.format(n, c, n+c, n, c, n-c))