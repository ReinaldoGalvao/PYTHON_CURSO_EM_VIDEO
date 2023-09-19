'''
Crie um programa onde o usuario digite uma expressao qualquer que use parenteses. 
Seu aplicativo devera analizar se a expressao passada esta com os parenteses abertos e fechados na ordem correta
'''

expr = str(input('Digite uma expressao: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Está correto!')
else:
    print('Está errado!')
    