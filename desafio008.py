#escrva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

mRua =  float(input('Fale quantos metros tem a sua rua: '))
cRua = mRua*100 #centimetros
mmRua = mRua*1000 #milimetros

print(f'A rua onde você mora tem: \n   {mRua} metros \n   {cRua} centimetros \n   {mmRua} milimetros ')