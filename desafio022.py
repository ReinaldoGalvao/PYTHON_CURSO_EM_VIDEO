"""
Crei um programa que leia o nome completo de uma pessoa e mostre:
01 O nome com todas letras MAIÚSCULAS
02 O nome com todas letras minusculas
03 Quantas letras ao todo (sem considerar os espaços)
04 Quantas letras tem o primeiro nome
"""
nome = str(input('Diga seu nome completo: ').strip())

print('='*20)
print(nome)
print('='*20)
print(f'Seu nome em maiuscolo é {nome.upper()}') #1
print('='*20)
print(f'Seu nome em minusculo é {nome.lower()}') #2
print('='*20)
print(f'Seu nome tem {len(nome)} letras contando os espaços.')
#print('='*20)
#print(len(nome) - nome.count(' '))#3
print('='*20)
nome_sem_espaco = (nome.replace(' ', '')) 
print(f'Seu nome tem {len(nome_sem_espaco)} letras sem contar os espaços.')
#print('='*20)
#print(len(nome.replace(' ', ''))) #3
print('='*20)
listanomes = nome.split() #4
#print(listanomes)
primeironome = listanomes[0] #4
numero_caracteresprimeiro = len(primeironome) #4
print(f'Seu primeiro nome tem {numero_caracteresprimeiro} letras.') #4
print('='*20)
print(f'Seu primeiro nome tem {nome.find(" ")} letras.')
print('='*20)
