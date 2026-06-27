# Tabuleiro vazio
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def mostrar_tabuleiro():
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(jogador):
    # Linhas
    for linha in tabuleiro:
        if linha.count(jogador) == 3:
            return True

    # Colunas
    for col in range(3):
        if (tabuleiro[0][col] == jogador and
            tabuleiro[1][col] == jogador and
            tabuleiro[2][col] == jogador):
            return True

    # Diagonal principal
    if (tabuleiro[0][0] == jogador and
        tabuleiro[1][1] == jogador and
        tabuleiro[2][2] == jogador):
        return True

    # Diagonal secundária
    if (tabuleiro[0][2] == jogador and
        tabuleiro[1][1] == jogador and
        tabuleiro[2][0] == jogador):
        return True

    return False

jogador = "X"

for rodada in range(9):
    mostrar_tabuleiro()

    linha = int(input(f"Jogador {jogador} - Linha (0-2): "))
    coluna = int(input(f"Jogador {jogador} - Coluna (0-2): "))

    if tabuleiro[linha][coluna] != " ":
        print("Posição ocupada!")
        continue

    tabuleiro[linha][coluna] = jogador

    if verificar_vitoria(jogador):
        mostrar_tabuleiro()
        print(f"Jogador {jogador} venceu!")
        break

    jogador = "O" if jogador == "X" else "X"

else:
    mostrar_tabuleiro()
    print("Empate!")