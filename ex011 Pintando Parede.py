largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = altura * largura
ltinta = 2 #por metro²
print('Sua parede tem a dimensão de {}x{} e sua aréa é de {}m²'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta'.format(area/ltinta))