#Crie um progrma que leia o nome de uma cidade e diga se ela começa ou não com o nome "Uber"

cidade = str(input("Digite o nome de uma cidade: ")).strip()
print("Essa cidade começa com 'Uber'! ")
print(cidade[:4].lower() == 'uber')

