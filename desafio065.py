
numero = 0
qts = 0
soma = 0
resposta = ''
media = 0

while True:
    if resposta == 'S':
        break
    while True:
        if resposta == 'S':
            break
        while True:
            numero = int(input('Diga um numero: '))
            qts += 1
            soma = soma + numero
            media = soma / qts
            resposta = input('Quer para? S para sim / N para nao: ').upper()
            if resposta != 'S':
                continue
            else:
                break
media = soma / qts
print(f'A soma desses {qts} numeros são de : {soma}')
print(f'A media dos {qts} numeros digitados é: {media}')
print('FIM')

