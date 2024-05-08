casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual seu salário:'))
ano = int(input('Quantos anos de financiamento: '))

pres = casa / (ano * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de {casa:.2f} em {ano} anos, a prestação será de R${pres:.2f}')

if pres <= minimo:
    print('Empréstimo concedido')
else:
    print('Não concedido')

