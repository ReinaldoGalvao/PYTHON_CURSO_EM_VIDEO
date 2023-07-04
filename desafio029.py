'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h uma mensagem dezendo que ele foi multado.
A multa vai custar R$7,00 por cada KM acima do permitido. 
'''

velocidade = int(input('Diga a velocidade do carro: '))
velocidade_max = int(input('Diga o maximo permitido na via: '))

if velocidade < velocidade_max:
    print(f'Você está a {velocidade} e nao ultrapassou a velocidade maxima permitida, PARABENS')
    
else:
    valor_multa = (velocidade - velocidade_max) * 7
    velocidade_acima = velocidade - velocidade_max
    print(f'Voce foi multado em R${valor_multa:.2f} por passar a {velocidade}km/hs, {velocidade_acima}km/hs a cima do permitido na via.')