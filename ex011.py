l = float(input('Qual a largura da parede em metros: '))
a = float(input('Qual a altura da parede em metros: '))

area = l * a
tinta = area / 2

print(f'Sua parede tem dimensão de {l}x{a} e sua área é de {area}m')
print(f'A quantidade de tinta necessária para pinta-la será {tinta}l')