
palavras = ('aprender', 'programar', 'linguagem', 'curso',
            'python', 'brincar', 'estudar', 'ligar'
            'jogar', 'praticar', 'futuro', 'programador')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')