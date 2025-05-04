import random

def gerar_arquivo_grande(nome_arquivo, tamanho_alvo_mb):
    tamanho_alvo_bytes = tamanho_alvo_mb * 1024**2
    tamanho_atual = 0

    with open(nome_arquivo, 'w') as f:
        while tamanho_atual < tamanho_alvo_bytes:
            numero = random.randint(0, 999999999)
            linha = f"{numero}\n"
            f.write(linha)
            tamanho_atual += len(linha.encode('utf-8'))

gerar_arquivo_grande("disordered_data.txt", 200)
