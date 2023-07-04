"""
Escreva um programa que fala o computador 'pensar' em um numero inteiroentre 0 e 5
e peça para o usuario tentar descrir qual foi o numero escolhido pelo computador.
o programa devera escrever na tela se o usuario venceu ou perdeu.
"""
import random
numeropc = random.randint(0, 5)

numerousuario = int(input('Escolha um numero entre 0 e 5: '))
while numerousuario < 0 or numerousuario > 5:
    numerousuario = int(input('O numero tem que ser entre 0 e 5: '))

if numeropc == numerousuario:
    print(f'Prabens voce acertou o numero escolhido pelo PC foi {numeropc}.')
else:
    print(f'Você perdeu, o numero escolhido pelo PC foi {numeropc}')
