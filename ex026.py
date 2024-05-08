
f = str(input('Digite uma frase: ')).strip().upper()

print(f'A letra A aparece {f.count('A')} vezes ')
print(f'A letra A aparece pela primeira vez na posição {f.find('A')+1}')
print(f'Aparece pela última vez na posição {f.rfind('A')+1}')