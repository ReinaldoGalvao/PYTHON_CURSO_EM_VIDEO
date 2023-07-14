'''
Faça um programa a soma entre todos os números ímpares que são multiplos de 3
e que se encontram no intervalo de 1 até 500.
'''

for c in range(1, 501):
    if c % 11 == 0:
        print(c)