distancia = float(input('Qual a distância da viagem? '))

if distancia <= 200:
     preco = 0.50 * distancia
else:
    preco = 0.45 * distancia

print(f'A passagem será R${preco:.2f}')