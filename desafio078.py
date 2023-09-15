'''
Faça um programa que leia 5 valores numericos e guarde em uma lista.
No final, mostre qual foi o maior e o menor valor digtado e suas respectivas posições na lista.
'''

valores = []
for v in range(0, 5):
    valores.append(int(input(f'Digite um valor: ')))
    
    
print(valores)
print(f'O maior valor da lista é {max(valores)}')
print(f'O maior valor da lista aparece na posiçaõ {valores.index(max(valores))}')
print(f'O menor valor da lista é {min(valores)}')
print(f'O maior valor da lista aparece na posiçaõ {valores.index(min(valores))}')