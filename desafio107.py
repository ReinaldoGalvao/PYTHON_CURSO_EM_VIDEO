'''
Crie um modulo chamado moeda.py que tenha as funçoes incorporadas aumentar(), diminuir(), dobra() e metade().
Faça também um programa que importe esse módulo e use alguma dessas funções.
'''
import moeda
numero1 = int(input('Diga um numero: '))
numero2 = int(input('Diga outro numero: '))
porcen = int(input(f'Diga quantos %: '))

print(f'A soma de {numero1} com {numero2} = {moeda.aumentar(numero1, numero2)}')
print(f'O dobro de {numero1} é {moeda.dobro(numero1)}\nO dobro de {numero2} é {moeda.dobro(numero2)}')
print(f'A metade de {numero1} é {moeda.metade(numero1)}\nA metade de {numero2} é {moeda.metade(numero2)}')
print(f'Aumentando {porcen}% de {numero1} é {moeda.porcentagem(numero1, porcen)}\nAumentando {porcen}% de {numero2} é {moeda.porcentagem(numero2, porcen)}')
print(f'Diminuindo {porcen}% de {numero1} é {moeda.porcentagemmenos(numero1, porcen)}\nDiminuindo {porcen}% de {numero2} é {moeda.porcentagemmenos(numero2, porcen)}')