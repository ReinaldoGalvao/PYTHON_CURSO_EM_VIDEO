'''
Desenvolva uma logica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
Abaixo de 18.5: Abaixo do peso
Entre 18.5 e 25: Peso ideal
Entre 25.1 até 30: Sobre peso
Entre 30.1 até 40: Obesidade
Acima de 40: Obesidade móbida
'''

peso = float(input('Diga seu peso: '))
altura = float(input('Diga sua altura: '))

imc = peso / (altura**2)

print(f'{imc:.2f}')

if imc < 18.5:
    print(f'O seu IMC é de {imc:.2f} e você está abaixo do peso.')

if imc > 18.5 and imc <= 25:
    print(f'O seu IMC é de {imc:.2f} e você está no imc ideal.')

if imc >= 25.1 and imc <= 30:
    print(f'O seu IMC é de {imc:.2f} e você está com sobre imc.')
    
if imc >= 30.1 and imc <= 40:
    print(f'O seu IMC é de {imc:.2f} e você está com Obesidade.')
    
if imc >= 40.1:
    print(f'O seu IMC é de {imc:.2f} e você está com Obesidade mórbida.')