
n = str(input('Digite seu nome completo: ')).strip()

print(f'Seu nome com letras maiúsculas: {n.upper()}')
print(f'Seu nome com letras minúsculas: {n.lower()}')
print(f'Seu nome tem: {len(n) - n.count(' ')} letras')
# print(f'Seu primeiro nome tem {n.find(' ')} letras')
separa = n.split()
print('Seu primeiro nome é {} e tem {} letras ' .format(separa[0], len(separa[0])))
