'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final mostre:

A - Quantas vezes apareceu o valor 9
B - Em que posição foi digitado o primeiro valor 3
C - Quais foram os nimeros pares
'''
cont = 0
num =  (int(input('Digite um numero: ')),
        int(input('Digite outro numero: ')),
        int(input('Digite mais um numero: ')),
        int(input('Digite o ultimo numero: ')))
print(f'Voce digotou os numeros {" ".join(map(str, num))}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
par = []
impar = []
if 3 in num:
    print(f'o primeiro numero 3 apareceu na {num.index(3)+1}ª posição')
else:
    print(f'O valor 3 nao foi digitado em nunhuma posição.')
for n in num:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(f'O numeros pares digitados foram {" ".join(map(str, par))}')
print(f'Os numeros impares digitados foram {" ".join(map(str, impar))}')
