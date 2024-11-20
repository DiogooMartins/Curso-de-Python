vel = float(input('Qual a velocidade do carro? '))
multa = (vel- 80)* 7
if vel > 80:
    print("Multado, Você excedeu o limite de velocidade!")
    print("Você foi multado em R${:.2f}".format(multa))
else:
    print("Você esta dentro do limite de velocidade, tenha uma boa viagem!")
