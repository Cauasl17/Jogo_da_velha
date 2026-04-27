def exibir_tabuleiro(tabuleiro):
    print("\n")
    for i in range(3):
        # Une os elementos da linha com um separador visual
        print(f" {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} ")
        if i < 2:
            print("---+---+---")
    print("\n")

def verificar_vencedor(tab, jogador):
    # Verificar linhas e colunas
    for i in range(3):
        if all([tab[i][j] == jogador for j in range(3)]) or \
           all([tab[j][i] == jogador for j in range(3)]):
            return True
            
    # Verificar diagonais
    if tab[0][0] == tab[1][1] == tab[2][2] == jogador or \
       tab[0][2] == tab[1][1] == tab[2][0] == jogador:
        return True
        
    return False

def verificar_empate(tabuleiro):
    # Se não houver nenhum espaço vazio (" "), é empate
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True

def jogada_valida(tabuleiro, linha, coluna):
    # Verifica se as coordenadas estão dentro do limite e se a célula está vazia
    if 0 <= linha <= 2 and 0 <= coluna <= 2:
        return tabuleiro[linha][coluna] == " "
    return False

def jogar():
    # Inicializa o tabuleiro vazio
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    
    print("--- BEM-VINDO AO JOGO DA VELHA ---")

    while True:
        exibir_tabuleiro(tabuleiro)
        print(f"Vez do jogador ({jogador_atual})")
        
        try:
            lin = int(input("Escolha a linha (0, 1, 2): "))
            col = int(input("Escolha a coluna (0, 1, 2): "))
            
            if jogada_valida(tabuleiro, lin, col):
                tabuleiro[lin][col] = jogador_atual
                
                if verificar_vencedor(tabuleiro, jogador_atual):
                    exibir_tabuleiro(tabuleiro)
                    print(f"Parabéns! O jogador '{jogador_atual}' venceu!")
                    break
                
                if verificar_empate(tabuleiro):
                    exibir_tabuleiro(tabuleiro)
                    print("O jogo terminou em empate!")
                    break
                
                # Alterna o jogador
                jogador_atual = "O" if jogador_atual == "X" else "X"
            else:
                print("Jogada inválida! Tente novamente em uma célula vazia.")
        
        except ValueError:
            print("Por favor, digite números inteiros entre 0 e 2.")

# Iniciar o jogo
if __name__ == "__main__":
    jogar()
