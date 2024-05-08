import random
import time
computador = random.randint(0, 5)
num = int(input('Digite um número entre 1 e 5: '))
print('PROCESSANDO...')
time.sleep(3)
if num == computador:
    print('Parabéns você acertou o número!')
else:
    print(f'Errou, eu pensei no {computador} e você digitou {num}')