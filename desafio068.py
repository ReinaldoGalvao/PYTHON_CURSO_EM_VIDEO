'''
Faça um programa que jogue par ou impar com o computador
O jogo só será interrompido quando o jogador perder
mostrando o total de vitorias consecultivas que ele conquistou no final do jogo
'''

from random import randint
win = 0
while True:
    strnumero = input(f'Diga um numero: ')
    while not strnumero.isdigit():
        strnumero = input('Diga um numero: ')
    numero = int(strnumero)

    parouimpar = input(f'Par ou Ímpar? [P/I]').strip().upper()
    while parouimpar != 'P' and parouimpar != 'I':
        parouimpar = input(f'Par ou Ímpar? [P/I]').strip().upper()
        continue
    numeropc =  randint(0, 100)
    soma = numero + numeropc
    if soma %2 == 0 and parouimpar == 'P':
        win += 1
        print(f'Vitória')
        print(f'Voce escolheu {numero} e o pc {numeropc} e a soma deles é {soma}')

    elif soma %2 != 0 and parouimpar == 'I':
        win += 1
        print(f'Vitória')
        print(f'Voce escolheu {numero} e o pc {numeropc} e a soma deles é {soma}')
    else:
        print('GAME OVER')
        break
print(f'Voce escolheu {numero} e o pc {numeropc} e a soma deles é {soma}')
print(f'Nessa rodada você teve {win} vitórias.')

