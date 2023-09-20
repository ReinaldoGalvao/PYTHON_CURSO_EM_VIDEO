'''
Crei um programa onde o usuario possa digitar sete valores numericos
e cadastre-os em uma lista unica que mantenha separados os valores.
No final, mostre os valores pares e impares em ordem crescente.
'''
numeros = [[], []]
valor = 0
par = 0 #conta par
impar = 0 #conta impar
for v in range (1, 8):
    valor = int(input(f'Digite o {v}º valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
        par +=1 #aqui add no contador par
    else:
        numeros[1].append(valor)
        impar +=1 #aqui add no contador impar
print('-='*30) #para imprimir 2 lista 
print(f'Todos os valores: ', end='')

primeiro_elemento = True #aqui

for lista_dentro in numeros: #imprime 
    for item in lista_dentro: #sem
        if primeiro_elemento: #a virgula
            print(item, end='') #no 
            primeiro_elemento = False #final
        else:
            print(f', {item}', end='') ##
print()
print('-='*30)
print(f'Foram adicionados {par} números pares.')
print('-='*30)
numeros[0].sort()
print(f'Os valores pares foram ', ', '.join(map(str, numeros[0]))) #imprime os dados de uma lista fora da lista
print('-='*30)
print(f'Foram adicionados {impar} números impares.')
print('-='*30)
numeros[1].sort()
print(f'Os valores impares foram ', ', '.join(map(str, numeros[1]))) #imprime os dados de uma lista fora da lista
print('-='*30)