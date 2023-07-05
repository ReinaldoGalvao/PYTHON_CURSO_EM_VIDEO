'''
Escreva um programa para aprovar o impréstimo bancário para a compra
de uma casa. O programa vai perguntar o valor da casa, o salario do comprador
e em quantos anos ele vai pagar.

calcule o valor da prestaçao mensal sabendo que ela não pode exceder 30% do
salario ou então o empréstimo será negado.

'''

valor_casa = int(input('Diga qual é o valor da casa: '))
salario = int(input('Diga o seu salário: '))
anos = int(input('Diga em quantos anos que pagar a casa: '))

parcelas_mes = anos * 12 #qts meses
parcelas = valor_casa / parcelas_mes #valor por mes
maximo = (salario * 30) /100 #30% do salario

if parcelas <= maximo:
    print(f' \n ============= \n O emprestimo de R${valor_casa:.2f} esta LIBERADO \n ============= \n Serão {parcelas_mes}x de R${parcelas:.2f} \n ============= \n ')
else:
    print(f' \n ============= \n NÃO LIBERADO \n ============= \n As prestações será de R${parcelas:.2f} e elas ultrapassarão o limite maximo que é de 30% do seu \nsalário que hoje é de R${maximo:.2f}')
    
#print(maximo)
#print(parcelas)