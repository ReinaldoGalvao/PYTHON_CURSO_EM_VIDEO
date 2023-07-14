'''
Refaça o desafio 009, mostrando a tabuada de um numero que o usauario escolher
só que agora utilizando um laço for.
'''

n1 = int(input('Fale um numero: '))
print(f'===== A tabuada de {n1} =====')
for i in range(1, 11):
    print(f'{n1} x {i} = {n1*i}')