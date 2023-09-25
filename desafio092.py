'''
Crie um programa que leia:
Nome, Ano de nascimento, Carteira de trabalho 
Usando a idade cadastre-os
Se por acaso a CTPS for diferente a ZERO o dicionário receberá também:
Ano da contratação e salário
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar
'''
import datetime

ano_atual = datetime.date.today().year

def puxar_contrat(dados):
    if dados['CTPS'] != '0':
        print(f'{dados["Ano_contrat"]} foi o ano do contrato')
        print(f'O salário é de {dados["Salario"]}')

def calcular_anos_para_aposentar(dados):
    if dados['Anos_aposentar'] > ano_atual:
        print(f'O {dados["Nome"]} irá se aposentar em {dados["Anos_aposentar"]} e faltam {dados["Anos_aposentar"] - ano_atual} anos. E terá {idade_aposentar} anos.')
    else:
        print(f'O {dados["Nome"]} já se aposentou em {dados["Anos_aposentar"]}')

def puxar_CTPS(dados):
    if dados['CTPS'] != '0':
        dados['Ano_contrat'] = int(input('Ano de contratação [ex 1995]: '))
        dados['Salario'] = float(input('Salario: '))

#print(ano_atual)
dados = {}

dados['Nome'] = str(input('Nome: '))
dados['Ano_nasc'] = int(input('Ano de nascimento [ex 1980]: '))
dados['CTPS'] = str(input('Carteira de trabalho: '))
dados['Idade'] = ano_atual - dados["Ano_nasc"]

puxar_CTPS(dados) #chamei a função
if dados['CTPS'] != '0':
    dados['Anos_aposentar'] = dados['Ano_contrat'] + 35
    idade_aposentar = dados["Anos_aposentar"] - ano_atual + dados["Idade"]
print(f'O {dados["Nome"]} tem {dados["Idade"]} anos')
puxar_contrat(dados) #chamei a função
if dados['CTPS'] != '0':
    calcular_anos_para_aposentar(dados) #chamei a função

#print(dados)
