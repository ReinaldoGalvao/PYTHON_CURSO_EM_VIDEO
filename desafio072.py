'''
Crie um programa que tenha um tupla totalmente preenchida com uma contagem
por extenso, de zero ate vinte.

Seu programa deverá ler um numero pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

opcao =''
numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    if opcao == 'N':
        break
    while True:
        extenso = int(input('Digite um numero ente 0 e 20: '))
        if 0 <= extenso <= 20:
            break
        print('O numero tem de ser entre 0 e 20. ', end='')
    print(f'Voce digitou o numero {numero[extenso]}')
    opcao = input('Quer continuar [S/N]: ').strip().upper()
    if opcao != 'N' and opcao != 'S':
        opcao = input('Quer continuar [S/N]: ').strip().upper()
    if opcao == 'N':
        break
'''

cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        num = int(input('Digite um numero entre 0 e 20: '))
        if 0 <= num <=20:
            break
        print('Você esta digitando um numero abaixo de 0 ou maior que 20\nTente novamente!')
    
    print(f'Voce digitou o numero {cont[num]}')
    opcao = input('Quer continuar [S/N]: ').strip().upper()
    if opcao != 'S':
        break





