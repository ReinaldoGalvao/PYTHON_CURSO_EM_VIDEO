'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler:
Nome
Partida
Gols por partida
No final, tudo isso será guardado em um dicionario, incluindo o total de gols
feito no campeonato.
'''

campeonato = {}
partidas = []

campeonato['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Partidas jogadas pelo {campeonato["nome"]}: '))
for i in range(1, tot +1):
    partidas.append(int(input(f'Quantos gols na {i}ª partida: ')))
campeonato['gols'] = partidas[:]
campeonato['total'] = sum(partidas)
print('-=' * 30)
print(campeonato)
print('-=' * 30)
for k, v in campeonato.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' *30)
media_gol = campeonato['total'] / len(partidas)
print(f'O jogador {campeonato["nome"]} jogou {len(campeonato["gols"])} partidas. \nE ficou com a média de {media_gol:.2f} gols por partidas.')
for i, v in enumerate(campeonato['gols']):
    print(f'Na partida {i + 1}, fez {v} gols')
print(f'Foi um total de {campeonato["total"]} gols')
