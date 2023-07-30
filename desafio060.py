'''
Faça um programa que leia um numero
e diga o fatorial dele
'''

numero = int(input('Diga um numero: '))

resultado=1
count=1

while count <= numero:
    resultado *= count
    count += 1

print(resultado)