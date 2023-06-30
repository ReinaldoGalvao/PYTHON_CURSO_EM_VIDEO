#faça um programa que leia um numero inteiro e mostre na tela sua tabuada

n1 = int(input('Fale um numero: '))
print(f'===== A tabuada de {n1} =====')
for i in range(1, 11):
    print(f'{n1} x {i} = {n1*i}')