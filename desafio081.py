'''
Crie um porgrama que leia varios numeros e cocar em uma lista

Depois disso, mostre:
A) Quantos numeros foram digitados.
B) A lista de valores decrescente.
C) Se o valor 5 foi digitado e esta na lista
'''

lista = []

while True:
    valor = input('Digite um  numero ou [s para sair]: ').lower()
    if valor == 's':
        break
    if valor.isdigit():
        lista.append(valor)
    else:
        print(f'Invalido tente novamente.')

lista.sort(reverse=True)
print(lista)

