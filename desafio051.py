'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa pregressão
'''
print('=================================')
print('=      10 TERMOS DE UMA PA      =')
print('=================================')
primeiro = int(input('Diga o primeiro termo: '))
razao = int(input('Diga a razão: '))
decimo_termo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo_termo + razao, razao):
    if c % 2 == 0:
        print('{}'.format(c), end='-> ')
    elif c % 2 != 0:
        print('{}'.format(c), end='-> ')
print('ACABOU')