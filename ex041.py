from datetime import date
nascimento = int(input('Em qual ano você nasceu: '))

atual = date.today().year
idade = atual - nascimento

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')