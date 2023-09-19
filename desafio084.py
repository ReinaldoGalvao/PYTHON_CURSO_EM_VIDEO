'''
FAÇA UM PROGRAMA QUE LEIA NOME E PESO DE VARIAS PESSOAS, GUARDANDO TUDO EM UMA LISTA
NO FINAL MOSTRE:

A) QUANTAS PESSOAS FORAM CADASTRADAS.
B) UMA LISTAGEM COM AS PESSOAS MAIS PESADAS.
C) UMA LISTAGEM COM AS PESSOAS MAIS LEVES.

'''

temp = []
princ = []
maior = 0
menor = 0
while True:
    temp.append(str(input('Qual o nome: ')))
    temp.append(float(input(f'Qual o peso: ')))
    if len(princ) == 0:
        maior = temp[1]
        menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = input('Deseja continuar? [S/N]')
    if resp in 'Nn':
        break
print('-='*30)
print(f'Ao todo você cadastrou {len(princ)} pessoas.')
print(f'O maior pesso foi de {maior}Kg. Peso de ' , end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O maior pesso foi de {menor}Kg. Peso de ' , end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
