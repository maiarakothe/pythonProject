import random
print('=-'*16)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*16)

soma = cont = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = random.randint(0, 10)
    soma = jogador + computador
    escolha = ' '

    while escolha not in 'PI':
        escolha = str(input('Par ou ímpar? [P/I] ')).upper().strip()[0]
    print('-' * 16)

    if soma % 2 == 0:
        resultado = f'Deu PAR'
    else:
        resultado = f'Deu Ímpar'

    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} {resultado}')
    print('-' * 20)

    if escolha == 'P' and soma % 2 == 0:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('-' * 20)
        cont += 1
    elif escolha == 'I' and soma % 2 == 1:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('-' * 20)
        cont += 1
    else:
        print('Você PERDEU!')
        print(f'GAME OVER! Você venceu {cont} vezes!')
        break