'''
Crei um programa onde o usuario possa digitar cinco valores numericos
e cadastre-os em uma lista, ja na posiçao correta de inserção (sem usar o sort())
no final,  mostre a lista ordenada na tela
'''

num = []
for i in range(0, 5):
    resposta = int(input('Diga um numero: '))
    if i == 0 or resposta > num[-1]:
        num.append(resposta)
    else:
        pos = 0
        while pos < len(num):
            if resposta <= num[pos]:
                num.insert(pos, resposta)
                break
            pos +=1

print(num)