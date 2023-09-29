'''
Crie uma funçao leiaInt(), que vai funcionar de forma semelhante a função input() do Python
só que fazendo a validação para aceitar apenas um valor numerico.

Ex:
n = leiaInt('Digite um numero')
'''

def leiaInt(msg):
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Por favor, digite um número inteiro válido.')
        if ok:
            break
    return valor

n = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o número {n}')
