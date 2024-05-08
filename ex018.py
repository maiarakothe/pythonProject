import math
a = float(input("Digite o ângulo que você deseja: "))
se = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print(f'O ângulo de {a} tem o SENO de {se:.2f}')
print(f'O ângulo de {a} tem o COSSENO de {cos:.2f}')
print(f'O ângulo de {a} tem o TANGENTE de {tan:.2f}')