'''
Desenvolva um programa que pergunte a distancia de uma viagem em km.
Calcule o preco da passagem, cobrando R$0,50 por km para viagem de até 200km
e R$0,45 para viagens mais longas.
'''
viagem = int(input('Diga de quantos kms será a viagem: '))
vcurta = 0.50
vlonga = 0.45

if viagem > 200:
    preco_vlonga = viagem * 0.45
    print(f'A sua viagem foi de {viagem}km e foi cobrado R${vlonga} por km percorrido dando o total de R${preco_vlonga:.2f}.')
else:
    preco_vcurta = viagem * 0.50
    print(f'A sua viagem foi de {viagem}km e foi cobrado R${vcurta} por km percorrido dando o total de R${preco_vcurta:.2f}.')