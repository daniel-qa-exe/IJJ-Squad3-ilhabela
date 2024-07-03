import os

dados = ["maçã", "banana", "uva", "morango", "pera", "abacaxi", "kiwi"]

pasta = "frutas"
if not os.path.exists(pasta):
    os.makedirs(pasta)

caminho_arquivo = os.path.join(pasta, "lista-frutas.txt")
with open(caminho_arquivo, "w") as arquivo:
    for linha in dados:
        arquivo.write(linha + "\n")

print(f"Arquivo salvo em: {caminho_arquivo}")