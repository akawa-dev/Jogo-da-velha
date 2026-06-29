from bot import bot_facil, bot_medio, bot_dificil



# criar o tabuleiro
def inicializar_tabuleiro():
   return [[" " for _ in range(3)] for _ in range(3)]

# printar o tabuleiro
def exibir_tabuleiro(tabuleiro):
   for linha in tabuleiro:
       print("|".join(linha))
       print("-" * 5)

# Verificar vitória
def verificar_vencedor(tabuleiro, jogador):
    # linhas
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

# Verificar empate
def verificar_empate(tabuleiro):
   for linha in tabuleiro:
       if " " in linha:
           return False
   return True

# jogo
def jogar():
   tabuleiro = inicializar_tabuleiro()
   jogador = proximo_inicio
   
   
   while True:
       exibir_tabuleiro(tabuleiro)
       print(f"Jogador {jogador}, é sua vez!")

       #entrada 
       try:

            if modo == 2 and jogador == "O":
                if dificuldade == 1:
                    linha, coluna = bot_facil(tabuleiro)
                
                elif dificuldade == 2:
                    linha, coluna = bot_medio(tabuleiro, verificar_vencedor)
                
                elif dificuldade == 3:
                    jogada = bot_dificil(tabuleiro, verificar_vencedor)
                    linha, coluna = jogada
                print("Bot jogou, é sua  vez!")

            else:
                linha = int(input("Escolha a linha (0-2): "))
                coluna = int(input("Escolha a coluna (0-2): "))

            if tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = jogador

                if verificar_vencedor(tabuleiro, jogador):
                    exibir_tabuleiro(tabuleiro)
                    print(f"Jogador {jogador} venceu!\n")
                    vencedor = jogador
                    return vencedor
                    

                if verificar_empate(tabuleiro):
                    exibir_tabuleiro(tabuleiro)
                    print("Empate!")
                    break

                    # trocar jogador
                if jogador == "X":
                    jogador = "O"
                else:
                    jogador = "X"

                # posição ocupada
            else:
                print("Posição já ocupada. Tente novamente.\n")

       #entrada com valores errados
       except (ValueError, IndexError):
           print("Entrada inválida. Escolha números entre 0 e 2.\n")

           
# Iniciar 
proximo_inicio = "X"
while True:
    # Escolha do modo
    modo = int(input("Escolha um modo \n1 - Multiplayer Local \n2 - Contra a Máquina \n"))

    # dificuldade
    dificuldade = 1
    if modo == 2: 
     dificuldade = int(input("Selecione a dificuldade do jogo\n1 - Fácil \n2 - Médio \n3 - Difícil \n"))

    vencedor = jogar()
    
    # Trocar de jogador inicial
    if vencedor == "X":
        proximo_inicio = "O"
    elif vencedor == "O":
        proximo_inicio = "X"
        # empate
    else:
        proximo_inicio = "X"  

    # jogar denovo ou não
    resposta = input("\nDeseja jogar novamente? (s/n): \n").strip().lower()
    if resposta == "s":
        print("Reiniciando o jogo...\n")
    else:
        print("Encerrando o jogo...\n")
        break