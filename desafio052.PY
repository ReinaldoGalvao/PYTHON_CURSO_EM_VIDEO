'''
Faça um programa que leia um número inteiro 
e diga se ele é ou não um número primo
'''

n = int(input('Diga um número: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{} '.format(c), end=' ')

print('\n\033[mO número \033[31m{}\033[m foi divisível \033[31m{}\033[m vezes'.format(n, tot))
if tot == 2:
    print('E por isso ele é \033[32mPRIMO\033[m!')
else:
    print('E por isso ele \033[31mNÃO\033[m é \033[31mPRIMO\033[m!')