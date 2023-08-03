'''
Crie um programa que leia varios numeros inteiros pelo teclado
O programa só vai parar quando o usuario digitar o valor 999
que é a condição de parada
No final mostre quantos numeros foram digitados e qual foi a soma entre eles
desconsiderando o flag.
'''
soma = 0 
count = 0

while True:
    numero = int(input('Diga um número: '))
    if numero == 999:
        break
    soma += numero
    count += 1
print(f'Foram digitado {count} números.')
print(f'A soma dos {count} números é de {soma}.')