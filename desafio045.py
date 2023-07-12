import random


def jogar_jogo():
    opcoes = ['Pedra', 'Papel', 'Tesoura']
    jogador_point = 50
    computador_point = 50

    while True:
        # Solicitar ao jogador que escolha uma opção
        jogador = input('Escolha entre Pedra, Papel ou Tesoura (ou Sair para encerrar o jogo): ').capitalize()

        # Verificar se o jogador deseja encerrar o jogo
        if jogador == 'Sair':
            print('Jogo acabou.')
            break

        # Verificar se a opção do jogador é válida
        if jogador not in opcoes:
            print('Opções inválidas. Tente novamente.')
            continue

        # Solicitar a aposta do jogador e o pagamento do computador
        aposta = float(input('Digite o valor da sua aposta: '))
        pagamento = float(input('Digite o valor que o computador pagará na sua vitória: '))

        # Gerar a jogada do computador
        computador = random.choice(opcoes)

        # Exibir a escolha do jogador e do computador
        print(f'Você escolheu: {jogador}')
        print(f'O computador escolheu: {computador}')

        # Verificar o resultado do jogo
        if jogador == computador:
            print('Empate! Ninguém ganha a aposta.')
        elif (jogador == 'Pedra' and computador == 'Tesoura') or (jogador == 'Papel' and computador == 'Pedra') or (jogador == 'Tesoura' and computador == 'Papel'):
            print('Você ganhou! O computador paga a aposta.')
            jogador_point -= aposta
            computador_point += pagamento
            aposta_necessaria = jogador_point / (pagamento - 1)
            print(f'Você precisa apostar {aposta_necessaria:.2f} para recuperar a sua pontuação atual.')
        else:
            print('O computador ganhou! Você perde a aposta.')
            jogador_point += aposta * (pagamento - 1)
            computador_point -= aposta
        print(f'Jogador: {jogador_point} x Computador: {computador_point}\n')

jogar_jogo()
