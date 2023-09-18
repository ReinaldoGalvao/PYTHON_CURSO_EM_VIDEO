'''
Crie um porgrama que leia varios numeros e cocar em uma lista

Depois disso, mostre:
A) Quantos numeros foram digitados.
B) A lista de valores decrescente.
C) Se o valor 5 foi digitado e esta na lista
'''

# Inicializa a lista vazia
lista = []

# Loop para ler os números
while True:
    valor = input('Digite um número ou [s para sair]: ').lower()
    if valor == 's':
        break
    if valor.isdigit():
        lista.append(int(valor))
    else:
        print(f'Inválido. Por favor, tente novamente.')

# A) Quantos números foram digitados
quantidade_numeros = len(lista)

# B) Lista de valores em ordem decrescente
lista.sort(reverse=True)

# C) Verifica se o valor 5 está na lista
valor_5_presente = 5 in lista

# Mostra os resultados
print(f'Foram digitados {quantidade_numeros} números.')
print(f'A lista em ordem decrescente é: {lista}.')
if 5 in lista:
    posicao_5 = lista.index(5)+1
    print(f'O numero 5 esta na posiçao {posicao_5}.')
if valor_5_presente:
    print(f'O valor 5 foi digitado e está na lista.')
else:
    print('O valor 5 não foi digitado ou não está na lista.')
