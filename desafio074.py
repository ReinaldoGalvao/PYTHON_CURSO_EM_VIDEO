'''
Sortei 5 numeros e me diga o maior e monor sorteado
'''

from random import randint

numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Eu sorteei o valor {numeros}')
print('Os valores sorteados foram: ', end ='')
for n in numeros:
    print(f'{n} ', end='')
print(f'O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')