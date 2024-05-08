cont = 0
while True:
    print('-' * 34)
    n = int(input('Quer ver a tabuada de qual valor: '))
    if n < 0:
        break
    print('-' * 34)
    while cont < 10:
        cont += 1
        print(f'{n} x {cont} = {n * cont}')
print('PROGRAMA TABUADA ENCERRADO. Volte, sempre!')