'''
Faça um programa que tenha uma lista chamada numeros e duas funçoes
chamadas sorteia() e somaPar().A primeira função vai sortear 5 numeros
e vai coloca-los dentro da lista e a segunda função vai mostrar a soma 
entre todos os valores PARES sorteados pela função anterior
'''


from random import randint
from time import sleep
"""
def sorteia():
    numeros = []
    for _ in range(5):
        numeros.append(randint(1, 10))
    return numeros

def somaPar(numeros):
    soma = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma += numero
    return soma

numeros = sorteia()
print(f'Números sorteados: {numeros}')
soma_pares = somaPar(numeros)
print(f'Soma dos números pares: {soma_pares}')


"""
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cost in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
            sleep(0.3)
    print(f'Somando os valores para de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)




