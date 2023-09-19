'''
Crie um porgrama que leia varios numeros e cocar em uma lista

Depois disso, mostre:
A) Quantos numeros foram digitados.
B) A lista de valores decrescente.
C) Se o valor 5 foi digitado e esta na lista
'''
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]')).lower()
    if resp == 'n':
        break
print('-='*30)
print(f'Você digitou {len(valores)} numeros.')
valores.sort(reverse=True)
print(f"Os valores em orde decrescente são {valores}")
if 5 in valores:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não foi encontrado na lista!")