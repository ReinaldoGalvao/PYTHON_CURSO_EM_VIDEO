#crie um programa que leia o nome de uma pessoa e diga se ela começa com "Santo".

nome = input('Diga seu nome completo: ')

nomeupper = nome.upper()

print(nomeupper)

nomeupperlista = nomeupper.split()
primeironomeupper = nomeupperlista[0]

while primeironomeupper == 'SANTOS':
    print(f'Tem {primeironomeupper} como primeiro nome sim.')
    break
    
else:
    print(f'Não tem {primeironomeupper} como primeiro nome.')