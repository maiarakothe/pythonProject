r = 'S'
cont = soma = media = 0
maior = float('-inf')
menor = float('inf')
while r in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1

    if n > maior:
        maior = n
    if n < menor:
        menor = n

    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

media = soma / cont
print(f'A média dos números é {media:.2f}')
print(f'O maior número foi {maior} e o menor foi {menor}')