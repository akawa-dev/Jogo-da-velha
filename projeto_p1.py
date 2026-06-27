'''tabuleiro = [ 
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
                          ]
def mostrar_tabuleiro():
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-"*9)    

def verificar_vitorias(jogador):
    #linha
    for linha in tabuleiro:
        if linha.count(jogador) == 3:
            return True

    #coluna
    for col in range(3):
        if (tabuleiro[0][col] == jogador and
            tabuleiro[1][col] == jogador and
            tabuleiro[2][col] == jogador):
            return True

    #diagonal 1
    if (tabuleiro[0][0] == jogador and
        tabuleiro[1][1] == jogador and
        tabuleiro[2][2] == jogador):
        return True

    #diagonal 2
    if (tabuleiro[0][2] == jogador and
        tabuleiro[1][1] == jogador and
        tabuleiro[2][0] == jogador):
        return True    

    return False

jogador = "X"
for rodada in range(9):
        mostrar_tabuleiro()
        linha, coluna = map(int, input(f"Jogador {jogador} escolha uma posição: Linha (0-2) Coluna (0-2): ").split())
    

        if tabuleiro[linha][coluna] != " ":
            print("Espaço já ocupado!")
            continue

        tabuleiro[linha][coluna] = jogador

        if verificar_vitorias(jogador):
            mostrar_tabuleiro()
            print(f"Jogador {jogador} ganhou o jogo")
            
            
            jogador = "O" if jogador == "X" else "X"
else:
    mostrar_tabuleiro()
    print("Empate!")
    
remach = input("Deseja jogar denovo? (s/n) ").strip().lower()
if remach == "s": 
    print("Reiniciando o jogo...")
else:
    print("Parando o jogo...")
    break
'''

tabuleiro = [ 
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def mostrar_tabuleiro():
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-"*9)    

def verificar_vitorias(jogador):
    # linha
    for linha in tabuleiro:
        if linha.count(jogador) == 3:
            return True

    # coluna
    for col in range(3):
        if (tabuleiro[0][col] == jogador and
            tabuleiro[1][col] == jogador and
            tabuleiro[2][col] == jogador):
            return True

    # diagonal 1
    if (tabuleiro[0][0] == jogador and
        tabuleiro[1][1] == jogador and
        tabuleiro[2][2] == jogador):
        return True

    # diagonal 2
    if (tabuleiro[0][2] == jogador and
        tabuleiro[1][1] == jogador and
        tabuleiro[2][0] == jogador):
        return True    

    return False


jogador = "X"

for rodada in range(9):

    mostrar_tabuleiro()

    linha, coluna = map(int, input(
        f"Jogador {jogador} escolha uma posição: Linha (0-2) Coluna (0-2): "
    ).split())

    if tabuleiro[linha][coluna] != " ":
        print("Espaço já ocupado!")
        continue

    tabuleiro[linha][coluna] = jogador

    if verificar_vitorias(jogador):
        mostrar_tabuleiro()
        print(f"Jogador {jogador} ganhou o jogo")

        remach = input("Deseja jogar de novo? (s/n) ").strip().lower()
        if remach == "s":
            print("Reiniciando o jogo...")
        else:
            print("Parando o jogo...")
        break

    jogador = "O" if jogador == "X" else "X"

else:
    mostrar_tabuleiro()
    print("Empate!")