'''
Crie um programa que leia o nome e o preco
de varios produtos
O programa devera perguntar se o usuario vai continuar.
No final mostre:

(A) Qual é o total gasto na compra.
(B) Qunatos produtos custam mais de R$1000
(C) Quel é o nome do produto mais barato
'''
total = 0
preco1000 = 0
nome_barato = ''
preco_barato = 0
primeira_vez = True

while True:
    item = input(f'Qual o nome do item: ').strip().capitalize()
    while not item.isalpha():
        item = input(f'Qual o nome do item: ').strip().capitalize()
    
    preco = input(f'Qual o valor do item: ').strip()
    while not preco.isdigit():
        preco = input(f'Qual o valor do item: ').strip()
    preco = int(preco)
    if primeira_vez:
        preco_barato = preco
        primeira_vez = False
        nome_barato = item
    total = total + preco
    if preco > 1000:
        preco1000 += 1
    if preco < preco_barato:
        nome_barato = item
    pergunta = input('Quer parar? [S/N]').strip().upper()
    if pergunta == 'S':
        break
print(f'O total da compra é de {total}')
print(f'Foram {preco1000} items custando acima de R$1.000')
print(f'O item mais barato é o {nome_barato}')