km = int(input('Diga quantos km você andou: '))
dias = int(input('Diga quantos dias você ficou com o carro: '))

cal_km = km * 0.15
cal_dias = dias * 60
total = cal_km + cal_dias

print(f'Você rodou {km}km e isso te custou R${cal_km} \nVocê ficou com o carro {dias} dias e isso te custou R${cal_dias:.2f}\nO total de tudo ficou em R${total:.2f}')