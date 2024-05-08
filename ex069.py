res = maior = cont = mulheres = 0
print('-'*25)
print('CADASTRE UMA PESSOA')
print('-'*25)

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    print('-' * 25)

    if idade > 18:
        maior += 1
    if sexo == 'M':
        cont += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1

    res = ' '
    while res not in 'SN':
        res = input('Quer continuar? [S/N]: ').upper().strip()[0]
    print('-' * 25)
    if res == 'N':
        break

print(f'{maior} pessoas tem mais de 18 anos!')
print(f'{cont} homens foram cadastrados!')
print(f'{mulheres} mulheres tem menos de 20 anos. ')