maior = float('-inf')
menor = float('inf')
for cont in range(1, 6):
    peso = float(input(f'Digite o peso da {cont} pessoa: '))

    if peso > maior:
        maior = peso

    if peso < menor:
        menor = peso

print(f'O maior peso é {maior:.2f}')
print(f'O menor peso é {menor:.2f}')
