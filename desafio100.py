'''
Faça um programa que tenha uma lista chamada numeros e duas funçoes
chamadas sorteia() e somaPar().A primeira função vai sortear 5 numeros
e vai coloca-los dentro da lista e a segunda função vai mostrar a soma 
entre todos os valores PARES sorteados pela função anterior
'''


from random import randint



import random

def sorteia():
    numeros = []
    for _ in range(5):
        numeros.append(random.randint(1, 10))
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

