def aumentar(x=0, y=0, formato=False):
    soma = x + y
    return soma if formato is False else moeda(soma)

def diminuir(x=0, y=0, formato=False):
    diminuir = x - y
    return diminuir if formato is False else moeda(diminuir)

def dobro(x=0, formato=False):
    dobro = x * 2
    return dobro if not formato else moeda(dobro)

def metade(x=0, formato=False):
    metade = x / 2
    return metade if not formato else moeda(metade)

def porcentagem(x=0, y=0, formato=False):
    porcentagem = x + (x * y /100) 
    return porcentagem if formato is False else moeda(porcentagem)

def porcentagemmenos(x=0, y=0, formato=False):
    porcentagem = x - (x * y /100) 
    return porcentagem if formato is False else moeda(porcentagem)

def moeda(x=0, moeda='R$'):
    return f'{moeda}{x:.2f}'.replace('.', ',')

def resumo(preco =0, taxaa=10, taxar=5):
    print('-'*40)
    print('RESUMO DO VALOR'.center(30))
    print('-'*40)
    print(f'Preço analizado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco ,True)}')
    print(f'Com {taxaa}% de aumento: \t{porcentagem(preco, taxaa, True)}')
    print(f'Com {taxar}% de redução: \t{porcentagemmenos(preco, taxar, True)}')
    print('-'*40)