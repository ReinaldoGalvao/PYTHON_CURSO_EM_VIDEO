#desenvolva um programa que leia as 2 notas de um aluno, calcule e mostre a média.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
soma = nota1 + nota2
media = soma / 2

print(f'A primeira nota foi {nota1} a segunda nota foi {nota2}, somando as duas notas são {soma} e sua média é {media}.')