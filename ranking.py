import json
import os

ARQUIVO_RANKING = "players.json"

def salvar_ou_atualizar_jogador(nome, pontos_novos):
    # Se o arquivo não existir, cria um vazio
    if not os.path.exists(ARQUIVO_RANKING):
        with open(ARQUIVO_RANKING, "w", encoding="utf-8") as f:
            json.dump([], f)

    # Lê o que já está salvo
    with open(ARQUIVO_RANKING, "r", encoding="utf-8") as f:
        dados = json.load(f)
    
    # Procura se o jogador já existe para atualizar os pontos
    jogador_encontrado = False
    for jogador in dados:
        if jogador["nome"].lower() == nome.lower():
            jogador["pontos"] = max(0, jogador["pontos"] + pontos_novos) # Nunca deixa menor que 0
            jogador_encontrado = True
            break
            
    # Se for um jogador novo, adiciona ele na lista
    if not jogador_encontrado:
        dados.append({"nome": nome, "pontos": max(0, pontos_novos)})
        
    # Salva tudo de volta no arquivo
    with open(ARQUIVO_RANKING, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def exibir_ranking():
    if not os.path.exists(ARQUIVO_RANKING):
        print("Nenhum ranking registrado ainda.")
        return

    with open(ARQUIVO_RANKING, "r", encoding="utf-8") as f:
        dados = json.load(f)
        
    # Ordena quem tem mais pontos para quem tem menos
    dados_ordenados = sorted(dados, key=lambda x: x["pontos"], reverse=True)
    
    print("\n🏆 TOP 10 RANKING 🏆")
    for i, jogador in enumerate(dados_ordenados[:10], start=1):
        print(f"{i}º {jogador['nome']} - {jogador['pontos']} pts")