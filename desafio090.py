'''
Faça um programa que leia nome e média de um aluno,
aguardadno também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
'''

ano_letivo ={}

ano_letivo['Nome'] = str(input('Nome: '))
ano_letivo['Média'] = float(input(f'Diga a média do aluno {ano_letivo["Nome"]}: '))

print(f"O nome é {ano_letivo['Nome']}")
print(f"A média é {ano_letivo['Média']}")
"""if ano_letivo['Média'] >= 7:
    print(f"O aluno {ano_letivo['Nome']} está aprovado.")
elif ano_letivo['Média'] >= 5 and ano_letivo['Média'] <= 6.9:
    print(f"O aluno {ano_letivo['Nome']} está de recuperação.")
else:
    print(f"O aluno {ano_letivo['Nome']} está reprovado.")  """
    
if ano_letivo['Média'] >= 7:
    ano_letivo['Situação'] = 'Aprovado'
elif 5 <= ano_letivo['Média'] < 7:
    ano_letivo['Situação'] = 'Recuperação'
else:
    ano_letivo['Situação'] =  'Reprovado'
    
print('x-'*30)

for k, v in ano_letivo.items():
    print(f' - {k} é igual a {v}')
    
