'''
Crie uma funçao leiaInt(), que vai funcionar de forma semelhante a função input() do Python
só que fazendo a validação para aceitar apenas um valor numerico.

Ex:
n = leiaInt('Digite um numero')
'''

def leiaInt(msg):
    while True:
        try:
            n1 = int(input(msg))
        except (ValueError, TypeError):
            print('Você tem que digitar um número válido.')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados enterrompida pelo usuário.')
            return 0
        else:
            return n1

def leiaFloat(msg):
    while True:
        try:
            n2 = float(input(msg))
        except (ValueError, TypeError):
            print('Você tem que digitar um número válido.')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados enterrompida pelo usuário.')
            return 0
        else:
            return n2

n1 = leiaInt('Digite um numero inteiro: ')
n2 = leiaFloat('Digite um numero real: ')
print(f'Você acabou de digitar o número inteiro foi {n1} e o numero real foi {n2:.2f}')
