'''
Faça um programa que tenha uma função chamada ficha()
que receba 2 parametros opcionais: nome de um jogador e quantos gols ele marcou.

o programa deverá ser capaz de mostrar a FICHA DO JOGADOR, mesmo que algum dado não
tenha sido informando corretamente.
'''
'''def jogo(jogador, gols):
    if jogador == '' and gols == '':
        print('O jogador <desconhecido> fez 0 gol(s) no campeonato.')
    elif jogador != '' and gols == '':
        print(f'O jogador {jogador} fez 0 gol(s) no campeonato.')
    elif jogador == '' and gols != '':
        print(f'O jogador <desconhecido> fez {gols} gol(s) no campeonato.')
    elif jogador != '' and gols != '':
        print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')
        

jogador = str(input('Nome do jogador: '))
gols = str(input('Numeros de gols: '))

jogo(jogador, gols)
'''


def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')
    
    

n = str(input('Nome do jogador: '))
g = str(input('Numeros de gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0
    
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
    

