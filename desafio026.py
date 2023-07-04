"""
Faça um programa que leia uma frase pelo teclado e mostre:

01 Quantas vezes aparece a letra "A" 
02 Em que posiçao aparece primeira vez a letra "A"
03 Em que posiçao aparece a letra "A" utima vez   

"""

frase = str(input('Digite um texto: ')).strip()
frase = str(input('Digite um texto: ')).upper().strip()

# Quantidade de vezes que a letra "A" aparece
frase_a = frase.upper().count('A')
print(f"A letra 'A' aparece {frase_a} vezes na frase.")
print(f"A letra 'A' aparece {frase.upper().count('A')} vezes na frase.")
print("A letra 'A' aparece {} vezes na frase.".format(frase.count('A')))

# Posição da primeira ocorrência da letra "A"
frase_primeiro_a = frase.upper().find('A')
print(f"A primeira ocorrência da letra 'A' está na posição {frase_primeiro_a +1}.")
print("A primeira ocorrência da letra 'A' está na posição {}.".format(frase.find('A')+1))

# Posição da última ocorrência da letra "A"
frase_ultimo_a = frase.upper().rfind('A')
print(f"A última ocorrência da letra 'A' está na posição {frase_ultimo_a + 1}.")
print("A última ocorrência da letra 'A' está na posição {}".format(frase.rfind('A')+1))