'''
Crie um programa que leia 2 numeros e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] novos números
[4] sair do programa

seu programa deverá realizar a operação
solicitada em cada caso
'''
"""numero1 = 0
numero2 = 0
resposta =''
while resposta in '1234':
    numero1 = int(input('Diga um número: '))
    numero2 = int(input('Diga outro número: '))
    print('============================')
    print('============MENU============')
    print('============================')
    resposta = input('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa\n    Escolha um das opções acima: ''')
    if resposta == '1':
        print(f'    A soma de {numero1} + {numero2} = {numero1 + numero2}')
    if resposta == '2':
        print(f'    A multiplicação de {numero1} x {numero2} = {numero1 * numero2}')
    if resposta == '3':
        if numero1 > numero2:
            print(f'    O número {numero1} é o maior entre os dois numeros.')
        else:
            print(f'    O número {numero2} é o maior entre os dois numeros.')
    if resposta == '4':
        continue
    if resposta == '5':
        break"""
        
numero1 = 0
numero2 = 0
resposta =''
while True:
    if resposta == '5':
        break
    numero1 = int(input('Diga um número: '))
    numero2 = int(input('Diga outro número: '))
    while True:
        print('\033[;7m============================\033[m')
        print('\033[;7m============MENU============\033[m')
        print('\033[;7m============================\033[m')
        resposta = input('''        [\033[1;31m1\033[m] somar
        [\033[1;31m2\033[m] multiplicar
        [\033[1;31m3\033[m] maior
        [\033[1;31m4\033[m] novos números
        [\033[1;31m5\033[m] sair do programa\n        Escolha um das opções acima: '''.replace(' ', ''))
        if resposta == '1':
            print(f'\nA soma de {numero1} + {numero2} = {numero1 + numero2}\n')
        if resposta == '2':
            print(f'\nA multiplicação de {numero1} x {numero2} = {numero1 * numero2}\n')
        if resposta == '3':
            if numero1 > numero2:
                print(f'\nO número {numero1} é o maior entre os dois numeros.\n')
            else:
                print(f'\nO número {numero2} é o maior entre os dois numeros.\n')
        if resposta == '4':
            break
        if resposta == '5':
            break