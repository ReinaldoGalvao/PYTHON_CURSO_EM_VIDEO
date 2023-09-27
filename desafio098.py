'''
Faça um programa que tenha uma função chamada contador()
quer receba três parâmetros:inicio, fim e passo e realize a contagem.

Seu programa tem que realizar três contagens atraves da fução criada:

A) De 1 até 10, de 1 em 1
B) De 10 ate 0, de 2 em 2
C) Uma contagem personalizada.
'''
from time import sleep
def escreva(txt):
    tamanho = len(txt) +1
    print('='*tamanho)
    sleep(0.5)
    print(txt)
    sleep(0.5)
    print('='*tamanho)

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    escreva(f'Contagem de {i} até {f} em {p}') #função dentro de outra função
    if i <= f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont +=p
        print('FIM!')
        
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -=p
        print('FIM!')
contador (1, 10, 1)
contador (10, 0, 2)

escreva(' Contagem personalizada')

inicio = int(input('Inicio: '))
fim = int(input('Fim:       '))
passo = int(input('Passo:   '))

contador(inicio, fim, passo)
