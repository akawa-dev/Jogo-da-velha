import random

# Jogadas disponíveis
def jogadas_livres(tabuleiro):
    livres = []
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == " ":
                livres.append((i, j))
    return livres


# Bot  fácil
def bot_facil(tabuleiro):
    return random.choice(jogadas_livres(tabuleiro))


# Bot médio
def bot_medio(tabuleiro):
    # tenta ganhar
    for i, j in jogadas_livres(tabuleiro):
        tabuleiro[i][j] = "O"
        if venceu(tabuleiro, "O"):
            tabuleiro[i][j] = " "
            return (i, j)
        tabuleiro[i][j] = " "

    # tenta impedir
    for i, j in jogadas_livres(tabuleiro):
        tabuleiro[i][j] = "X"
        if venceu(tabuleiro, "X"):
            tabuleiro[i][j] = " "
            return (i, j)
        tabuleiro[i][j] = " "

    # aleatório
    return bot_facil(tabuleiro)


