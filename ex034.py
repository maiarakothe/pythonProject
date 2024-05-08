salario = float(input('Digite seu salário: '))

if salario > 1250:
    aumento = salario + (salario * 10 / 100)
    print(f'Seu aumento com 10% será de {aumento:.2f}')
else:
    aumento = salario + (salario * 15 / 100)
    print(f'Seu aumento com 15% será de {aumento:.2f}')