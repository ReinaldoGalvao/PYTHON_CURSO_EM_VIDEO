'''
Faça um programa que calcule o valor a ser pago por um produto, cosiderando o seu 
preço normal e condiçao de pagamento

À vista dinherio / pix: 10% de desconto
2x no cartao: 5% de desconto
3x ou mais no cartao: 20% juros
'''
nome_loja = 'LOJAS BEMOS'
print(f'{nome_loja:=^40}')

preco = float(input('Diga o valor da compra: '))

print('''FORMAS DE PAGAMENTO 
[1] à vista DINHEIRO/PIX
[2] à vista CARTÃO
[3] 2X no CARTÃO
[4] 3X OU mais no CARTÃO''')

opcao = input('Digite qual é a opção: ')

while not opcao.isdigit() or int(opcao) not in [1, 2, 3, 4]:
    print('Opção inválida. Tente novamente.')
    opcao = input('Digite qual é a opção: ')

opcao = int(opcao)  # Converter para número inteiro

if opcao == 1:
    total = preco - (preco * 0.10)
    # Restante do código...
elif opcao == 2:
    total = preco - (preco * 0.05)
    # Restante do código...
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f}')
elif opcao == 4:
    total = preco + (preco * 0.20)
    totparc = input('Digite quantas parcelas: ')
    
    while not totparc.isdigit():
        totparc = input('Valor inválido. Digite novamente a quantidade de parcelas: ')
    
    totparc = int(totparc)
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} com juros')
    
else:
    print('Opção inválida. Tente novamente.')

print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')
