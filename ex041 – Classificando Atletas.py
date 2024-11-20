from datetime import date
ano = date.today().year
anonasc = int(input("Em que ano você nasceu? "))
idade = ano - anonasc

if idade <= 9:
    print("Atleta MIRIM!")
elif idade > 9 and idade <= 14:
    print("Atleta INFANTIL!")
elif idade > 14 and idade <= 19:
    print("Atleta JUNIOR!")
elif idade == 20:
    print("Atleta SÊNIOR!")
else:
    print("Atleta MASTER!")
