'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre=os (com idade) em um dicionário se por acaso a CTPS for diferente a ZERO
o dicionario receberá tambem o ano de contratação e o salário. Calcule e acrescente,
alen da idade, com quantos anos a pessoa vai se aposentar.
'''

dados = {}

dados['Nome'] = str(input('Nome: '))
dados['ano_nas'] = int(input('Ano de Nascimento: ex 1955'))
dados['CTPS'] = int(input('Carteira de Trabalho: '))
if dados['CTPS'] != '':
    dados['ano_contrat'] = int(input('Ano de contratação: ex 1980'))

