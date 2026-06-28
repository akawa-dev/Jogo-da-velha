import random


def jogadas_livres(tabuleiro):
    livres = []
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == " ":
                livres.append((i, j))
    return livres


# bot  fácil
def bot_facil(tabuleiro):
    return random.choice(jogadas_livres(tabuleiro))


# bot médio
def bot_medio(tabuleiro):
    # 1. tenta ganhar
    for i, j in jogadas_livres(tabuleiro):
        tabuleiro[i][j] = "O"
        if venceu(tabuleiro, "O"):
            tabuleiro[i][j] = " "
            return (i, j)
        tabuleiro[i][j] = " "

    # 2. tenta impedir
    for i, j in jogadas_livres(tabuleiro):
        tabuleiro[i][j] = "X"
        if venceu(tabuleiro, "X"):
            tabuleiro[i][j] = " "
            return (i, j)
        tabuleiro[i][j] = " "

    # 3. aleatório
    return bot_facil(tabuleiro)


