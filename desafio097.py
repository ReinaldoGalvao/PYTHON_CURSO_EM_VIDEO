'''
Crie um progtama que tenha uma função chamada escreva(), que recebe um texto qualquer como 
parametro e mostre uma mensagem com o tamanho adaptavel
'''
frase = str(input('Diga o texto da mensagem: '))
def escreva(txt):
    tamanho = len(txt) + 1
    print('=' * tamanho)
    print(txt) 
    print('=' * tamanho)
    
escreva(frase)
