'''
Crie um programa que  leia o comprimento de 3 retas
e diga se ao usuario se elas poder ou nao formar um triangulo
'''
from rich import print

cores = {
    'limpa':'\033[m',
    'azul':'\033[34m',
    'amarelo':'\033[33m',
    'pretoebranco':'\033[7:30m'
    }

r1 = int(input('Diaga o comprimento da primeira reta: '))
r2 = int(input('Diaga o comprimento da segunda reta: '))
r3 = int(input('Diaga o comprimento da terceira reta: '))

if (r2 - r3) < r1 < r2 + r3 or (r1 - r3) < r2 < r1 + r3 or (r1 - r2) < r3 < r1 + r2:
    print('Pode formar um triangulo')
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('é um Equliátero')
        
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('é um Isósceles')
        
    else:
        print('é um Escaleno')
else:
    print('\033[0;34;4Nao pode')