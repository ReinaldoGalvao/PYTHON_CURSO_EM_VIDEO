'''
crie um programa que leia varios numeros inteiros pelo teclado.
O programa só vai parar quando o usuario digitar 999
no final qunatos numeros foram digitados e qual foi a soma entre eles.
'''

numero = 0
qts = 0
soma = 0
while True:
    if numero == 999:
        print('FIM')
        break
    while True:
        numero = int(input('Diga um numero: '))
        if numero == 999:
            break
        if numero != 999:
            qts += 1
            soma = soma + numero
print(f'Foram digitados {qts} numeros')
print(f'a soma dos numeros é {soma}')