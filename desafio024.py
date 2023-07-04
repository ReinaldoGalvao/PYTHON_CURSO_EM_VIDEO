#crie um programa que leia o nome de uma pessoa e diga se ela começa com "Santo".

nome = input('Diga o nome da sua CIDADE: ').strip()

nomeupper = nome.upper()

print(nomeupper)

nomeupperlista = nomeupper.split()
primeironomeupper = nomeupperlista[0]

while primeironomeupper == 'SANTO':
    print(f'Tem SANTO como primeiro nome sim.')
    break
else:
    print(f'Não tem SANTO como primeiro nome.')