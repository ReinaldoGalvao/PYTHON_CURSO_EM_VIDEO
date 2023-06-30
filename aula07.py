"""
nome = str(input('Qual seu nome? '))

print('Prazer em te conhecer {:=^20}'.format(nome))

"""

n1 =int(input('Diga um numero: '))
n2 = int(input('Diga outro numero: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
dfloat = round(d, 2)
di = n1 // n2
e = n1 ** n2

print(f'A soma é {s}, o produto é {m}, a divisão é {dfloat}',end=' ')
print(f'Divisão inteira {di} e potência {e}')