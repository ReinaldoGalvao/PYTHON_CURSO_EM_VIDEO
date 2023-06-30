#faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor.

n1 = int(input('Fale um numero: '))
nmais = n1 + 1
nmenos = n1 - 1
print(f'O numero dito foi {n1} e seu sucessor é {nmais} e seu antecessor é {nmenos}.')

#exemplo

n2 = int(input('Fale um numero: '))
print(f'O numero dito foi {n2} e seu sucessor é {n2+1:.2f} e seu antecessor é {n2-1:.2f}.')
print(f'{n2-1:.2f}')