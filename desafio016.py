"""
Crie um programa que leia um numero Real qualquer pelo teclado
e mostre na tela sua porcao inteira
ex: 6.127 = 6
"""
import math
numero =  float(input('Diga um numero: '))
numero_inteiro = math.floor(numero)
print(f'O numero {numero} tem a parte inteira {numero_inteiro}.')