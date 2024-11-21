print("Digite três segmentos do triângulo! ")
seg1 = float(input("Primeiro segmento: "))
seg2 = float(input("Segundo segmento: "))
seg3 = float(input("Terceiro segmento: "))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print("\nOs segmentos acima PODEM formam um triângulo.")
    if seg1 == seg2 == seg3:
        print("E formam um triângulo EQUILÁTERO, pois todos os segmentos são iguais!")
    elif seg1 != seg2 != seg3 != seg1:
        print("E formam um triângulo ESCALENO, pois não possui segmentos iguais!")
    else:
        print("E formam um triângulo ISÓSCELES, pois dois lados são iguais!")
else:
    print("\nOs segmentos acima NÃO podem formar um triângulo.")
