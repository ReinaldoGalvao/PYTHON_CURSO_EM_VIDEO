'''
Creie um programa que leia uma frase qualquer e diga se ela é
um palindroma, desconsiderando os espaços.
'''



def is_palindroma(frase):
    frase_junta = frase.replace(' ', '')
    frase_revertida = frase_junta[::-1]
    return frase_junta == frase_revertida

a = 'apos a sopa'
b =  'o lobo ama o bolo'

print(is_palindroma(a))
print(is_palindroma(b))