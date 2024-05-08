soma = 0
maior = float('-inf')
homem = ' '
mulheres = 0
for p in range(1, 5):
    print(f'--- {p} PESSOA ----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (F/M): ').upper()

    soma = soma + idade

    if sexo == 'M' and idade > maior:
        maior = idade
        homem = nome

    if idade < 20 and sexo == 'F':
        mulheres += 1

media = soma / 4
print(f'A média de idade é {media} anos.')
print(f'O homem mais velho é o {homem} com {maior} anos.')
print(f'{mulheres} mulheres tem menos que 20 anos.')
