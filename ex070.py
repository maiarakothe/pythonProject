soma = cont = 0
menor = float('inf')
barato = ' '
print('-'*30)
print('LOJA SUPER BARATÃO')
print('-'*30)
while True:
    nome = input('Nome do produto: ')
    preco = float(input('Preço: R$'))
    soma += preco
    if preco < menor:
        menor = preco
        barato = nome
    if preco > 1000:
        cont += 1
    res = ' '
    while res not in 'SN':
        res = input('Quer continuar? [S/N] ').upper().strip()[0]
    if res == 'N':
        break
print('-'*30)
print(f'O total gasto foi de R${soma:.2f}')
print(f'Temos {cont} produtos que custam mais de R$1000 reais.')
print(f'O produto mais barato é {barato} por R${menor}')