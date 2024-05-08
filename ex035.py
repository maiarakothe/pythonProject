print('='*20)
print('Analisador de Triângulos')
print('='*20)
n1 = int(input('Primeiro segmento: '))
n2 = int(input('Primeiro segmento: '))
n3 = int(input('Primeiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima PODEM FORMAR um triângulo')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
