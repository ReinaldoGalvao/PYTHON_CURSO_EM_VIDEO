#faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input('Diga o preço da camisa: '))
desconto = float(input('Diga qual o valor do desconto: '))

desconto_porcento = desconto / 100

preco_final = preco - (preco * desconto_porcento)

print(f'O valor com o desconto de {desconto}% é de {preco_final}.')
