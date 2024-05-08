carro = float(input('Digite a velocidade do carro: '))
if carro > 80:
    multa = (carro - 80) * 7
    print(f'Você foi multado, a multa será de {multa:.2f}')
else:
    print('Continue assim')