"""
Faça um program,a que leia um angulo qualquer e mostre seu seno, cosseno e tangente de um angulo.

"""
import math

angulo = float(input('Diga o ângulo do circulo: '))
rad = math.radians(angulo)
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

print(f'Para o angulo de {angulo}°, temos o seno de {seno:.2f} , cosseno de {cosseno:.2f} e a tangente de {tangente:.2f}.')