'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa pregressão
'''

numero = int(input('Diga um número: '))
razao = int(input('Diga a razão: '))
x = int(input('Diga qunatas vezes: '))

for c in range(numero, x, razao):
    print (c)