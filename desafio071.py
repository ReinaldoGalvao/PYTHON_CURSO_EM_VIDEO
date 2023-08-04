
dinheiro = int(input('Diga quantos quer sacar: '))

notas50 = dinheiro // 50
resto50 = dinheiro % 50

notas20 = resto50 // 20
resto20 = resto50 % 20

notas10 = resto20 // 10
resto10 = resto20 % 10

notas1 = resto10

print(f'{notas50} notas de R$50,00')
print(f'{notas20} notas de R$20,00')
print(f'{notas10} notas de R$10,00')
print(f'{notas1} notas de R$1,00')

