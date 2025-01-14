idademedia = 0
somaidade = 0
idadehmaisvelho = 0
nomemaisvelho = 0
totalmulher = 0
for pessoas in range(1, 5):
    print("----- {}ª PESSOA -----".format(pessoas))
    nome = str(input("Digite o nome da {}° pessoa: ".format(pessoas))).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: "))
    somaidade += idade
    if pessoas == 1 and sexo in 'Mm':
        idadehmaisvelho = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > idadehmaisvelho:
        idadehmaisvelho = idade
        nomemaisvelho = nome
    if idade < 20 and sexo in 'Ff':
        totalmulher += 1
idademedia = somaidade / 4
print("A idade media das quatro pessoas é de {} anos".format(idademedia))
print("O homem mais velho tem {} anos e se chama {}".format(idadehmaisvelho, nomemaisvelho))
print("{} mulher/mulheres tem menos de 20 anos".format(totalmulher))