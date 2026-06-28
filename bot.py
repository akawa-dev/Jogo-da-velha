import random


def jogadas_livres(tabuleiro):
    livres = []
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == " ":
                livres.append((i, j))
    return livres


# 🟢 FÁCIL → aleatório
def bot_facil(tabuleiro):
    return random.choice(jogadas_livres(tabuleiro))


# 🟡 MÉDIO → tenta ganhar ou bloquear
def bot_medio(tabuleiro):
    # 1. tenta ganhar
    for i, j in jogadas_livres(tabuleiro):
        tabuleiro[i][j] = "O"
        if venceu(tabuleiro, "O"):
            tabuleiro[i][j] = " "
            return (i, j)
        tabuleiro[i][j] = " "

    # 2. tenta bloquear jogador
    for i, j in jogadas_livres(tabuleiro):
        tabuleiro[i][j] = "X"
        if venceu(tabuleiro, "X"):
            tabuleiro[i][j] = " "
            return (i, j)
        tabuleiro[i][j] = " "

    # 3. aleatório
    return bot_facil(tabuleiro)


# 🔴 DIFÍCIL → minimax (IA perfeita)
def bot_dificil(tabuleiro):
    best_score = -999
    best_move = None

    for i, j in jogadas_livres(tabuleiro):
        tabuleiro[i][j] = "O"
        score = minimax(tabuleiro, 0, False)
        tabuleiro[i][j] = " "

        if score > best_score:
            best_score = score
            best_move = (i, j)

    return best_move


def minimax(tabuleiro, depth, is_max):
    if venceu(tabuleiro, "O"):
        return 1
    if venceu(tabuleiro, "X"):
        return -1
    if not jogadas_livres(tabuleiro):
        return 0

    if is_max:
        best = -999
        for i, j in jogadas_livres(tabuleiro):
            tabuleiro[i][j] = "O"
            best = max(best, minimax(tabuleiro, depth + 1, False))
            tabuleiro[i][j] = " "
        return best
    else:
        best = 999
        for i, j in jogadas_livres(tabuleiro):
            tabuleiro[i][j] = "X"
            best = min(best, minimax(tabuleiro, depth + 1, True))
            tabuleiro[i][j] = " "
        return best


# função auxiliar (duplicada aqui para simplificar o bot)
def venceu(tabuleiro, jogador):
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador:
            return True
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador:
            return True

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True

    return False