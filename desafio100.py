'''
Faça um programa que tenha uma lista chamada numeros e duas funçoes
chamadas sorteia() e somaPar().A primeira função vai sortear 5 numeros
e vai coloca-los dentro da lista e a segunda função vai mostrar a soma 
entre todos os valores PARES sorteados pela função anterior
'''
from random import randint

def somaPar(numeros):
    if numeros % 2 == 0:
        print(f'O {numeros} é par.')


def sorteia(* numeros):
    for i in range(1, 5):
        num = randint(1, 6)
        somaPar()
    print(f'Os numeros sorteados foram {num}')
    
sorteia()