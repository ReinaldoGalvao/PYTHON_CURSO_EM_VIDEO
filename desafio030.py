'''
Crie um programa que leia um numero inteiro e mostre na tela se é PAR ou IMPAR.
'''

n = int(input('Diga um numero: '))

"""if (n + n)/2 % 2:
     print('Impar')
else:
    print('Par')"""
    
resultado = n % 2
if resultado == 0:
    print(f'O numero {n} é par.')
else:
    print(f'O numero {n} é impar.')
