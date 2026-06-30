from bot import bot_facil, bot_medio, bot_dificil


# ─── Placar ────────────────────────────────────────────────────────────────────
placar = {"X": 0, "O": 0, "Empates": 0}

def exibir_placar(modo):
    print("\n" + "=" * 30)
    print("         📊 PLACAR")
    print("=" * 30)
    if modo == 1:
        print(f"  Jogador X : {placar['X']} vitória(s)")
        print(f"  Jogador O : {placar['O']} vitória(s)")
    else:
        print(f"  Jogador   : {placar['X']} vitória(s)")
        print(f"  Bot (O)   : {placar['O']} vitória(s)")
    print(f"  Empates   : {placar['Empates']}")
    print("=" * 30 + "\n")


# ─── Tabuleiro ─────────────────────────────────────────────────────────────────
def inicializar_tabuleiro():
    return [[" " for _ in range(3)] for _ in range(3)]

def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)


# ─── Lógica ────────────────────────────────────────────────────────────────────
def verificar_vencedor(tabuleiro, jogador):
    # linhas e colunas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador:
            return True
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador:
            return True

    # diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True

    return False

def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True


# ─── Partida ───────────────────────────────────────────────────────────────────
def jogar():
    tabuleiro = inicializar_tabuleiro()
    jogador = proximo_inicio

    while True:
        exibir_tabuleiro(tabuleiro)
        print(f"Jogador {jogador}, é sua vez!")

        try:
            if modo == 2 and jogador == "O":
                if dificuldade == 1:
                    linha, coluna = bot_facil(tabuleiro)
                elif dificuldade == 2:
                    linha, coluna = bot_medio(tabuleiro, verificar_vencedor)
                elif dificuldade == 3:
                    jogada = bot_dificil(tabuleiro, verificar_vencedor)
                    linha, coluna = jogada
                print("Bot jogou, é sua vez!")
            else:
                linha = int(input("Escolha a linha (0-2): "))
                coluna = int(input("Escolha a coluna (0-2): "))

            if tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = jogador

                if verificar_vencedor(tabuleiro, jogador):
                    exibir_tabuleiro(tabuleiro)
                    if modo == 2 and jogador == "O":
                        print("Bot venceu! Melhor sorte na próxima.\n")
                    else:
                        print(f"Jogador {jogador} venceu!\n")
                    placar[jogador] += 1
                    return jogador

                if verificar_empate(tabuleiro):
                    exibir_tabuleiro(tabuleiro)
                    print("Empate!")
                    placar["Empates"] += 1
                    return None

                # trocar jogador
                jogador = "O" if jogador == "X" else "X"
            else:
                print("Posição já ocupada. Tente novamente.\n")

        except (ValueError, IndexError):
            print("Entrada inválida. Escolha números entre 0 e 2.\n")


# ─── Iniciar ───────────────────────────────────────────────────────────────────
proximo_inicio = "X"
while True:
    # Escolha do modo
    modo = int(input("Escolha um modo \n1 - Multiplayer Local \n2 - Contra a Máquina \n"))

    # Dificuldade
    dificuldade = 1
    if modo == 2:
        dificuldade = int(input("Selecione a dificuldade do jogo\n1 - Fácil \n2 - Médio \n3 - Difícil \n"))

    # Exibir placar antes de iniciar a partida
    exibir_placar(modo)

    vencedor = jogar()

    # Exibir placar atualizado ao final da partida
    exibir_placar(modo)

    # Trocar de jogador inicial
    if vencedor == "X":
        proximo_inicio = "O"
    elif vencedor == "O":
        proximo_inicio = "X"
    else:
        proximo_inicio = "X"  # empate

    # Jogar de novo ou não
    resposta = input("\nDeseja jogar novamente? (s/n): \n").strip().lower()
    if resposta == "s":
        print("Reiniciando o jogo...\n")
    else:
        print("Encerrando o jogo...\n")
        break