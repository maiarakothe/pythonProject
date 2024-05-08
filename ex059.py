n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opcao = 0
while opcao != 5:
    print(' - '*20)
    print('''O que você deseja fazer com os números:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao = int(input('Opção: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}')
    elif opcao == 2:
        multiplicar = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é {multiplicar}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O número {n1} é maior!')
        elif n2 > n1:
            print(f'O número {n2} é maior!')
        else:
            print(f'Os dois números são iguais!')
    elif opcao == 4:
        n1 = int(input('Digite um novo número: '))
        n2 = int(input('Digite outro número: '))
    elif opcao == 5:
        print('Saindo...')
    else:
        print('Número ínvalido, tente novamente')
print('Acabou')