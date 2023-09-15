'''
Crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista
Caso o numero ja exista la dentro ele nao será adicionado
no final sera exibidos, em ordem crescente
'''

'''valores = []

for v in range(5):
    if v in valores:
        valores.pop()
    
    valores.append(int(input('Diga um numero: ')))
    
print(valores)

'''

valores = []

while True:
    valor = input("Digite um valor numérico (ou 's' para sair): ").lower()

    if valor == 's':
        break

    if valor.isdigit():
        valor = int(valor)
        if valor not in valores:
            valores.append(valor)
        else:
            print(f"O valor {valor} já está na lista.")
    else:
        print("Por favor, digite um valor numérico válido.")

valores.sort()

print("Valores em ordem crescente:")
for valor in valores:
    print(valor)

