'''
Exercício Python 56:
Desenvolva um programa que leia 
o nome, idade e sexo de 4 pessoas
No final do programa mostre:
a média de idade do grupo
qual é o nome do homem mais velho
quantas mulheres têm menos de 20 anos.
'''
nome = ''
idade = 0
sexo = ''
total_masculino = 0
total_feminino = 0
soma_idade = 0
nome_Mvelho = ''
nome_Mvelhoh = ''
idadeveriveio = 0
idadeveriveioh = 0
def contem_apenas_letras(texto):
    return texto.isalpha()

def contem_apenas_numeros(texto):
    return texto.isnumeric()

for i in range(1, 5):
    nome = input('Diga o nome da {0}° pessoa: '.format(i))
    while not contem_apenas_letras(nome):
        print('Nome inválido. Digite apenas letras, sem números ou caracteres especiais.')
        nome = input('Diga o nome da {0}° pessoa: '.format(i))

    idade_str = input('Diga a idadade da {0}° pessoa: '.format(i))
    while not contem_apenas_numeros(idade_str):
        print('idade inválida. Digite apenas numeros, sem letras ou caracteres especiais.')
        idade_str = input('Diga a idade da {0}° pessoa: '.format(i))
        
    idade = int(idade_str)
    
    sexo = input('Diga o sexo da {0}° pessoa: '.format(i)).strip().upper()
    while sexo not in ('M', 'F'):
        print('Sexo invalido!')
        sexo = input('Diga o sexo da {0}° pessoa: '.format(i)).strip().upper()
    
    soma_idade += idade
    if sexo == 'F':
        total_feminino += 1
        if idadeveriveio < idade:
            idadeveriveio = idade
            nome_Mvelho = nome
    else:
        total_masculino += 1
        if idadeveriveioh < idade:
            idadeveriveioh = idade
            nome_Mvelhoh = nome

media_idade = soma_idade / 4

print(f'Total de pessoas do sexo masculino: {total_masculino}')
print(f'Total de pessoas do sexo feminino: {total_feminino}')
print(f'Média de idades: {media_idade:.2f}')
print(f'A mulher mais velha do grupo : {nome_Mvelho} com a idade de {idadeveriveio} anos.')
print(f'A mulher mais velha do grupo : {nome_Mvelhoh} com a idade de {idadeveriveioh} anos.')
