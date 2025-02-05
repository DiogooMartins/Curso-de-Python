print("-="*8, "TABUADA", "-="*8)
while True:
    num = int(input("Digite um numero (negativo para parar): "))
    print('=*=' * 35)
    if num < 0:
        break
    for t in range(1,11):
        print(f"{num} + {t} = {(num + t)}", ' '*13, f"{num} - {t} = {num - t}", ' '*10, f"{num} x {t} = {num * t}", ' '*10, f"{num} : {t} = {(num / t):.2f}")
    print('=*=' * 35)
