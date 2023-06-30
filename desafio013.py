#faça um algoritmo que leia o seu salario e mostre seu novo salario com o % tambem setado por voce

salario = float(input('Diga qual seu salario atual: '))
porcentagem = float(input('Diga quantos porcento seu salario ira almentar: '))

porcentagem_calculo = porcentagem / 100
salario_final = salario + (salario * porcentagem_calculo)

print(f'Após o aumento seu salario que antes era de {salario} com o aumento é de {salario_final}.')