'''
Faça um programa que leia nome e média de um aluno,
aguardadno também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
'''

ano_letivo ={}

ano_letivo['Nome'] = str(input('Nome: '))
ano_letivo['Média'] = int(input('Diga a média: '))

print(f"O nome é {ano_letivo['Nome']}")
print(f"A média é {ano_letivo['Média']}")
if ano_letivo['Média'] >= 5:
    print(f"O aluno {ano_letivo['Nome']} está aprovado.")
else:
    print(f"O aluno {ano_letivo['Nome']} está reprovado.")