'''
Crie um pacote chamado utilidadesCeV que tenha dois modulos internos chamados moeda e dado.
Transfira todas as funções utilizados nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
'''

from utilidadescev import moeda

p = float(input('Diga um valor R$: '))
moeda.resumo(p, 20, 12)

