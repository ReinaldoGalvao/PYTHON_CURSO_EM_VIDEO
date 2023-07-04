#Faça um programa que leia 3 numeros e mostre qual é o numero maior e qual é o menor.

n1 = int(input('Diga um numero: '))
n2 = int(input('Diga outro numero: '))
n3 = int(input('Diga outro numero: '))

if n3 > n2 and n1 < n3:
    #print(f'O numero maior é {n3}')
    maior = n3

if n3 < n2 and n1 < n2:
    #print(f'O numero maior é {n2}')
    maior = n2
    
if n1 > n2 and n3 < n1:
    #print(f'O numero maior é {n1}')
    maior = n1
    
#####
#####

if n3 < n2 and n3 < n1:
    #print(f'O numero menor é {n3}')
    menor = n3
    
if n2 < n1 and n2 < n3:
    #print(f'O numero menor é {n2}')
    menor = n2
    
if n1 < n2 and n1 < n3:
    #print(f'O numero menor é {n1}')
    menor = n1
print(f'O maior dos numeros é o {maior} e o menor é o {menor}.')