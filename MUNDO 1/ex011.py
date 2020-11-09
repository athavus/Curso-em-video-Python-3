alt = float(input('Altura da parede em metros: '))
larg = float(input('Largura da parede em metros: '))
area = alt * larg
tinta = area / 2
print(f'Sua parede tem dimensão de {alt}x{larg} e sua área é {area:.3f}m²')
print(f'Para pintar essa parede, você precisará de {tinta}l de tinta')
