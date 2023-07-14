'''
Crie um programa que mostre na tela todos os numeros pares que estão
no intervalo entre 1 e 50
'''

for c in range(1, 51):
    par = c % 2
    if par == 0:
        print(c)