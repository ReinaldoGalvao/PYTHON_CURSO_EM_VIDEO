'''
Refaça o DESAFIO 051, lendo o primeiro termo e a razao 
de uma PA, mostrando os 10 primeiros termos da progressao 
usando a estrutura whlie
'''

print('===========================')
print('=      GERADOR DE PA      =')
print('===========================')
primeiro = int(input('Diga o primeiro termo: '))
razao = int(input('Diga a razão: '))
termo = primeiro
count = 1

while count <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    count += 1
print('FIM')