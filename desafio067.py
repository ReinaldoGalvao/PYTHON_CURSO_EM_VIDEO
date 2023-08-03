'''
Faça um programa que mostre a tabuada de varios numeros
um de cada vez, para cada valor digitado pelo usuario
O programa será interrompido quando o número solicitado for negativo
'''

numero = 0
while True:
    print(f'==========-TABUADA-===========')
    numero = int(input('Diga um número: '))
    print(f'==============================')
    if numero < 0:
        break
    for i in range(1, 11):
        print(f'{numero} x {i} = {i*numero}')
    print(f'\n')