'''
Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
Para salarios superiores a R$1.250,00 calcule em aumento de 10%.
Para salarios inferiores ou iguais, o aumento é de 15%.
'''

salario = float(input('Diga qual é o seu salario: '))

if salario <= 1250:
    salariomenor = (salario * 15 ) /100 + salario
    print(f'O seu salario é inferior a R$1250,00\n E por isso teve um aumento de 15% e agora seu salario é {salariomenor} .')
    
if salario > 1250:
    salariomaior = (salario * 10 )/100 + salario
    print(f'O seu salario é maior a R$1250,00\n E por isso teve um aumento de 10% e agora seu salario é {salariomaior} .')