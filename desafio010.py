#crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos dolares ela pode comprar

dolar = ''
dinheiro = float(input('Quanto de dinhero você tem na carteira? '))
dolar = float(input('Digite o valor do dolar hoje: '))
conversao_dolar = dinheiro / dolar
print(f'Você tem {conversao_dolar:.2f} dolares na conversão dos {dinheiro:.2f} reias que está na sua carteira.')


"""
import requests

# Faz a requisição GET para a API que retorna a taxa de câmbio atual do dólar
response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    data = response.json()
    
    # Obtém o valor da taxa de câmbio do dólar em relação ao Real
    taxa_cambio = data["rates"]["BRL"]
    
    # Lê o valor em dinheiro que a pessoa tem na carteira
    dinheiro_carteira = float(input("Informe o valor em dinheiro que você tem na carteira: "))
    
    # Calcula a quantidade de dólares que podem ser comprados
    valor_dolares = dinheiro_carteira / taxa_cambio
    
    # Exibe o resultado
    print(f"Com o valor de R${dinheiro_carteira:.2f} na carteira e a taxa de câmbio de {taxa_cambio:.2f}, você pode comprar US${valor_dolares:.2f}.")
else:
    print("Erro na requisição. Não foi possível obter a taxa de câmbio do dólar.")
"""