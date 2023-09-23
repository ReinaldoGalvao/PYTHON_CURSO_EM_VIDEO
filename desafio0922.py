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

def calcular_anos_para_aposentar(dados):
    if dados['Anos_aposentar'] > ano_atual:
        print(f'O {dados["Nome"]} irá se aposentar em {dados["Anos_aposentar"]} e faltam {dados["Anos_aposentar"] - ano_atual} anos')
    else:
        print(f'O {dados["Nome"]} já se aposentou em {dados["Anos_aposentar"]}')
#print(ano_atual)
dados = {}

dados['Nome'] = str(input('Nome: '))
dados['Ano_nasc'] = int(input('Ano de nascimento [ex 1980]: '))
dados['CTPS'] = str(input('Carteira de trabalho: '))
dados['Idade'] = ano_atual - dados["Ano_nasc"]
if dados['CTPS'] != '':
    dados['Ano_contrat'] = int(input('Ano de contratação [ex 1995]: '))
    dados['Salario'] = float(input('Salario: '))
dados['Anos_aposentar'] = dados['Ano_contrat'] + 35
print(f'O {dados["Nome"]} tem {dados["Idade"]} anos')
calcular_anos_para_aposentar(dados) #chamei a função

#print(dados)