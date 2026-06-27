

# Inicializa o tabuleiro
def inicializar_tabuleiro():
   return [[" " for _ in range(3)] for _ in range(3)]
# Exibe o tabuleiro
def exibir_tabuleiro(tabuleiro):
   for linha in tabuleiro:
       print("|".join(linha))
       print("-" * 5)
# Verifica se há um vencedor
def verificar_vencedor(tabuleiro):
   # Verifica linhas e colunas
   for i in range(3):
       if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " ":
           return True
       if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != " ":
           return True
   # Verifica diagonais
   if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
       return True
   if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
       return True
   return False
# Verifica se o jogo terminou em empate
def verificar_empate(tabuleiro):
   for linha in tabuleiro:
       if " " in linha:
           return False
   return True
# Função principal do jogo
def jogar():
   tabuleiro = inicializar_tabuleiro()
   jogador_atual = "X"
   while True:
       exibir_tabuleiro(tabuleiro)
       print(f"Jogador {jogador_atual}, é sua vez!")
       try:
           linha = int(input("Escolha a linha (0-2): "))
           coluna = int(input("Escolha a coluna (0-2): "))
           if tabuleiro[linha][coluna] == " ":
               tabuleiro[linha][coluna] = jogador_atual
               if verificar_vencedor(tabuleiro):
                   exibir_tabuleiro(tabuleiro)
                   print(f"Jogador {jogador_atual} venceu!")
                   break
               if verificar_empate(tabuleiro):
                   exibir_tabuleiro(tabuleiro)
                   print("Empate!")
                   break
               jogador_atual = "O" if jogador_atual == "X" else "X"
           else:
               print("Posição já ocupada. Tente novamente.")
       except (ValueError, IndexError):
           print("Entrada inválida. Escolha números entre 0 e 2.")
# Inicia o jogo
jogar()
