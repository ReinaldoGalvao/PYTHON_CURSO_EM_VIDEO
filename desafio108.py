'''
Adapite o codigo do desafio 107, criando uma função adicional chamado moeda() que
consiga mostrar os valores como um valor monetário formatado.
'''

 
import moeda
p = int(input('Diga um numero: '))
porcen = int(input(f'Diga quantos %: '))

print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando {porcen}% temos {moeda.moeda(moeda.porcentagem(p))}')
print(f'Diminuindo {porcen}% temos {moeda.moeda(moeda.porcentagemmenos(p))}')