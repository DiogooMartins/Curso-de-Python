altura = float(input("Qual a sua altura?(m) "))
peso = float(input("Qual o seu peso?(kg) "))
imc = peso / (altura ** 2)    #Índice de Massa Corporal (IMC)
print("\nO seu IMC é de {:.2f}".format(imc))
if imc < 18.5:
    print("Você está a baixo do peso normal!")
elif 25 <= imc >= 18.5:
    print("Você está no peso ideal!")
elif imc > 25 and imc <= 30:
    print("Você está com sobrepeso!")
elif imc > 30 and imc <= 40:
    print("Você possui obsidade, cuidado!")
else:
    print("Você possui obsidade mórbita, cuidado!")