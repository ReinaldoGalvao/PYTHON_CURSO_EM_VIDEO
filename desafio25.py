#crie um programa que leia o nome de uma pessoa e diga se ela "Silva" e não tive fique perguntando ate ter "Silva".

nome = input('Diga o seu nome completo: ')

nomeupper = nome.upper()

print(nomeupper)

while  True:
    if 'SILVA' in nomeupper:
        print(f'No nome {nomeupper} tem SILVA sim.')
        break
    
    else:
        nome = (input(f'No nome {nomeupper} nao temm SILVA.\n Digite um nome que tenha SILVA: '))
        continue
    
