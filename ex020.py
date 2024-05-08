from random import shuffle
a1 = str(input('Digite seu nome: '))
a2 = str(input('Digite seu nome: '))
a3 = str(input('Digite seu nome: '))
a4 = str(input('Digite seu nome: '))

lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'A ordem será {lista}')
