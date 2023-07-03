nome_completo = input("Digite o seu nome completo: ")

# Dividindo o nome completo em partes separadas
nomes = nome_completo.split()

# Primeiro nome
primeiro_nome = nomes[0]

# Último nome
ultimo_nome = nomes[-1]

print(f"Primeiro nome: {primeiro_nome}")
print(f"Último nome: {ultimo_nome}")