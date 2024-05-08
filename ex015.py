km = float(input('Quantos km o carro percorreu? '))
dias = int(input('Quantos dias o carro foi alugado? '))

preco = (dias * 60) + (0.15 * km)

print(f'O preço a ser pago será de R${preco:.2f}')