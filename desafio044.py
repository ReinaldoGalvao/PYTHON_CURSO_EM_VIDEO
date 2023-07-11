'''
Faça um programa que calcule o valor a ser pago por um produto, cosiderando o seu 
preço normal e condiçao de pagamento

À vista dinherio / pix: 10% de desconto
2x no cartao: 5% de desconto
3x ou mais no cartao: 20% juros
'''


preco_normal = float(input('Dia o valor da caisa: '))

x2_cartao = preco_normal - (preco_normal * 0.05)

x3_cartao = ( preco_normal * 0.20 ) + preco_normal

print(preco_normal)
print(x2_cartao)
print(x3_cartao)

print(f'O preço da camisa custa: \n Preço normal {preco_normal - 0.005:.2f} \n Preço 2x cartão {x2_cartao - 0.005} \n Preço 3x cartão ou mais {x3_cartao - 0.005:.2f}   ')