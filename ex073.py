
tabela = ('Botafogo', 'Flamengo', 'Bahia', 'Athletico-PR', 'Palmeiras', 'São Paulo', 'Bragantino',
          'cruzeiro', 'Atlético-MG', 'Internacional', 'Juventude', 'Fortaleza', 'Atlético-GO', 'Cuiabá',
          'Vasco', 'Corinthians', 'Grêmio', 'Criciúma', 'Fluminense', 'Vitória')

print('Os 5 primeiros colocados são:')
print(tabela[:5])
print('-'*60)

print('Os últimos colocados foram: ')
print(tabela[-4:])
print('-'*60)

print('Os times em ordem alfabética: ')
print(sorted(tabela))
print('-'*60)

print(f'O Chapecoense não está presente')