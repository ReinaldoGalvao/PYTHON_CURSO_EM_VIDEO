"""
faça um programa de random para nomes de alunos sorteados
"""
import random
aluno1 = input('Fale o nome do primeiro aluno: ')
aluno2 = input('Fale o nome do segundo aluno: ')
aluno3 = input('Fale o nome do terceiro aluno: ')
aluno4 = input('Fale o nome do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print(f'A ordem de apresentação será: ')
print(lista)