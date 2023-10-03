import moeda
p = int(input('Diga um valor R$: '))
porcen = int(input(f'Diga quantos %: '))

print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, formato=True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, formato=True)}')
print(f'Aumentando {porcen}% temos {moeda.porcentagem(p, porcen, formato=True)}')
print(f'Diminuindo {porcen}% temos {moeda.porcentagemmenos(p, porcen, formato=True)}')