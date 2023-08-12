'''
Crie uma tupla preenchida cm os 20 primeiros colocados da tabela do Brasileirao
na ordem de colocação.Depois mostre:
A) Apenas os 5 primeiros times melhor colocados.
B) Os ultimos 4 piores colocados
C) Uma lista com os times em ordem alfabeticas
D) Em que posição na tabela o Flamengo está
'''

brasileirao= ('Botafogo', 'Flamengo', 'Fluminense', 'Palmeiras', 'Bragantino', 'Grêmio', 'Athletico-PR', 'Cuiabá', 'São Paulo', 'Atlético-MG', 'Cruzeiro', 'Internacional', 'Fortaleza', 'Corinthians', 'Goiás', 'Bahia', 'Santos', 'Coritiba', 'Vasco', 'America-MG')

print(f'Os 5 primeiros times são {brasileirao[:5]}\n1º {brasileirao[0]}\n2º {brasileirao[1]}\n3º {brasileirao[2]}\n4º {brasileirao[3]}\n5º {brasileirao[4]}')
print('===================================================')
print(f'Os 4 ultimos da tabela são {brasileirao[16:]}\n17º {brasileirao[16]}\n18º {brasileirao[17]}\n19º {brasileirao[18]}\n20º {brasileirao[19]}')
print('===================================================')
print(sorted(brasileirao))
print(f'Os times em ordem alfabeticas são: \n{sorted(brasileirao[0:])}')
