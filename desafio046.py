'''faça um programa que mostre na tela uma contagem regressiva
para o estouro de fogos de artificios, indo de 10 até 0, com uma pausa de 1 segundo antre eles.
'''
import time
for c in range(10, -1, -1):
    print(c)
    time.sleep(1)