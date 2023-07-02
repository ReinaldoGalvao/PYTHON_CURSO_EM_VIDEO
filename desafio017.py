import math
c_oposto =  float(input('Diga o tamanho do cateto oposto: '))
c_adjacente =  float(input('Diga o tamanho do cateto adjacente: '))
hipotenusa = math.hypot(c_adjacente, c_oposto)
print(f'A hipotenusa é {hipotenusa:.2f}')