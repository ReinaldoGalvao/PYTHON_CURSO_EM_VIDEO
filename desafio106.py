'''
Faça um mini-sistema que utilize o iteractiveHelp do Python.
O usuario vai digitar o comando e o manual vai aparecer.
Quando o usuario digitar a palavra 'FIM', o programa se encerra.
OBS: use cores.
'''
from time import sleep
c = ('\033[m',      #sem cor
    '\033[0;30;41m',#1 - vermelho
    '\033[0;35;46m',#2 - magenta
    '\033[0;31;47m',#3 - vermelho, fundo branco
    '\033[0;32;40m',#4 - verde, fundo preto
    '\033[0;37;42m',#5 - branco, fundo verde
    '\033[0;34;43m' #6 - azul
    )

def ajuda(com):
    titulo(f'Acessando o manual do comando\'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    print(c[cor], end='')
    tam = len(msg) +4
    print('=' * tam)
    print(f'  {msg}')
    print('=' * tam)
    print(c[0], end='')
    #sleep(1)

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 4)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 3)