print(f'{"Lojas Guanabara":=^40}')
produto = float(input('Digite o preço: '))
print('''Formas de pagamento:
 [1] à vista dinheiro/cheque
 [2] à vista cartão
 [3] 2x no cartão
 [4] 3x ou mais no cartão''')
pagamento = int(input('Qual a opção: '))

if pagamento == 1:
    valor = produto - (produto * 10 / 100)
elif pagamento == 2:
    valor = produto - (produto * 5 / 100)
elif pagamento == 3:
    valor = produto
    parcela = valor / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} sem juros')
elif pagamento == 4:
    valor = produto + (produto * 20/ 100)
    totparc = int(input('Quantas parcelas: '))
    parcela = valor / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f}')
else:
    valor = produto
    print('Opcão inválida de pagamento. Tente Novamente')

print(f'Sua compra de R${produto:.2f} vai custar R${valor:.2f} no final')