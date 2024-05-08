from datetime import date
ano = date.today().year
maior = 0
menor = 0
for cont in range(1, 8):
    nasc = int(input(f'Em que ano a {cont} nasceu: '))
    idade = ano - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas são maiores de idade!')
print(f'{menor} pessoas são menores de idade!')
