'''
Escreva um prorama que leia 2 numeros inteiros e compare-os, mostrando na tela um mensagem:
O primeiro valor é maior
O segundo valor é maior
Não existe valor maior, os dois são iguais
''' 
numeros = []
for i in range(2):
    nun = int(input('Fale um numero: '))
    numeros.append(nun)
    
if numeros[0] > numeros[1]:
    print(f'O numero {numeros[0]} é maior que o numero {numeros[1]}.')

elif numeros[0] < numeros[1]:
    print(f'O numero {numeros[1]} é maior que o numero {numeros[0]}.')

elif numeros[0] == numeros[1]:
    print(f'Os numeros são iguais.')