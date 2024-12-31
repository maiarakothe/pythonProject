
lista = []*5

for cont in range(5):
    lista.append(int(input(f'Digite um valor para a posição {cont}: ')))

print(lista)
print(f'O maior valor digitado foi {max(lista)} nas posições {lista.count(max(lista))}..')
print(f'O menor valor digitado foi {min(lista)} nas posições {lista.index(min(lista))}..')