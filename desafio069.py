'''
Crie um programa que leia a idade e o sexo de várias  pessoas.
A cada pessoa cadastrada o programa deverá perguntar se o 
usuário quer ou nao continuar. No final mostre:

(A) Quantas pessoas tem mais de 18 anos.
(B) Quantos homens foram cadastrados.
(C) Quantas mulheres tem menos de 20 anos
'''

homens = 0
mulher20 = 0
todos18 = 0
vez = 0
while True:
    vez += 1
    sexo = input(f'Qual sexo da {vez}° pessoa? [M/F]: ').strip().upper()
    while sexo != 'F' and sexo != 'M':
        sexo = input(f'Qual sexo da {vez}° pessoa? [M/F]: ').strip().upper()
    idade = input(f'Qual a idade da {vez}° pessoa: ').strip()
    while not idade.isdigit():
        idade = input(f'Qual a idade da {vez}° pessoa: ').strip()
    idade = int(idade)
    if sexo == 'M':
        homens += 1
    if idade > 18:
        todos18 += 1
    if idade < 20 and sexo == 'F':
        mulher20 += 1
    resposta = input('Quer para? [S/N]').strip().upper()
    while resposta != 'S' and resposta != 'N':
        resposta = input('Quer para? [S/N]').strip().upper()
    if resposta == 'S':
        break

print(f'O total de pessoas cadastradas acima de 18 anos foram {todos18}')
print(f'O total de homens cadastrados foram {homens}')
print(f'O total de mulheres cadastrados abaixo de 20 anos foram {mulher20}')
