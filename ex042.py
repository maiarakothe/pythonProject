print('='*20)
print('Analisador de Triângulos')
print('='*20)
n1 = int(input('Primeiro segmento: '))
n2 = int(input('Primeiro segmento: '))
n3 = int(input('Primeiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima PODEM FORMAR um triângulo')
    if n1 == n2 == n3:
        print('Equilátero')
    elif n1 != n2 != n3 != n1:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')