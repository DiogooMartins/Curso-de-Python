print("=*"*5 , "10 TERMOS DE UM PA" , "*="*5)
ptermo = int(input("Digite o primeiro termo: "))
razão = int(input("Digite a razão: "))
décimo = ptermo + 10 * razão
for n in range(ptermo,décimo, razão):
    print(n, end=" → ")
print("Acabou")