
numero = 0
qts = 0
soma = 0
resposta = ''
media = 0
maior= 0
menor = 0
primeira_vez = True

while True:
    if resposta == 'S':
        break
    while True:
        numero = int(input('Diga um numero: '))
        qts += 1
        soma = soma + numero
        if primeira_vez:
            menor = numero + 1
            primeira_vez = False
        if numero > maior:
            maior = numero
        if menor > numero:
            menor = numero
        resposta = input('Quer para? S para sim / N para nao: ').upper()
        if resposta != 'S':
            continue
        else:
            break
media = soma / qts
print(f'A soma desses {qts} numeros são de : {soma}')
print(f'O menor numero é {menor} e o maior numeros é: {maior}')
print(f'A media dos {qts} numeros digitados é: {media:.2f}')
print('FIM')

