'''
Faça um programa que tenha uma função chamada maior(), que
receba varios parametros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior
'''


from time import sleep

def maior(* numeros):
    cont = maior = 0
    sleep(0.5)
    print('Analisando os valores passados...')
    for valor in numeros:
        print(f'{valor} ', end='')
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if maior < valor:
                maior = valor
        cont += 1
    print()
    sleep(0.5)
    print('=='*25)
    sleep(0.5)
    print(f'Foram informados {cont} valores ao todo')
    sleep(0.5)
    print(f'O maior valor informando foi {maior}')
    sleep(0.5)
    print('=='*25)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

