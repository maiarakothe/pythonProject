import random
a1 = str(input('Digite seu nome: '))
a2 = str(input('Digite seu nome: '))
a3 = str(input('Digite seu nome: '))
a4 = str(input('Digite seu nome: '))

lista = [a1, a2, a3, a4]
e = random.choice(lista)

print(f'O aluno escolhido foi {e}')