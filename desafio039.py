from datetime import datetime

'''
Faça um programa que leia o ano de nascimento de um jovem e informa de acordo com a sua idade:

Se ela ainda va se alistar ao serviço militar.
se é hora de se alistar
se ja passou do tempo do alistamento

seu programa tambem devera mostrar o tempo que falta ou passou do prazo.

'''

data_nasc = int(input('Diga qual o ano que voce nasceu: '))
data_atu = datetime.now()
data_ano = data_atu.year
print(data_atu)
print(data_ano)
data_mat = data_ano - data_nasc
print(data_mat)
if data_mat <= 16:
    print(f'Você é muito novo ainda para se alistar. Faltan {(18 - data_mat)} anos para isso servir')

elif data_mat == 17:
    print(f'Você já esta pronto para se alistar. Falta {(17 - data_mat)} ano para se alistar e {(18 - data_mat)} anos para isso servir')
    
elif data_mat == 18:
    print(f'Você esta atrazado para se alistar. éra para você esta servindo.')
    
elif data_mat > 18:
    print(f'Você já passou do tempo de se alistar em {(data_mat - 17)} ano e em {(data_mat - 18)} anos para isso servir')

