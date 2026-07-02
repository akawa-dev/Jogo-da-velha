import random

# jogadas disponíveis
def jogadas_livres(tabuleiro):
    livres = []
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == " ":
                livres.append((i, j))
    return livres


# bot fácil 
def bot_facil(tabuleiro):
    return random.choice(jogadas_livres(tabuleiro))


# bot médio
def bot_medio(tabuleiro, venceu):
    # tenta ganhar
    for i, j in jogadas_livres(tabuleiro):
        tabuleiro[i][j] = "O"
        if venceu(tabuleiro, "O"):
            tabuleiro[i][j] = " "
            return (i, j)
        tabuleiro[i][j] = " "

    # tenta impedir o jogador de ganhar
    for i, j in jogadas_livres(tabuleiro):
        tabuleiro[i][j] = "X"
        if venceu(tabuleiro, "X"):
            tabuleiro[i][j] = " "
            return (i, j)
        tabuleiro[i][j] = " "

    return bot_facil(tabuleiro)

# Bot difícil — algoritmo Minimax (imbatível)
def minimax(tabuleiro, venceu, profundidade, maximizando):
    '''Avalia recursivamente o tabuleiro e retorna a pontuação da jogada.'''
    # Caso o bot (O) tenha ganho
    if venceu(tabuleiro, "O"):
        return 10 - profundidade
    # Caso o humano (X) tenha ganho
    if venceu(tabuleiro, "X"):
        return profundidade - 10
    # Empate (sem jogadas livres)
    if not jogadas_livres(tabuleiro):
        return 0

    if maximizando:  # vez do bot (O) — quer maximizar
        melhor = -float("inf")
        for i, j in jogadas_livres(tabuleiro):
            tabuleiro[i][j] = "O"
            pontos = minimax(tabuleiro, venceu, profundidade + 1, False)
            tabuleiro[i][j] = " "
            melhor = max(melhor, pontos)
        return melhor
    else:            # vez do humano (X) — quer minimizar
        melhor = float("inf")
        for i, j in jogadas_livres(tabuleiro):
            tabuleiro[i][j] = "X"
            pontos = minimax(tabuleiro, venceu, profundidade + 1, True)
            tabuleiro[i][j] = " "
            melhor = min(melhor, pontos)
        return melhor


def bot_dificil(tabuleiro, venceu):
    """Escolhe a melhor jogada possível usando Minimax."""
    melhor_pontos = -float("inf")
    melhor_jogada = None

    for i, j in jogadas_livres(tabuleiro):
        tabuleiro[i][j] = "O"
        pontos = minimax(tabuleiro, venceu, 1, False)
        tabuleiro[i][j] = " "

        if pontos > melhor_pontos:
            melhor_pontos = pontos
            melhor_jogada = (i, j)
    
    if melhor_jogada is None:
        return random.choice(jogadas_livres(tabuleiro))

    return melhor_jogada