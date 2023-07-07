#crie um programa que leia 2 notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

notas = []

for i in range(2):
    nota = float(input('Diga a nota: '))
    notas.append(nota)
    
media = (notas[0] + notas[1]) /2

if media < 5.0:
    print(f'Sua media foi {media:.2f} e você está REPROVADO.')
    
elif media > 5.0 and media < 6.9 :
    print(f'Sua media foi {media:.2f} e você está RECUPERAÇÃO.')
    
elif media >= 7.0:
    print(f'Sua media foi {media:.2f} e você está APROVADO.') 