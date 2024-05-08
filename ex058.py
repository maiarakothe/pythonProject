import random
import time

jogador = ' '
cont = 0
computador = random.randint(0, 10)

print('Tente acertar o número que eu pensei!!')
print('-'*40)
while jogador != computador:
    jogador = int(input('Digite um número entre 1 e 10: '))
    print('PROCESSANDO...')
    cont += 1
    time.sleep(0.5)
    if jogador == computador:
        print('Parabéns você acertou o número!')
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Foram necessários {cont} palpites')