'''
Creie um programa que leia uma frase qualquer e diga se ela é
um palindroma, desconsiderando os espaços.
'''

frase = str(input('Digite uma frase: ')).strip().upper()
print(frase)
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

"""inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]"""

if junto == inverso:
    print('É palindroma')
else:
    print('Não é palindroma')
print(junto, inverso)



"""
def is_palindroma(frase):
    frase_junta = frase.replace(' ', '')
    frase_revertida = frase_junta[::-1]
    return frase_junta == frase_revertida

a = 'apos a sopa'
b =  'o lobo ama o bolo'

print(is_palindroma(a))
print(is_palindroma(b))"""