'''
Faça um programa que leia seis numeros inteiros e mostre a soma apenas daquelas que forem pares.
Se o valor digitado for impar, desconsidere-o
'''

soma = 0

for _ in range(6):
    numero = int(input("Digite um número inteiro: "))
    
    if numero % 2 == 0:
        soma += numero

print("A soma dos números pares é:", soma)