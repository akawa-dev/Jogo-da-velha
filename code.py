from bot import bot_facil, bot_medio

# Escolha do modo
modo = int(input("Escolha um modo \n1 - Multiplayer Local \n2 - Contra a Máquina \n"))
if modo == 2: 
    int(input("Selecione a dificuldade \n1 - Fácil \n2 - Médio \n3 - Difícil"))
# criar o tabuleiro
def inicializar_tabuleiro():
   return [[" " for _ in range(3)] for _ in range(3)]

# printar o tabuleiro
def exibir_tabuleiro(tabuleiro):
   for linha in tabuleiro:
       print("|".join(linha))
       print("-" * 5)

# Verificar vitória
def verificar_vencedor(tabuleiro):

   # linhas e colunas
   for i in range(3):
       if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " ":
           return True
       if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != " ":
           return True

   # diagonais
   if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
       return True
   if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
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
   jogador = "X"
   
   while True:
       exibir_tabuleiro(tabuleiro)
       print(f"Jogador {jogador}, é sua vez!")

       #entrada
       try:
           linha = int(input("Escolha a linha (0-2): "))
           coluna = int(input("Escolha a coluna (0-2): "))

           if tabuleiro[linha][coluna] == " ":
               tabuleiro[linha][coluna] = jogador

               if verificar_vencedor(tabuleiro):
                   exibir_tabuleiro(tabuleiro)
                   print(f"Jogador {jogador} venceu!")
                   break

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
               print("Posição já ocupada. Tente novamente.")

       #entrada com valores errados
       except (ValueError, IndexError):
           print("Entrada inválida. Escolha números entre 0 e 2.")
# Iniciar
jogar()

