'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade do grupo
C) Uma lista com todas as mulheres
D) Uma lista com todas as pessoas com idade acima da média.
'''

galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('INVALIDO! Digite M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('INVALIDO - Responda S ou N')
    if resp == 'N':
        break
print('-=' *30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
print('-=' *30)
media = soma / len(galera)
print(f'A média de idade é {media:5.2f} anos')
print('-=' *30)
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ')
        
print('Lista de pessoas com a idade acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')