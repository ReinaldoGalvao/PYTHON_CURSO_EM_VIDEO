'''
Melhore o desafio 28 onde o computador vai pensar em um numero
entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar
mostrando no final quantos palpites foram necessarios para vencer.
'''

import random
numeropc = random.randint(0, 10)

numerousuario = 11
numero_erro = 1
'''while numerousuario < 0 or numerousuario > 100:
    numerousuario = int(input('O numero tem que ser entre 0 e 100: '))'''

while numerousuario != numeropc:
    numerousuario = int(input('Escolha um numero entre 0 e 10: '))
    if numeropc > numerousuario:
        print('Chutou baixo.')
        numero_erro += 1
    elif numeropc < numerousuario:
        print('Chutou alto.')
        numero_erro += 1
    else:
        print('ACERTOU!!!!!\nVocê precisou de {} tentativas para acertar.'.format(numero_erro))