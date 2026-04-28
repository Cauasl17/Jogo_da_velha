def exibir_tabuleiro(tabuleiro):
    # Mostra o jogo na tela
    print("\n")

    # 3 linhas do tabuleiro
    for i in range(3):
        # Desenha uma linha: casa | casa | casa
        print(f" {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} ")

        # Separador entre as linhas
        if i < 2:
            print("---+---+---")

    print("\n")


def verificar_vencedor(tab, jogador):
    # Procura 3 iguais: linha ou coluna
    for i in range(3):
        # Linha completa OU coluna completa
        if all([tab[i][j] == jogador for j in range(3)]) or \
           all([tab[j][i] == jogador for j in range(3)]):
            return True

    # Procura 3 iguais nas diagonais
    if tab[0][0] == tab[1][1] == tab[2][2] == jogador or \
       tab[0][2] == tab[1][1] == tab[2][0] == jogador:
        return True

    # Se não achou vitória
    return False


def verificar_empate(tabuleiro):
    # Empate = tabuleiro cheio
    for linha in tabuleiro:
        # Se ainda tem espaço, não empatou
        if " " in linha:
            return False

    # Sem espaço vazio = empate
    return True


def jogada_valida(tabuleiro, linha, coluna):
    # Confere se a posição existe
    if 0 <= linha <= 2 and 0 <= coluna <= 2:
        # Só pode jogar em casa vazia
        return tabuleiro[linha][coluna] == " "

    # Fora do tabuleiro
    return False


def jogar():
    # Cria uma matriz 3x3 vazia
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

    # X sempre começa
    jogador_atual = "X"

    print("--- BEM-VINDO AO JOGO DA VELHA ---")

    # Loop principal do jogo
    while True:
        # Mostra o tabuleiro atual
        exibir_tabuleiro(tabuleiro)

        # Mostra de quem é a vez
        print(f"Vez do jogador ({jogador_atual})")

        try:
            # Jogador escolhe linha e coluna
            lin = int(input("Escolha a linha (0, 1, 2): "))
            col = int(input("Escolha a coluna (0, 1, 2): "))

            # Se a jogada for possível
            if jogada_valida(tabuleiro, lin, col):
                # Marca X ou O no tabuleiro
                tabuleiro[lin][col] = jogador_atual

                # Depois da jogada, verifica vitória
                if verificar_vencedor(tabuleiro, jogador_atual):
                    exibir_tabuleiro(tabuleiro)
                    print(f"Parabéns! O jogador '{jogador_atual}' venceu!")
                    break

                # Se ninguém venceu, verifica empate
                if verificar_empate(tabuleiro):
                    exibir_tabuleiro(tabuleiro)
                    print("O jogo terminou em empate!")
                    break

                # Troca X por O, ou O por X
                jogador_atual = "O" if jogador_atual == "X" else "X"

            else:
                # Posição ocupada ou fora do limite
                print("Jogada inválida! Tente novamente em uma célula vazia.")

        except ValueError:
            # Se a pessoa digitar letra em vez de número
            print("Por favor, digite números inteiros entre 0 e 2.")


# Só começa se este arquivo for executado direto
if __name__ == "__main__":
    jogar()
