#parender base numericas

nun = int(input('Digite um numero: '))
print('''Escolha uma das bases para conversão:
[ 1 ]converter para BINÁRIO  
[ 2 ]converter para OCTAL
[ 3 ]converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))

while opcao not in [1, 2, 3]:
    print('Opção inválida. Tente novamente.')
    opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{nun} convertido para BINÁRIO é igual a {bin(nun)[2:]}')
    
elif opcao == 2:
    print(f'{nun} convertido para OCTAL é igual a {oct(nun)[2:]}')

elif opcao == 3:
    print(f'{nun} convertido para HEXADECIMAL é igual a {hex(nun)[2:]}')