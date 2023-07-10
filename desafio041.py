"""
A confederação Nacional de natação prescisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria de acordo a sua idade:    
"""
from datetime import datetime

nome = input('Diga o nome do nadador que deseja saber qual categoria ele participa: ')
data_nasc = (input(f'Diga qual ano o {nome} nasceu: '))
while not data_nasc.isdigit() or len(data_nasc) != 4 or int(data_nasc) > datetime.now().year:
    data_nasc = input(f'Diga qual ano o {nome} nasceu,\n exemplo: 2004 \n Diga: ')

data_atu = datetime.now()
data_ano = data_atu.year
idade = int(data_ano) - int(data_nasc)
#print(idade)

if idade <= 9:
    print(f'{nome} está na categoria MIRIN.')
    
elif idade > 9 and idade <= 14:
    print(f'{nome} está na categoria INFANTIL.')
    
elif idade > 14 and idade <= 19:
    print(f'{nome} está na categoria JUNIOR.')
    
elif idade == 20:
    print(f'{nome} está na categoria SÊNIOR.')
    
else:
    print(f'{nome} está na categoria MASTER.')