'''
Crie um porgrama que leia varios numeros e coleque em uma lista
Despois disso, crie duas listas extras que vão conter apenas os valores
pares e outra só para os impares digitaddos

Ao final, mostre o conteudo das tres listas geradas

'''
cont = 0
numeros = []
par = []
impar = []
if cont == 0:
    num = input("Diga um numero: ")
while True:
    if num.notisnumeric():
        print('a')
    if num.isnumeric():
        num = int(num)
        cont += 1
        numeros.append(num)
        if num % 2 == 0:
            par.append(num)
        if num % 2 == 1:
            impar.append(num)
    resp = input("Quer continuar? [S/N]")
    if resp in 'Nn':
        break
    if cont >= 1 :
        num = input("Diga um numero: ")
    else:
        print("Errou")
        continue

'''
print(numeros)
if par[0] == ' ':
    print('Não foi digitado numeros pares.')

if par[0] != ' ':
    print(par)

if impar[0] == ' ':
    print('Não foi digitado numeros impares.')

if impar[0] != ' ':
    print(impar)

print(impar)



'''