"""
Crei um programa que leia o nome completo de uma pessoa e mostre:
01 O nome com todas letras MAIÚSCULAS
02 O nome com todas letras minusculas
03 Quantas letras ao todo (sem considerar os espaços)
04 Quantas letras tem o primeiro nome
"""
nome = input('Diga seu nome completo: ')

print('='*20)
print(nome)
print('='*20)
print(nome.upper()) #1
print('='*20)
print(nome.lower()) #2
print('='*20)
print(len(nome))
print('='*20)
print(len(nome.replace(' ', ''))) #3
print('='*20)
listanomes = nome.split() #4
print(listanomes)
primeironome = listanomes[0] #4
numero_caracteresprimeiro = len(primeironome) #4
print(f'O primeiro nome tem {numero_caracteresprimeiro} caracteres.') #4
print('='*20)
