'''
Faça um programa que tenha uma função chamada Area(), que receba as
dimensões da um terrono retangular (largura e comprimento) e mostre a area do terrono
'''
def area (l, c):
    a = l * c
    print(f'A area de um terreno {l:.2f} x {c:.2f} é de {a}m°')

print('Controle de Terrenos')
print('-' *20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))

area(l, c)