res = ' '
lista = []
while res != 'N':
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n in lista:
        if n == lista[n]:
            lista.remove(n)
            print('Valor não adicionado')
    res = input('Deseja continuar? [S/N] ').upper()
print(lista.sort())