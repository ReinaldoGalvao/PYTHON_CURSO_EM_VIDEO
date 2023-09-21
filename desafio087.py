'''
Crie um programa que crie uma matriz de dimensao 3x3 e preencha com valores lidos pelo teclado
no final, mostre a matriz na tela, com a formatação correta

Aprimore esse desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.

B)A soma dos valores da terceira coluna.

C)O maior valor da segunda linha.
'''
"""colun = 1
linhas = 1
terceiracolun = []
segunda_linha = []
par = []
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            par.append(matriz[linha][coluna])
        if linhas == 2:
            segunda_linha.append(matriz[linha][coluna])
            linhas = 0
        
        if colun == 3:
            terceiracolun.append(matriz[linha][coluna])
            colun = 0
        colun += 1
        linhas += 1



print('-='*15)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha] [coluna]:^5}]', end='')
    print()
    
    
print('-='*15)
print(par)
soma = sum(par)
print(f'A soma dos números pares é: {soma}')
somarcoluna = sum(terceiracolun)
print(f'A soma dos números da terceira coluna é {somarcoluna}')

print(f'O maior valor da segunda linha é {max(segunda_linha)}')"""

matriz =  [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0 , 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-='*15)
print(f'A soma dos pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]

print(f'A soma da terceira coluna é {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]

print(f'O maior da segunda linha é {mai}')
print('-='*15)
