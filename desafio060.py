'''
Faça um programa que leia um numero
e diga o fatorial dele
'''

'''from math import factorial

n = int(input('Digite um numero: '))
f = factorial(n)

print('O factorial de {} é {}.'.format(n, f))'''


numero = int(input('Diga um numero: '))

resultado=1
count=1

while count <= numero:
    resultado *= count
    count += 1

print(resultado)