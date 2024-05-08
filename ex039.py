from datetime import date
nascimento = int(input('Em qual ano você nasceu: '))
atual = date.today().year
idade = atual - nascimento
sexo = input('Qual seu sexo (M/F):').upper()
print(f'Quem nasceu em {nascimento} tem {idade} anos')

if sexo == 'M':
    if idade < 18:
        saldo = 18 - idade
        print(f'Você ainda se alistará ao serviço militar, falta {saldo} anos')
        ano = atual + saldo
        print(f'Seu alistamento será em {ano}')
    elif idade == 18:
        print('É a hora de se alistar')
    elif idade > 18:
        saldo = idade - 18
        ano = atual - saldo
        print(f'Seu alistamento foi em {ano}')
        print(f'Você deveria ter se alistado faz {saldo} anos !')
else:
    print('Você não precisa se alistar!')

