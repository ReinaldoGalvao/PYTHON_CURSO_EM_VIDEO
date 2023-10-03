def aumentar(x=0, y=0):
    soma = x + y
    return soma

def diminuir(x=0, y=0):
    diminuir = x - y
    return diminuir

def dobro(x=0):
    dobro = x * 2
    return dobro

def metade(x=0):
    metade = x / 2
    return metade

def porcentagem(x=0, y=0):
    porcentagem = x + (x * y /100) 
    return porcentagem

def porcentagemmenos(x=0, y=0):
    porcentagem = x - (x * y /100) 
    return porcentagem

def moeda(x=0, moeda='R$'):
    return f'{moeda}{x:.2f}'.replace('.', ',')