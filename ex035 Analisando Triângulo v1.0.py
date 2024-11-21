print("=="*10, "Analisando Triângulos", "=="*10)

reta1 = float(input("\nPrimeiro segmento: "))
reta2 = float(input("Segundo segmento: "))
reta3 = float(input("Terceiro segmento: "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("Os segmentos acima PODEM formam um triângulo.")
else:
    print("Os segmentos acima NÃO podem formar um triângulo.")
