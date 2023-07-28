'''
Faça um programa que leia o sexo de uma pessoa, 
mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até
ter um valor correto.
'''
'''sexo = input('Diga seu sexo (F)para feminino ou (M)para masculino:  ').upper().strip()

while sexo != 'F' and sexo != 'M':
    print('Seu sexo é {}'.format(sexo))
    sexo = input('Diga seu sexo (F)para feminino ou (M)para masculino:  ').upper().strip()
    if sexo == 'F':
        print('Você escolheu o sexo Feminino')
        
    if sexo == 'M':
        print('Você escolheu o sexo Masculino')
        '''
def salvar_sexo():
    while True:
        sexo = input('Diga seu sexo (F)para feminino ou (M)para masculino:  ').upper().strip()
        if sexo == 'M':
            print("Sexo digitado: Masculino")
            return sexo
        elif sexo == 'F':
            print("Sexo digitado: Feminino")
            return sexo
        else:
            print("Valor incorreto. Digite apenas 'M' ou 'F'.")

sexo = salvar_sexo()