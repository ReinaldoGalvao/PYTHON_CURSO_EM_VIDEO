def obter_numero():
    while True:
        valor = input('Diga um numero: ').strip()
        if valor.isnumeric():
            return int(valor)
        else:
            print("Valor inválido. Digite um número válido.")

numero = 0
qts = 0
soma = 0
resposta = ''
media = 0
maior = 0
menor = 0
primeira_vez = True

while True:
    if resposta == 'S':
        break
    while True:
        numero = obter_numero()
        qts += 1
        soma = soma + numero
        if primeira_vez:
            menor = numero
            primeira_vez = False
        if numero > maior:
            maior = numero
        if menor > numero:
            menor = numero
        resposta = input('Quer parar? S para sim / N para nao: ').upper().strip()
        while resposta != 'S' and resposta != 'N':
            resposta = input('Quer parar? S para sim / N para nao: ').upper().strip()
        else:
            break

media = soma / qts
print(f'A soma desses {qts} numeros são de: {soma}')
print(f'O menor numero é {menor} e o maior numero é: {maior}')
print(f'A media dos {qts} numeros digitados é: {media:.2f}')
print('FIM')
