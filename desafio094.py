'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade do grupo
C) Uma lista com todas as mulheres
D) Uma lista com todas as pessoas com idade acima da média.
'''


dados = {}

while True:
    dados['nome'] = input('Nome: ')
    dados['sexo'] = input('Sexo [M/F]: ').upper()
    while dados['sexo'] not in ['M', 'F']:
        dados['sexo'] = input('Incorreto - Sexo [M/F]: ').upper()
    dados['idade'] = input('Idade: ')
    while True:
        resp = input('Deseja continuar? [S/N]:').upper()
        if resp == 'S':
            break
        elif resp == 'N':
            break
        elif resp != 'S' and resp != 'N':
            continue
    if resp == 'S':
        continue
    if resp == 'N':
        break

print(dados)