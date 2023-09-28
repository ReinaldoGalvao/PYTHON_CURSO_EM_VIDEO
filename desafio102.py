'''
Crie um programa que tenha um função fatorial()
quer receba 2 parametros: o primeiro que indique o numero
a calcular e o outro chamado de show, que será um valor lógico
(opicional) indicando se será mostrado ou não na tela o precesso
de calculo fatorial.
'''

def fatorial(n, show=False):
    """Calula o fatorial

    Args:
        n :argumento que sera usado --- numero
        show: mostra o calculo

    Returns:
        _type_: printa na tela o resultado
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            print(' x ', end='')
        else:
            print(' = ', end='')
        f *= c
    return f


num = int(input('Diga um numero: '))
print(fatorial(num, show=True))
