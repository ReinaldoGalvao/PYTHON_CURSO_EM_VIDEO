'''
Crei um programa que leia o ano de nascimento de 7 pessoas
No final mostre quantas pessoas ainda não atingiram a maior idade 
e quantas já são maiores.
'''
from datetime import datetime
data_atu = datetime.now()
print(data_atu)
data_ano = data_atu.year

# Definir a idade mínima para ser considerado maior de idade
IDADE_MINIMA_MAIOR_IDADE = 21

# Inicializar contadores
menores_de_idade = 0
maiores_de_idade = 0

# Loop para ler o ano de nascimento das 7 pessoas
for i in range(1, 8):
    ano_nascimento = int(input(f"Digite o ano de nascimento da {i}ª pessoa: "))
    
    # Calcular a idade da pessoa
    idade = (data_ano - ano_nascimento)
    
    # Verificar se a pessoa é menor ou maior de idade
    if idade < IDADE_MINIMA_MAIOR_IDADE:
        menores_de_idade += 1
    else:
        maiores_de_idade += 1

# Mostrar o resultado
print(f"Pessoas menores de idade: {menores_de_idade}")
print(f"Pessoas maiores de idade: {maiores_de_idade}")